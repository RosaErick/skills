---
name: proffer-branding-guide-v1
description: Brand guide and design system reference for the Proffer application (v1). Use this skill when creating, reviewing, or auditing UI components, choosing colors, applying typography, defining spacing, or implementing effects. It ensures visual consistency and hierarchy across the entire application.
---

# Proffer Brand Guide & Design System Reference (v1)

This skill provides the complete brand identity, design tokens, component patterns, and visual hierarchy rules for the Proffer application. Use it as the single source of truth when building or reviewing any UI.

---

## 1. Brand Identity

**Product**: Proffer — a B2B SaaS platform focused on pricing intelligence and market analytics for businesses.

**Personality**: Professional, trustworthy, data-driven, growth-oriented. The brand should feel precise and modern, while remaining approachable for business users.

**Core Values**: Clarity · Precision · Growth · Trust

---

## 2. Color Palette

All colors are extracted directly from the Proffer codebase and are the established brand standards.

### Primary Green Scale
| Token Name        | Hex Value | Usage |
|-------------------|-----------|-------|
| `brand-primary`   | `#739D23` | Primary CTAs, active states, checkboxes, dividers, table headers, carousel active dots |
| `brand-hover`     | `#8DBA20` | Hover state for primary elements and links |
| `brand-light`     | `#CBDF9B` | Inactive carousel dots, subtle highlights, light backgrounds |
| `brand-dark`      | `#254000` | Hero blocks, dark emphasis, price badges, badge backgrounds |
| `brand-muted`     | `#F1F4E8` | Card hover background, light green tints |
| `brand-border`    | `rgba(115, 152, 34, 0.5)` | Card borders, input borders on plan cards |

### Neutrals
| Token Name        | Hex Value | Usage |
|-------------------|-----------|-------|
| `neutral-white`   | `#FFFFFF` | Card backgrounds, table header text |
| `neutral-divider` | `#D5D5D5` | Borders, dividers, section separators |
| `neutral-subtle`  | `#868686` | Muted text, subtle table borders |
| `neutral-dark`    | `#000000` | Primary text on light backgrounds |

### Semantic Colors
| Token Name        | Hex Value | Usage |
|-------------------|-----------|-------|
| `danger`          | `tomato`  | Strikethrough prices, error states |
| `overlay-dark`    | `rgba(0,0,0,0.7)` | Tooltip backgrounds, overlays |

