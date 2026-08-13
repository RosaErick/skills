---
name: react-review
description: Reviews React code for best practices specific to this project. Checks for hook anti-patterns, react-query misuse, stale closures, mutation of cached data, performance, error handling, state design, async safety, and component/state structure issues. Use when writing or reviewing hooks, components, or query logic.
argument-hint: [file or description of what to review]
---

Review the code provided in $ARGUMENTS (or the current file/context if no argument is given) against the React best practices below. For each issue found, show:

1. **The problem** — quote the relevant code snippet
2. **Why it's a problem** — brief, specific explanation
3. **The fix** — show the corrected code

Only report real issues. If the code is already correct, say so explicitly.

---

## React Query Rules

**RQ-1: Never mutate query cache data**
```js
// BAD — .sort() mutates the cached array in-place
setOptions(query.data.sort())

// GOOD — copy first
setOptions([...query.data].sort())
```
Same for `.reverse()`, `.splice()`, `.push()`, and any other mutating method. Applies to nested objects too — spread or deep-clone before mutating.

**RQ-2: Query keys must include all variables the fetcher depends on**
```js
// BAD — fetches with tenantId but key doesn't include it
useQuery(["estados"], () => getEstados(auth, tenantId))

// GOOD
useQuery(["estados", tenantId], () => getEstados(auth, tenantId))
```
If the query key doesn't change, react-query serves stale cache even when the fetcher would return different data.

**RQ-3: Don't sync query data to state via useEffect for display**
```js
// BAD — races between effects, stale renders, unnecessary re-renders
const [items, setItems] = useState([]);
useEffect(() => { if (query.data) setItems(query.data); }, [query.data]);

// GOOD — derive directly
const items = query.data ?? [];
// or with transformation:
const items = useMemo(() => query.data?.map(transform) ?? [], [query.data]);
```
The effect-sync pattern is only acceptable when you need to merge multiple query results into one piece of local state (e.g., paginated append). In that case, also depend on `query.dataUpdatedAt` to ensure the effect re-fires on re-fetches.

**RQ-4: Clear tenant-scoped caches on tenant switch**
When a user changes tenant/account context, call `queryClient.removeQueries` for all relevant query prefixes before the new fetch. Otherwise stale cache from the old tenant can flash or, in edge cases, be served permanently.

**RQ-5: Avoid long `staleTime` on queries scoped by a user/tenant key**
If the key already encodes tenant/user identity (e.g., `["estados", tenantId]`), a long `staleTime` provides no UX benefit but increases the risk window for showing wrong-tenant data. Keep `staleTime` at 0 or omit it for tenant-scoped queries.

**RQ-6: Always handle query error state — don't only handle data**
```js
// BAD — silently renders nothing on error
if (query.isLoading) return <Spin />;
return <Table data={query.data ?? []} />;

// GOOD — surface the error to the user
if (query.isLoading) return <Spin />;
if (query.isError) return <Alert type="error" message={query.error.message} />;
return <Table data={query.data ?? []} />;
```
`query.data` is `undefined` on error, so omitting the error check renders a blank component with no user feedback.

**RQ-7: Use select to transform data inside the query — not outside**
```js
// OK but triggers unnecessary re-renders when unrelated data in the response changes
const query = useQuery(["produtos"], fetchProdutos);
const sorted = useMemo(() => [...(query.data ?? [])].sort(...), [query.data]);

// BETTER — component only re-renders when the transformed result actually changes
const query = useQuery(["produtos"], fetchProdutos, {
  select: (data) => [...data].sort((a, b) => a.descricao.localeCompare(b.descricao)),
});
const sorted = query.data ?? [];
```

---

## Hook Rules

**HK-1: Don't call Hooks conditionally or after early returns**
```js
// BAD
if (isAdmin) {
  const data = useQuery(...); // Hook in conditional
}

// GOOD
const query = useQuery({ enabled: isAdmin, ... });
```

