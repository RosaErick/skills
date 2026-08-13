---
name: tailwind-patterns
description: "Tailwind v4: @theme tokens as CSS variables, @utility and custom variants, container queries, dark mode, cva variants, v3 migration. Use when setting up Tailwind, defining tokens or taming class soup."
allowed-tools: Read, Write, Edit, Glob, Grep
metadata:
  tags: tailwind, css, design-tokens, responsive, dark-mode, v4
---

# Tailwind Patterns (v4)

Tailwind v4 moved configuration out of JavaScript and into CSS. Tokens are real CSS variables, the
content scan is automatic, and `tailwind.config.js` is optional legacy. Everything here assumes v4.

## 1. Setup

```css
/* app.css — the whole configuration lives here */
@import "tailwindcss";

@theme {
  --color-brand-50:  oklch(0.97 0.02 264);
  --color-brand-500: oklch(0.62 0.19 264);
  --color-brand-900: oklch(0.32 0.11 264);

  --font-display: "Satoshi", ui-sans-serif, system-ui, sans-serif;
  --radius-card: 0.75rem;
  --spacing: 0.25rem;        /* the whole spacing scale derives from this */
}
```

```ts
// vite.config.ts
import tailwindcss from "@tailwindcss/vite";
export default defineConfig({ plugins: [tailwindcss()] });
```

PostCSS setups use `@tailwindcss/postcss`; there's a standalone CLI too. No `content` array — v4
detects sources automatically, and `@source` adds anything outside the project (a package's dist,
for example) or excludes noise with `@source not`.

Every theme entry becomes both a utility and a CSS variable: `--color-brand-500` gives you
`bg-brand-500` *and* `var(--color-brand-500)` for use in plain CSS, inline styles or a chart library.
That's the main reason to define tokens in `@theme` rather than raw `:root`.

## 2. Tokens: name by role, not by look

```css
@theme {
  /* palette — the raw material */
  --color-brand-500: oklch(0.62 0.19 264);
  --color-danger-500: oklch(0.58 0.22 27);

  /* semantic — what the app actually uses */
  --color-surface: var(--color-white);
  --color-surface-muted: var(--color-neutral-50);
  --color-text: var(--color-neutral-900);
  --color-text-muted: var(--color-neutral-500);
  --color-border: var(--color-neutral-200);
}
```

`bg-surface text-text-muted border-border` survives a rebrand; `bg-white text-gray-500` does not.
Two layers — palette then semantic — is the sweet spot; a third layer of aliases is bureaucracy.

Use `oklch()` for new palettes: perceptually even lightness steps, and access to colors outside sRGB
on displays that support them.

Extend the default theme by adding keys; replace a scale wholesale with `--color-*: initial` before
redefining it, when you want *only* your colors to exist.

## 3. Custom utilities and variants

```css
@utility scrollbar-none {
  scrollbar-width: none;
  &::-webkit-scrollbar { display: none; }
}

@custom-variant dark (&:where(.dark, .dark *));   /* class-based dark mode */
@custom-variant hocus (&:hover, &:focus-visible);
```

`@utility` registers a real utility — it works with variants (`md:scrollbar-none`) and respects
ordering. A bare CSS class does not. Reach for it when a genuinely reusable primitive is missing, not
as a shortcut for a component.

## 4. Responsive and container queries

Breakpoints answer "how big is the window". Container queries answer "how big is the space this
component was given" — which is the question a reusable component actually has.

```html
<div class="@container">
  <article class="flex flex-col gap-4 @md:flex-row @md:items-center">
    <img class="w-full @md:w-48" src="…" alt="" />
    <div class="@md:flex-1">…</div>
  </article>
</div>
```

Container queries are built in — no plugin. Use them for cards, sidebars, anything that appears in
more than one layout. Keep media-query breakpoints for page-level structure.

