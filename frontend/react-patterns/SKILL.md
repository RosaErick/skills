---
source: original
name: react-patterns
description: "Modern React (18/19) component, hook, state and TypeScript patterns — composition, custom hooks, state placement, Context, refs, effects, Suspense and error boundaries, React Compiler and memoization, and the anti-patterns that cause re-render bugs. Use when writing or reviewing React components and hooks, deciding where state should live, choosing between useState/useReducer/Context/a store, typing props or generic components, removing unnecessary useEffect, or fixing stale closures, key bugs and wasted re-renders. Trigger terms: React component, custom hook, useState, useEffect, useReducer, Context, useMemo, useCallback, React Compiler, forwardRef, re-render, stale closure, props typing."
allowed-tools: Read, Write, Edit, Glob, Grep
metadata:
  tags: react, hooks, typescript, state-management, performance, composition
---

# React Patterns

Component and hook design for React 18/19. Framework-level concerns (routing, server rendering,
data loading in the App Router) belong to `nextjs-best-practices`; loading, error and empty state
UI belongs to `react-ui-patterns`; utility classes belong to `tailwind-patterns`.

## The three questions

Most React defects trace back to one of these being answered by accident:

1. **Does this need to be state at all?** Derived values are computed during render, not stored.
2. **Where does this state live?** The lowest common owner of everything that reads it.
3. **What synchronizes this with the outside world?** That, and only that, is an effect.

---

## 1. State: derive, don't store

```tsx
// ❌ two sources of truth; they drift the moment `items` changes
const [items, setItems] = useState<Item[]>([]);
const [total, setTotal] = useState(0);

// ✅ one source of truth
const [items, setItems] = useState<Item[]>([]);
const total = items.reduce((sum, item) => sum + item.price, 0);
```

Store the minimum. Everything that can be computed from it, compute in render — React re-runs the
component anyway, and the computation is almost always cheaper than a synchronization bug.

Only reach for `useMemo` when the derivation is measurably expensive (large sorts, heavy parsing) or
its identity feeds a dependency array.

### Choosing the state primitive

| Situation | Use |
|---|---|
| Independent values, simple updates | `useState` |
| Next value depends on the previous one, or several fields move together | `useReducer` |
| Rarely-changing value needed deep in a subtree (theme, current user, locale) | Context |
| Server data: caching, revalidation, request dedup | TanStack Query / SWR / RSC + `use()` |
| Frequently-changing client state shared across unrelated trees | Zustand / Redux Toolkit / Jotai |
| Value that must survive across renders but must not trigger one | `useRef` |
| URL-worthy state: filters, tabs, pagination | The URL (search params) |

Server state is not client state. Wrapping `fetch` in `useState` + `useEffect` reimplements caching,
deduplication, retries and race handling — badly. Use a query library or a Server Component.

### Placement

Start with the state inside the component that uses it. Move it up only when a second component
needs to read the same value. Move it into Context only when passing it down would cross three or
more layers that don't care about it. Move it into a store only when unrelated trees need it and
Context re-renders become the actual, profiled problem.

---

## 2. Effects: the escape hatch, not the workhorse

An effect synchronizes React with something outside React — a subscription, the DOM, a timer, an
analytics beacon. Everything else has a better home.

| Instead of an effect that… | Do this |
|---|---|
| Computes a value from props or state | Compute it during render |
| Resets state when a prop changes | Give the component a `key`, or derive it |
| Runs on a click or a submit | Put the logic in the event handler |
| Fetches data for the page | Query library, route loader, or a Server Component |
| Notifies a parent about a state change | Call the callback where the change happens |

```tsx
// ❌ an extra render, and it's stale for one frame
useEffect(() => { setFullName(`${first} ${last}`); }, [first, last]);

// ✅
const fullName = `${first} ${last}`;
```

When an effect is genuinely right:

```tsx
useEffect(() => {
  const controller = new AbortController();
  const socket = connect(roomId, { signal: controller.signal });
  return () => controller.abort();   // every effect that opens something closes it
}, [roomId]);
```

Rules that prevent the classic bugs:

- Every dependency the effect reads goes in the array. Never silence the lint rule — fix the design.
- Cleanup runs on unmount *and* before every re-run. Effects must be safe to run twice (Strict Mode
  does exactly that in development, on purpose).
- Reading the latest value of something without re-subscribing is what `useEffectEvent` is for
  (React 19.2) — the alternative is a ref updated in an effect.

---

## 3. Composition over configuration

A component that grows a `variant`, `isCompact`, `showHeader`, `headerSlot` set of props is asking
to be split. Pass elements, not flags.

```tsx
// ❌ boolean props multiply into untestable combinations
<Card title="Orders" showFooter footerAlign="right" compact />

// ✅ the caller composes what it needs
<Card>
  <Card.Header>Orders</Card.Header>
  <Card.Body compact>{children}</Card.Body>
  <Card.Footer align="right"><Button>Export</Button></Card.Footer>
</Card>
```

Compound components share state through a private Context and expose it as sub-components. Keep the
context internal; the consumer only ever sees the JSX.

`children` and render props are still the cheapest inversion of control there is: a component that
takes `renderItem` doesn't need to know anything about items.

### Custom hooks

