# Loading and error boundaries

Choose the data mode already used by the component. For ordinary queries, an early return for initial pending or initial failure is valid; reserve stable space when a layout shift would harm the experience. Render a separate empty-success state.

For suspense queries, place a Suspense fallback and an error boundary at the appropriate route or section. Data is available when the child renders successfully. Do not also write unreachable initial `isLoading` branches around the suspense query.

When a background refresh fails and cached data is usable, retain the content and provide nonblocking feedback/retry. For mutations, retain input, prevent accidental duplicates and expose specific recovery. Use the app's existing snackbar/inline feedback component; a custom `useMuiSnackbar` hook is not a dependency unless the project has it.

Check initial loading, failure, empty success, populated success and a failed refresh where relevant. Preserve keyboard focus and accessible status announcements.