### ✅ Rules
- **Never** use generic blue, red, or plain green — always use the brand scale above.
- Primary brand color `#739D23` is always the primary action color.
- Use `brand-hover` ONLY for hover/focus states — never as a static color.
- `brand-dark` (#254000) is used exclusively for high-contrast emphasis elements.

---

## 3. Typography

### Font Families
| Role | Font | Import |
|------|------|--------|
| Primary (UI) | **Inter** | Google Fonts — `wght@100..900` |
| Tables / Data | **Roboto** | Google Fonts — `sans-serif` fallback |

```css
@import url("https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400;500;600;700;800;900&display=swap");
```

### Type Scale (Responsive)
The project uses a custom responsive font scale defined in `src/utils/ResponsiveFonts.css`. All text classes automatically scale down at breakpoints.

| Class     | Default   | ≤1024px | ≤768px  | ≤640px  | ≤480px  |
|-----------|-----------|---------|---------|---------|---------|
| `text-sm` | 14px      | 13px    | 12px    | 11px    | 10px    |
| `text-base`| 16px     | 15px    | 14px    | 13px    | 12px    |
| `text-lg` | 18px      | 16px    | 15px    | 14px    | 13px    |
| `text-xl` | 20px      | 18px    | 16px    | 15px    | 14px    |
| `text-2xl`| 24px      | 22px    | 20px    | 18px    | 16px    |
| `text-3xl`| 30px      | 28px    | 24px    | 22px    | 20px    |
| `text-4xl`| 36px      | 32px    | 30px    | 28px    | 26px    |
| `text-5xl`| 48px      | 40px    | 36px    | 32px    | 30px    |

### Font Weights
| Weight | Use Case |
|--------|----------|
| 400 | Body text, captions, secondary labels |
| 500 | Sub-headings, emphasis text, form labels |
| 600 | Strong labels, list item values, table labels |
| 700 | Page titles, card headers, primary headings |
| 800–900 | Hero text only |

### Typography Hierarchy
```
H1 (Page Title)    → text-4xl / text-5xl, weight 700–800
H2 (Section Title) → text-3xl / text-2xl, weight 700
H3 (Card Title)    → text-xl / text-lg, weight 700  (ant-card-head-title: 18px bold)
Body               → text-base, weight 400–500
Caption / Footnote → text-sm, weight 400
Column Headers     → 12px, weight bold (small-caps style)
Small label        → 11–12px, weight 700
```

### ✅ Rules
- Always use **Inter** as the primary font. Roboto is reserved for data tables only.
- All `@import` for fonts must be in component-level CSS or the global stylesheet.
- Use `transition: all 0.5s ease` on `.ant-typography` for smooth animate.
- Never mix font families within the same card or form component.

---

## 4. Spacing & Layout

### Base Unit
The base spacing unit is **4px**. Use multiples of 4 for all spacing values.

### Common Spacing Tokens
| Token | Value | Usage |
|-------|-------|-------|
| `space-xs` | 4px | Tight gaps between inline elements |
| `space-sm` | 8px | Input padding, icon margins |
| `space-md` | 16px | Card internal padding |
| `space-lg` | 24px | Section gaps, column margins |
| `space-xl` | 40px | Card inner gap (plan cards) |
| `space-2xl` | 50px | Bottom margin on major cards |

### Layout Containers
```css
/* Standard content width */
.margin-layout-container { margin: 0 2vw; }

/* At ≥1200px */
.margin-layout-container { margin: 0 4vw; }

/* At ≥1600px */
.margin-layout-container { margin: 0 15vw; }

/* Premium (dashboard-style) */
.premium-layout-container { margin: 0 2vw; }
```

### Breakpoints
| Name | Value | Behavior |
|------|-------|----------|
| `xs` | ≤480px | Mobile small |
| `sm` | ≤580px | Sidebar hidden, hamburger shown |
| `md` | ≤768px | Footer no margin, fonts scale |
| `lg` | ≤1024px | Font scale begins |
| `xl` | ≥1200px | Container expands |
| `2xl` | ≥1600px | Max container width |

---

## 5. Components

### 5.1 Cards

**Standard Card Pattern** (Ant Design `<Card>`)
```css
.card-plan {
  border-radius: 10px; /* Always 8–12px for cards */
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
  border: 2px solid rgba(115, 152, 34, 0.5); /* brand-border */
  padding: 20px;
  transition: box-shadow 0.5s ease, transform 0.5s ease;
}

.card-plan:hover {
  box-shadow: 0px 4px 4px rgba(115, 152, 34, 0.5);
  transform: scale(1.02);
  border: 2px solid #739820; /* brand-primary */
}
```

**Card Header** (`ant-card-head-title`):
- Font size: 18px
- Font weight: bold
- Margin top: 14px
- Text align: left

**Feature/Benefit Card Hover:**
- Scale: `1.05` (more prominent than standard)
- Background: `#F1F4E8` (brand-muted)

**Highlight Badge (Popular, etc.):**
```css
.card-plan-popular {
  background-color: #739820;
  color: white;
  border-radius: 10px;
  padding: 10px;
}
```

### 5.2 Buttons

**Primary Button:**
- Background: `#739D23`
- Color: `#FFFFFF`
- Font weight: 600
- Hover: `#8DBA20`
- Full-width in forms: `width: 100%`

**Link / Text Button:**
- Color: `#739D23`
- Hover: `#8DBA20`

**Payment Button (MercadoPago):**
- Background: `#739d23`
- Font size: 15px
- Font weight: 600

### 5.3 Form & Input

- Border: 1px solid `#ccc`
- Border radius: 5px
- Padding: 8px
- Width: 100% (inputs within forms)
- Form item margin: `0 0 10px`

**Checkbox (Ant Design override):**
```css
.ant-checkbox-inner { border-color: #739d23; }
.ant-checkbox-checked .ant-checkbox-inner { 
  background: #739d23; 
  border-color: #739d23; 
}
```

**Select Options:**
- Font size: 14px (scales down responsively, see text-sm)
- Align self: center

### 5.4 Tables

**Table Headers:**
```css
.ant-table-thead .ant-table-cell {
  background-color: #739D23; /* brand-primary */
  color: #FFFFFF;
  font-family: 'Roboto', sans-serif;
  font-weight: 300;
}
```

**Table Borders:**
- Subtle: `1px solid #868686`
- White space: `normal`

### 5.5 Navigation / Sidebar

- Sidebar trigger height: 80px
- Box shadow: `0 20px 25px -5px rgba(0,0,0,0.1), 0 8px 10px -6px rgba(0,0,0,0.1)`
- At ≤580px: sidebar hidden, hamburger menu shown

**Logo Container:**
- Height: max 65px
- Direction: row, space-between
- Transition: `all 0.5s ease`

### 5.6 Carousels

- Inactive dots: `#CBDF9B` (brand-light), 12px circle
- Active dot: `#739D23` (brand-primary), 12px circle, border
- Dots position: `bottom: -75px`

### 5.7 Dividers (Brand Divider)

```css
.divider {
  height: 2px;
  background-color: #739d23;
  margin-top: 10px;
}
```

### 5.8 Price Blocks / Badges

```css
.price-block {
  background-color: #254000; /* brand-dark */
  color: #fff;
  padding: 5px 20px;
  border-radius: 50px; /* pill shape */
  font-size: 12px;
  font-weight: bold;
}
```

---

## 6. Effects & Motion

### Shadow Scale
| Level | Value | Usage |
|-------|-------|-------|
| `shadow-sm` | `0px 4px 4px rgba(0,0,0,0.25)` | Cards, buttons, badges |
| `shadow-brand` | `0px 4px 4px rgba(115,152,34,0.5)` | Card hover state |
| `shadow-nav` | `0 20px 25px -5px rgba(0,0,0,0.1), 0 8px 10px -6px rgba(0,0,0,0.1)` | Navigation elements |
| `shadow-overlay` | `rgba(0,0,0,0.7)` | Tooltips, overlays |

### Border Radius Scale
| Token | Value | Usage |
|-------|-------|-------|
| `radius-sm` | 5px | Inputs, form elements |
| `radius-md` | 8px | General cards |
| `radius-lg` | 10px | Plan cards, popups |
| `radius-xl` | 12px | Filter cards, promo cards |
| `radius-pill` | 50px | Badge/pill elements |

### Transitions
All transitions use `ease` timing function.

| Token | Value | Usage |
|-------|-------|-------|
| `transition-fast` | `all 0.1s ease` | Tooltip |
| `transition-base` | `all 0.2s ease-out` | Accordion |
| `transition-smooth` | `all 0.5s ease` | Cards hover, typography, logo |

### Animations
```css
/* Spinning logo background — Login page decoration */
@keyframes spin {
  0%   { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
.background-logo { animation: spin 60s infinite linear; }

/* Accordion expand/collapse (Tailwind custom) */
"accordion-down": "accordion-down 0.2s ease-out"
"accordion-up": "accordion-up 0.2s ease-out"

/* Bounce (slow) */
"bounce-slow": "bounce 2s infinite"
```

---

## 7. Visual Hierarchy Rules

When laying out any screen, follow this priority order:

```
1. PRIMARY ACTION    → High contrast (#739D23), bold font (700+), full-width or prominent position
2. SECONDARY INFO    → Medium contrast (neutral dark), medium weight (500–600)
3. DATA / METRICS    → Roboto font, table format, left-aligned headers
4. SUPPORTING TEXT   → text-sm, weight 400, muted color (#868686)
5. DECORATIVE / BG  → brand-muted (#F1F4E8), brand-light (#CBDF9B), low opacity
```

### Elevation Hierarchy
Elements closer to the user (more interactive) get higher elevation (more shadow and scale):

```
Level 3 (Top)    → Modals, tooltips, badges → shadow-nav + z-index high
Level 2 (Mid)    → Cards on hover → shadow-brand + scale(1.02-1.05)
Level 1 (Base)   → Static cards → shadow-sm
Level 0 (Ground) → Page background, layout containers → no shadow
```

### Content Density
- **Desktop**: Use 2–4 column grid layouts
- **Tablet (≤768px)**: Collapse to 1–2 columns, carousel hidden
- **Mobile (≤580px)**: Single column, sidebar hidden
- Always maintain minimum touch target of 40px for interactive elements

---

## 8. Tech Stack Reference

When implementing components aligned with this guide:

| Layer | Technology |
|-------|-----------|
| Framework | React (functional components with hooks) |
| Component Library | Ant Design (antd) — override with CSS specificity |
| Utility CSS | Tailwind CSS v3 (preflight disabled — antd handles base) |
| Custom CSS | Vanilla CSS modules per component |
| Fonts | Google Fonts (Inter, Roboto) |
| Charts | Chart.js, G2/AntV |
| Animations | CSS keyframes + Tailwind `animation` tokens |

**Ant Design Override Pattern:**
Always override Ant Design default colors via class-level CSS, not inline styles:
```css
/* ✅ Correct */
.ant-checkbox-checked .ant-checkbox-inner { background: #739d23; }

/* ❌ Avoid */
<Checkbox style={{ backgroundColor: '#739d23' }} />
```

---

## 9. Do's and Don'ts

### ✅ Do
- Use `#739D23` as the single consistent primary action color
- Apply `transition: all 0.5s ease` on interactive cards
- Use `border-radius: 10px` for plan/feature cards
- Always include hover states with `shadow-brand` + scale transform
- Use the responsive font scale from `ResponsiveFonts.css`
- Follow the visual hierarchy levels (elevation model)
- Use `brand-dark` (#254000) for badge pill backgrounds only

### ❌ Don't
- Use raw Ant Design blue (default primary) — always override to brand-primary
- Mix font weights arbitrarily — follow the weight table
- Apply `scale(1.05)` to non-interactive elements
- Use opacity or blur on primary action buttons
- Skip responsive behaviors — always define `@media` rules for ≤768px and ≤580px
- Use hard-coded pixel sizes when a responsive Tailwind class exists

---

## 10. Skill Usage Instructions

When this skill is active, for **any UI task**:

1. **New Component** → Reference Section 5 for the component type, apply colors from Section 2, typography from Section 3, effects from Section 6
2. **Color Decision** → Always pick from the palette in Section 2. Never introduce new colors without a clear semantic reason.
3. **Design Review** → Check against the Do's and Don'ts (Section 9) and the visual hierarchy (Section 7)
4. **Design System Creation** → Use the tokens in Sections 2–6 as CSS custom property definitions (`--brand-primary: #739D23;` etc.)
5. **Spacing/Layout** → Use Section 4 breakpoints and container classes

When generating CSS, always output:
- CSS custom properties for all color tokens
- Responsive variants using the breakpoints in Section 4
- Transition declarations matching Section 6
