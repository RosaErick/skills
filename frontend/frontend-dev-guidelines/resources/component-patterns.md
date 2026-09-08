# Component patterns for an existing React/MUI app

Use the project's naming, export and typing convention. A typed function component or `React.FC` can both work; preserve neighboring style. Put required data in explicit props and avoid leaking internal state representation across the boundary.

Keep data ownership and UI state clear. Extract a component when it has a meaningful responsibility or reuse benefit, not to satisfy a line limit. Reuse existing layout, form and feedback primitives. Do not introduce aliases or application hooks that the repository does not define.

A component should have coherent loading/error handling at the chosen query or route boundary. Check accessibility of interactive controls and the behavior touched by the change.