Extract a hook when the *logic* repeats, not when the JSX repeats. A custom hook is a function that
calls other hooks — it must obey the same rules (top level, unconditional, `use` prefix) and it
should return a stable, minimal API.

```tsx
function useDebouncedValue<T>(value: T, delay = 300): T {
  const [debounced, setDebounced] = useState(value);
  useEffect(() => {
    const id = setTimeout(() => setDebounced(value), delay);
    return () => clearTimeout(id);
  }, [value, delay]);
  return debounced;
}
```

Signs a hook is doing too much: it returns more than four things, takes a config object, or its name
needs "and" to be accurate.

---

## 4. React 19 in practice

| API | Use it for |
|---|---|
| `use(promise)` / `use(context)` | Reading a promise or context conditionally, inside render, with Suspense handling the pending state |
| `useActionState` | Form submissions: pending flag, result and error from one reducer-shaped action |
| `useFormStatus` | A submit button that knows its parent form is pending, without prop drilling |
| `useOptimistic` | Showing the intended result before the server confirms it |
| `ref` as a prop | Function components receive `ref` directly — `forwardRef` is no longer needed |
| Ref cleanup functions | Return a cleanup from a ref callback instead of checking for `null` |
| `<Activity>` (19.2) | Keeping a subtree's state alive while hidden, instead of unmounting it |
| `useEffectEvent` (19.2) | Reading the freshest props inside an effect without re-running it |
| Document metadata in JSX | `<title>`, `<meta>`, `<link>` render anywhere and hoist to `<head>` |

```tsx
function CommentForm({ postId }: { postId: string }) {
  const [state, submit, isPending] = useActionState(
    async (_prev: State, formData: FormData) => postComment(postId, formData),
    { error: null },
  );

  return (
    <form action={submit}>
      <textarea name="body" required />
      {state.error && <p role="alert">{state.error}</p>}
      <button disabled={isPending}>{isPending ? "Posting…" : "Post"}</button>
    </form>
  );
}
```

---

## 5. Performance: measure, then act

React Compiler (stable since 2025) memoizes components and values automatically at build time. With
it enabled, hand-written `useMemo`, `useCallback` and `memo` are mostly noise — and code written to
please the compiler (rules-of-React-clean, no mutation of props or state) optimizes better than code
sprinkled with manual memos.

Without the compiler, the order is: **profile first**, then fix the specific finding.

| Symptom | Actual fix |
|---|---|
| Whole page re-renders on every keystroke | Move the input's state down into the input's own component |
| Context update re-renders everything | Split the context: one for the value, one for the setter; or a store with selectors |
| List of thousands of rows janks | Virtualize (TanStack Virtual); memoization won't save it |
| Expensive derivation on every render | `useMemo` with correct dependencies |
| Child memo never hits | The parent is passing a new object/array/function literal each render |
| Items reorder and state follows the wrong row | Stable unique `key` — never the array index |

Measure with the React DevTools Profiler and the browser's performance panel. "It feels slow"
is not a finding.

---

## 6. TypeScript

```tsx
type ButtonProps = React.ComponentPropsWithRef<"button"> & {
  variant?: "primary" | "ghost";
};

function Button({ variant = "primary", ...props }: ButtonProps) { … }
```

- Extend the DOM element's props (`ComponentPropsWithRef<"button">`) instead of hand-listing
  `onClick`, `disabled`, `className` — the caller gets everything a real button accepts.
- `children: React.ReactNode`. `React.FC` adds nothing and is worth avoiding.
- Discriminated unions beat optional props for mutually exclusive states:
  `{ status: "loading" } | { status: "error"; error: Error } | { status: "ready"; data: Data }`.
- Generic components need a generic function, not a generic const:
  `function List<T>({ items, renderItem }: { items: T[]; renderItem: (item: T) => ReactNode })`.
- Type the reducer's action union exhaustively and let the compiler catch the missing case.

---

## 7. Errors and suspense boundaries

- An error boundary per meaningful region (route, panel, widget), not one at the root that blanks the
  app. `react-error-boundary` covers the common case with a reset handler.
- Error boundaries do not catch errors in event handlers, async callbacks or `setTimeout` — handle
  those where they happen.
- `<Suspense>` marks a region that can show a fallback while something inside loads. Place it where
  the loading UI makes sense visually, not at the top of the tree.
- The fallback should be the same shape as the content it replaces, or the layout jumps.

---

## Anti-patterns

| ❌ | ✅ |
|---|---|
| `useEffect` copying props into state | Derive during render, or `key` to reset |
| `fetch` in `useEffect` with manual loading flags | Query library, route loader, or Server Component |
| Index as `key` in a reorderable list | Stable id from the data |
| One giant Context holding unrelated values | One context per concern, or a store with selectors |
| `useMemo`/`useCallback` everywhere by default | Compiler, or profile then memoize the hot path |
| Mutating state or props in place | New object/array, or `useReducer` with immutable updates |
| Conditional hooks, hooks in loops | Always top level, always the same order |
| A hook that returns eight values | Split it, or return an object with a documented shape |
| Business logic inside JSX | Extract to a function or a hook and unit-test it |

---

> React is composition. Small components, honest state, effects only at the boundary with the
> outside world — everything else in this file follows from those three.
