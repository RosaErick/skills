# Performance within this React stack

Measure a slow interaction or render before selecting an optimization. Check request waterfalls, unnecessary work and large lists before adding blanket memoization.

`useMemo` can reuse an expensive pure calculation; `useCallback` can stabilize identity when a memoized consumer or dependency needs it. A freshly created handler is not a defect by itself. Include captured reactive dependencies and account for an enabled React Compiler. Never use an empty array solely to suppress an identity change when it makes captured values stale.

For long lists, consider virtualization when measured rendering cost warrants it. Debounce only the operation that benefits, preserve immediate input feedback and cancel stale requests as appropriate. Compare the same user scenario after the change and verify behavior.