**HK-2: Stable references in dependency arrays**
Objects and arrays created inline are new references on every render and will cause infinite loops or excessive re-fetches.
```js
// BAD — new object every render triggers the effect every render
useEffect(() => { fetch(filters); }, [{ estado, fabricante }]);

// GOOD
const filterParams = useMemo(() => ({ estado, fabricante }), [estado, fabricante]);
useEffect(() => { fetch(filterParams); }, [filterParams]);
```

**HK-3: Exhaustive useEffect dependencies**
All values read inside a `useEffect` should be in the dependency array. Omitting them causes stale closure bugs — the effect runs with old values.
```js
// BAD — selectedTenantId inside effect but missing from deps
useEffect(() => {
  fetchData(selectedTenantId);
}, []); // stale closure

// GOOD
useEffect(() => {
  fetchData(selectedTenantId);
}, [selectedTenantId]);
```
Exceptions: `queryClient` from `useQueryClient()` is stable and can be omitted, but including it causes no harm.

**HK-4: Cleanup async effects**
Effects that start async operations should return a cleanup function to avoid state updates on unmounted components.
```js
useEffect(() => {
  let cancelled = false;
  fetchSomething().then(data => {
    if (!cancelled) setState(data);
  });
  return () => { cancelled = true; };
}, [dep]);
```
For fetch/XHR calls, prefer `AbortController` — it also cancels the in-flight network request, not just the state update:
```js
useEffect(() => {
  const controller = new AbortController();
  fetch(url, { signal: controller.signal })
    .then(r => r.json())
    .then(data => setState(data))
    .catch(err => { if (err.name !== "AbortError") setError(err); });
  return () => controller.abort();
}, [url]);
```

**HK-5: useCallback/useMemo dependency arrays must be complete**
Same rule as useEffect. A memoized function with missing deps will silently close over stale values.

**HK-6: One concern per custom hook — avoid God hooks**
A custom hook that manages 10+ pieces of state, 5 queries, and all event handlers is a maintenance liability. Split by concern:
```js
// BAD — useMonitoramentoLogic handles filters, queries, table state, export, AND chart data
// in 400 lines

// GOOD — split into focused hooks consumed by the logic hook
const filters = useMonitoramentoFilters();
const { data, isLoading, isError } = useMonitoramentoDados(filters.active);
const exportLogic = useMonitoramentoExport(data);
```
Page logic hooks (`useXxxLogic`) can compose these — they're the only entry point for the page component.

**HK-7: Return stable references from custom hooks**
If a custom hook returns an object literal on every call, consumers using that object as a dep will trigger infinite re-renders.
```js
// BAD — new object reference every render
function useFilters() {
  return { estado, fabricante, setEstado, setFabricante };
}

// GOOD — memoize the returned object
function useFilters() {
  return useMemo(
    () => ({ estado, fabricante, setEstado, setFabricante }),
    [estado, fabricante] // setters are stable, safe to omit
  );
}
```

---

## Component Rules

**CM-1: Pages are JSX only — logic lives in hooks**
Page components (`pages/*/`) should contain only JSX and `useContext` calls. All state, queries, handlers, and computed values belong in the co-located logic hook (`useXxxLogic`). If you find `useState` or `useQuery` directly in a page component, move it to the hook.

**CM-2: Don't pass auth down as props**
`auth` is available anywhere via `useAuth()`. Passing it through component props creates unnecessary coupling and makes components harder to test.

**CM-3: Derive display state — don't store it**
If a value can be computed from other state, use `useMemo` instead of `useState` + `useEffect`.
```js
// BAD — extra state that must be kept in sync
const [hasEstado, setHasEstado] = useState(false);
useEffect(() => setHasEstado(!!filters.estado), [filters.estado]);

// GOOD
const hasEstado = !!filters.estado;
```

**CM-4: Don't mutate state directly**
```js
// BAD
filters.estado = "SP";
setFilters(filters);

// GOOD
setFilters(prev => ({ ...prev, estado: "SP" }));
```

