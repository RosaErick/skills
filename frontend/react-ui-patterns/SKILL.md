---
source: original
name: react-ui-patterns
description: "Implement React loading, empty, error, retry, and mutation states without losing usable data."
---

# Model the visible states of the interaction

Inspect the query/form library and the current component boundary. Choose the project's existing data mode: ordinary queries expose explicit state; Suspense queries hand initial loading and thrown failures to boundaries. Do not mix the two models accidentally or mandate a migration between them.

For ordinary queries, distinguish initial pending with no data, initial failure with no data, empty success, success with data, and background refresh. Keep usable data visible during a refresh and show a nonblocking refresh error with a retry action when appropriate. Include every value used by an example, including its retry function.

```tsx
// TanStack Query ordinary-query example; Items and query options are app-specific.
const { data, isPending, isError, error, isFetching, refetch } = useQuery(itemsQuery);
if (isPending) return <Loading />;
if (isError && data === undefined) {
  return <ErrorMessage error={error} onRetry={() => void refetch()} />;
}
return <section aria-busy={isFetching}>
  {isError && <p role="status">Could not refresh. <button onClick={() => void refetch()}>Retry</button></p>}
  {data?.length ? <Items items={data} /> : <EmptyState />}
</section>;
```

For mutations, prevent accidental duplicate submission, retain user input on failure and provide specific recovery. Use optimistic updates only when rollback/conflict behavior is defined. Announce important async feedback accessibly and avoid moving focus unexpectedly.

Verify the changed interaction across its meaningful states. Prefer the installed library's documentation for API details; unrelated GraphQL or Formik skills are not dependencies.