Mobile-first stays the rule: unprefixed classes are the small screen, `md:` and up are progressive
enhancement. `max-md:` exists for the rare inversion.

## 5. Dark mode

```css
@custom-variant dark (&:where(.dark, .dark *));
```

```html
<div class="bg-surface text-text dark:bg-neutral-900 dark:text-neutral-100">
```

Better: put dark values in the tokens and stop writing `dark:` at every call site.

```css
:root { --color-surface: var(--color-white); --color-text: var(--color-neutral-900); }
.dark { --color-surface: var(--color-neutral-900); --color-text: var(--color-neutral-100); }
```

Now `bg-surface text-text` is correct in both themes, and a new component can't forget its dark
variant. Follow the user's `prefers-color-scheme` by default and let an explicit choice override it;
set `color-scheme` so form controls and scrollbars match.

## 6. Taming class strings

Long class lists are fine — they're the trade you accepted. Repeated class lists are the problem, and
the fix is a component, not `@apply`.

```tsx
// button.tsx
const button = cva(
  "inline-flex items-center justify-center rounded-card font-medium transition-colors " +
  "focus-visible:outline-2 focus-visible:outline-offset-2 disabled:opacity-50 disabled:pointer-events-none",
  {
    variants: {
      variant: {
        primary: "bg-brand-500 text-white hover:bg-brand-600",
        ghost: "bg-transparent text-text hover:bg-surface-muted",
      },
      size: { sm: "h-8 px-3 text-sm", md: "h-10 px-4" },
    },
    defaultVariants: { variant: "primary", size: "md" },
  },
);

export function Button({ variant, size, className, ...props }: ButtonProps) {
  return <button className={twMerge(button({ variant, size }), className)} {...props} />;
}
```

`cva` (or `tailwind-variants`) holds the variant matrix; `tailwind-merge` resolves conflicts so a
caller's `className` actually wins instead of losing to specificity roulette.

`@apply` is the last resort — for third-party markup you can't touch, or a base layer style. It
recreates the indirection Tailwind exists to remove: the class name stops telling you what it does.

Arbitrary values (`w-[347px]`, `text-[#3b82f6]`) are an escape hatch. One is a pragmatic exception;
a file full of them means the token scale is wrong.

## 7. Migrating from v3

`npx @tailwindcss/upgrade` does most of it on a clean git tree. What it doesn't catch:

| v3 | v4 |
|---|---|
| `tailwind.config.js` theme | `@theme` in CSS (`@config` still loads a legacy file) |
| `@tailwind base/components/utilities` | `@import "tailwindcss"` |
| `bg-opacity-50`, `text-opacity-*` | `bg-black/50`, `text-white/70` |
| `flex-shrink-0`, `flex-grow` | `shrink-0`, `grow` |
| `outline-none` | `outline-hidden` (`outline-none` now really means none) |
| `shadow-sm`, `rounded-sm` | `shadow-xs`, `rounded-xs` (each scale shifted down one) |
| Default border color `gray-200` | `currentColor` — set it explicitly where you relied on the old default |
| `@layer components` | `@utility`, or a real component |

Also check: PostCSS plugin package renamed, custom plugins that read the JS config, and any tooling
that parsed `tailwind.config.js`.

---

## Anti-patterns

| ❌ | ✅ |
|---|---|
| `@apply` used to build components | A component with `cva` + `tailwind-merge` |
| `bg-white text-gray-500` everywhere | Semantic tokens: `bg-surface text-text-muted` |
| `dark:` on every element | Dark values in the tokens |
| `w-[327px]`, `mt-[13px]` scattered | Fix the scale, use the token |
| Breakpoints inside a reusable card | `@container` queries |
| Concatenating class strings by hand | `twMerge`/`clsx`, so conflicts resolve predictably |
| Dynamic class names (`text-${color}-500`) | Full class strings in a lookup map — the scanner only sees literals |
| Both a v3 config and `@theme` | One source of tokens |