**CM-5: React 18 concurrent features — use startTransition deliberately**
Wrap only low-priority state updates (filter cascade, product list refresh) in `startTransition`. Do NOT wrap updates that must show immediate feedback (loading indicators, user input echo). Mixing them causes the UI to feel laggy.

**CM-6: Avoid inline objects and functions as JSX props**
Every render creates a new reference, which breaks `React.memo` and causes child re-renders even when nothing changed.
```js
// BAD — new object and function on every render
<FilterCard
  style={{ marginTop: 16 }}
  onChange={(val) => setFilters({ ...filters, estado: val })}
/>

// GOOD — stable references
const cardStyle = { marginTop: 16 }; // module-level constant if truly static
// or useMemo if it depends on state

const handleChange = useCallback(
  (val) => setFilters(prev => ({ ...prev, estado: val })),
  []
);
<FilterCard style={cardStyle} onChange={handleChange} />
```

**CM-7: Use discriminated unions instead of boolean flag soup**
Multiple boolean flags that encode a single concept are hard to reason about and allow impossible states.
```js
// BAD — what does isLoading=false, isError=false, isEmpty=false, hasData=false mean?
const [isLoading, setIsLoading] = useState(false);
const [isError, setIsError] = useState(false);
const [isEmpty, setIsEmpty] = useState(false);

// GOOD — one state, one truth
const [status, setStatus] = useState("idle"); // "idle" | "loading" | "success" | "empty" | "error"
```
react-query already does this for you with `query.status`. Prefer it over adding your own loading flags.

**CM-8: Wrap expensive subtrees or frequently-updated parents with React.memo**
```js
// If a parent re-renders on every keystroke but a child is expensive to render:
const ExpensiveChart = React.memo(({ data }) => {
  // Only re-renders when data actually changes
});
```
Do NOT memo everything — only measure first. Profile before adding memos.

---

## Error Handling Rules

**EH-1: Use Error Boundaries around async routes and chart components**
Network errors, JSON parse failures, and unexpected API shapes will throw during render. Without error boundaries, the entire app unmounts.
```js
// Wrap lazy-loaded routes in ErrorBoundary:
<ErrorBoundary fallback={<ErrorPage />}>
  <React.Suspense fallback={<LoadingSpin />}>
    <ProfferMonitoramento />
  </React.Suspense>
</ErrorBoundary>
```
Chart components (Chart.js) are especially prone to crashing on malformed data — always wrap them.

**EH-2: Don't swallow errors — at minimum log them**
```js
// BAD
try {
  await doSomething();
} catch (e) {
  // silently ignored
}

// GOOD
try {
  await doSomething();
} catch (e) {
  console.error("[useMonitoramentoLogic] doSomething failed:", e);
  toast.error("Erro ao carregar dados. Tente novamente.");
}
```

**EH-3: Don't treat missing data as an error — distinguish empty from failed**
```js
// BAD — throws when API returns [] legitimately
if (!query.data || query.data.length === 0) throw new Error("No data");

// GOOD
if (query.isError) return <Alert type="error" ... />;
if (!query.data?.length) return <Empty description="Sem dados para exibir" />;
return <Table data={query.data} />;
```

---

## State Design Rules

**SD-1: Colocate state as close to where it's used as possible**
Don't lift state to the logic hook if only one sub-component reads it. Lifting state unnecessarily causes unrelated components to re-render.

**SD-2: Put shareable filter state in the URL**
Filters that a user might want to bookmark, share, or restore on refresh belong in the URL query string, not in `useState`.
```js
// Current approach (local state — not shareable):
const [estado, setEstado] = useState("");

// Senior approach (URL state — shareable, survives refresh):
const [searchParams, setSearchParams] = useSearchParams();
const estado = searchParams.get("estado") ?? "";
const setEstado = (val) => setSearchParams(prev => { prev.set("estado", val); return prev; });
```
Start migrating filter state to URL when you need deep-linking or want browser back button to restore filter context.

**SD-3: Prefer useReducer over multiple useState when state updates are coupled**
When setting one piece of state always requires reading or resetting another, multiple `useState` calls lead to inconsistency windows.
```js
// BAD — filter reset requires 4 synchronized setState calls
const clearFilters = () => {
  setEstado("");
  setFabricante("");
  setFormulacao("");
  setEan(null);
};

// GOOD — atomic update
const [filters, dispatch] = useReducer(filtersReducer, initialFilters);
const clearFilters = () => dispatch({ type: "RESET" });
```

---

## Async Safety Rules

**AS-1: Prevent race conditions in sequential async operations**
If the user triggers an async op while a previous one is still in flight, results can arrive out of order.
```js
// BAD — last-write wins, result may correspond to a stale request
useEffect(() => {
  setLoading(true);
  fetchData(filters).then(data => {
    setData(data);
    setLoading(false);
  });
}, [filters]);

// GOOD — ignore results from superseded requests
useEffect(() => {
  let stale = false;
  setLoading(true);
  fetchData(filters).then(data => {
    if (!stale) {
      setData(data);
      setLoading(false);
    }
  });
  return () => { stale = true; };
}, [filters]);
```
react-query handles this automatically — another reason to keep fetches inside `useQuery` and not raw `useEffect`.

**AS-2: Treat async event handlers as fire-and-forget — add explicit loading state**
```js
// BAD — no feedback if the user clicks twice or the call is slow
const handleExport = async () => {
  await exportData(filters);
};

// GOOD
const [isExporting, setIsExporting] = useState(false);
const handleExport = async () => {
  if (isExporting) return;
  setIsExporting(true);
  try {
    await exportData(filters);
  } finally {
    setIsExporting(false);
  }
};
```

---

## Performance Rules

**PF-1: Don't re-compute expensive values on every render**
```js
// BAD — pareto calculation runs on every re-render (any state change)
const paretoData = computePareto(query.data);

// GOOD
const paretoData = useMemo(() => computePareto(query.data), [query.data]);
```

**PF-2: Virtualize long lists**
Rendering 500+ rows of a table in the DOM is slow and increases memory. Consider `react-window` or Ant Design's virtual table for large datasets.

**PF-3: Code-split below the route level for heavy components**
Charts and large data tables can be lazy-loaded independently of their parent page:
```js
const BubblePlot = React.lazy(() => import("../graphs/BubblePlot"));
```

**PF-4: useDeferredValue for non-urgent derived data**
When derived data (like a filtered list) is expensive to compute and the source updates frequently (e.g., text search), defer the expensive update:
```js
const deferredQuery = useDeferredValue(searchQuery);
const results = useMemo(() => filterItems(items, deferredQuery), [items, deferredQuery]);
```
The UI stays responsive while the filtered list catches up.

---

## Anti-Patterns Specific to This Codebase

**AP-1: Importing from deleted directories**
These directories no longer exist. Any import from them is a broken import:
- `application/` → use `providers/`, `hooks/`, `routes/`
- `infra/` → use `api/`, `config/`
- `containers/` → use `pages/`
- `libs/` → use `utils/`

**AP-2: Direct `fetch()` in components or hooks**
All HTTP calls must go through `src/api/apiClient.js`. This ensures consistent auth headers, environment switching, and error handling.

**AP-3: Calling `.sort()` or `.reverse()` on arrays from props or context**
These methods mutate the original array. Components sharing the same array reference will see unexpected mutations.

**AP-4: Theme values hardcoded in components**
Never hardcode colors. Use `isDarkMode` from `useContext(ThemeModeContext)` or Ant Design's `token` object via `theme.useToken()`.

**AP-5: Skipping the `hasTenantSelected` guard**
Never enable a query for admin users without checking `hasTenantSelected`. Querying without a selected tenant will hit the API without an `X-Tenant-Id` header and return data for the wrong scope.
