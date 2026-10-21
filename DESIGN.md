---
name: 김다연 Portfolio
description: A research portfolio set as a statistical figure. Every mark is a measured value, and one ultramarine series stands for her own result.
colors:
  plot-ground: "#F6F7F9"
  plate: "#FFFFFF"
  sunk: "#EEF0F3"
  ink: "#13151A"
  ink-2: "#3A3F49"
  ink-3: "#5F6673"
  hairline: "#DCE0E6"
  grid: "#E9ECF0"
  her-result: "#2B45D4"
  her-result-ink: "#2238B8"
  her-result-halo: "#E9ECFB"
  baseline-gray: "#A0A7B4"
  baseline-faint: "#C9CED6"
  night: "#111318"
  night-line: "#2C303A"
  night-ink: "#E9EBEF"
  night-3: "#A3A9B5"
typography:
  display:
    fontFamily: "Pretendard Variable, Pretendard, -apple-system, Apple SD Gothic Neo, Malgun Gothic, system-ui, sans-serif"
    fontSize: "clamp(2.35rem, 4.3vw, 3.75rem)"
    fontWeight: 760
    lineHeight: 1.08
    letterSpacing: "-0.035em"
    fontFeature: "\"tnum\" 1"
  headline:
    fontFamily: "Pretendard Variable, Pretendard, system-ui, sans-serif"
    fontSize: "clamp(1.55rem, 2.2vw, 1.95rem)"
    fontWeight: 730
    lineHeight: 1.25
    letterSpacing: "-0.025em"
    fontFeature: "\"tnum\" 1"
  title:
    fontFamily: "Pretendard Variable, Pretendard, system-ui, sans-serif"
    fontSize: "clamp(1.3rem, 1.8vw, 1.6rem)"
    fontWeight: 720
    lineHeight: 1.32
    letterSpacing: "-0.025em"
    fontFeature: "\"tnum\" 1"
  body:
    fontFamily: "Pretendard Variable, Pretendard, system-ui, sans-serif"
    fontSize: "16px"
    fontWeight: 400
    lineHeight: 1.7
    letterSpacing: "normal"
    fontFeature: "\"tnum\" 1"
  label:
    fontFamily: "Pretendard Variable, Pretendard, system-ui, sans-serif"
    fontSize: "13.5px"
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: "normal"
    fontFeature: "\"tnum\" 1"
  figure-mono:
    fontFamily: "JetBrains Mono, ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"
    fontSize: "12.5px"
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: "0"
    fontFeature: "normal"
rounded:
  inset: "4px"
  sm: "6px"
  md: "8px"
  mark: "50%"
spacing:
  gutter: "clamp(16px, 4vw, 40px)"
  column-gap: "24px"
  bar: "64px"
  plate-pad: "clamp(20px, 2.4vw, 30px)"
  section: "clamp(80px, 11vw, 136px)"
  max-width: "1240px"
components:
  button-primary:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.plate}"
    rounded: "{rounded.md}"
    padding: "0 20px"
    height: "46px"
  button-primary-hover:
    backgroundColor: "{colors.ink-2}"
  button-line:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "0 20px"
    height: "46px"
  button-line-hover:
    backgroundColor: "{colors.plate}"
  figure-plate:
    backgroundColor: "{colors.plate}"
    rounded: "{rounded.md}"
    padding: "{spacing.plate-pad}"
  nav-link:
    textColor: "{colors.ink-2}"
    rounded: "{rounded.sm}"
    padding: "8px 10px"
  nav-link-hover:
    backgroundColor: "{colors.sunk}"
    textColor: "{colors.ink}"
  filter-tab:
    textColor: "{colors.ink-3}"
    padding: "10px 0 12px"
  filter-tab-active:
    textColor: "{colors.ink}"
  index-row-hover:
    backgroundColor: "{colors.plate}"
    rounded: "{rounded.sm}"
  close-band:
    backgroundColor: "{colors.night}"
    textColor: "{colors.night-ink}"
---

# Design System: 김다연 Portfolio

## Overview

**Creative North Star: "The Figure Plate"**

The page reads like a results section. It is laid out on a cool white plotting ground. Plates hold figures and are bordered by hairlines. Blue-black ink carries the axes, headings and body text. Every chart is drawn from measured numbers: a lollipop or before→after dot plot with gray baselines, a dashed ink line for ground truth, and exactly one ultramarine series for her own method or verified result. Figures carry continuous numbers and captions, and their panels are lettered (a)(b). Projects carry stable addresses P01–P15 that the page cites like cross-references.

Density changes by section. The first viewport is a dense 5/12 claim column next to a 7/12 Fig. 1 plate. Below it, sections switch to a report layout: a sticky 3/12 heading column beside a 9/12 body. Section breaks are deep and marked by full-width hairlines. The one dark block is the contact band at the end. Motion has one job. On first view, a mark travels from its baseline value to its measured value.

**Key Characteristics:**
- Every graphic is a data figure drawn from real numbers. There are no decorative charts and no hero art.
- Ultramarine always means "her method or verified result" and nothing else.
- The surfaces are flat. Depth comes from the step between plate and ground, plus hairlines.
- Figures, tables and projects use numbered addresses (Fig. n, Table n, Pnn), not badges or kickers.
- Pretendard sets everything with tabular figures. JetBrains Mono appears only where a value or an identifier is printed.

## Colors

The palette is a cool neutral plotting system with a single ultramarine signal.

### Primary
- **Her-Result Ultramarine** (her-result): fills the "me" series in a figure. That covers the stem (2px), the 11px marker, the dashed reference line she set, the highlighted bar fill on detail pages, and the legend swatch for "본인 방법 · 결과".
- **Ultramarine Ink** (her-result-ink): the text form of the same meaning. It is used for the value label of the "me" row, the PI role and award cells in tables, and skills she implemented herself (`own`). It is darker than her-result so it passes AA as text.
- **Ultramarine Halo** (her-result-halo): the 3px halo ring around a "me" marker, and the text-selection background.

### Neutral
- **Plotting Ground** (plot-ground): the page background and the top bar. It is also the theme-color.
- **Plate White** (plate): figure plates, image plates, and the hover background of index rows and the line button.
- **Sunk Gray** (sunk): nav-link hover and the placeholder behind the photo.
- **Blue-Black Ink** (ink): headings, primary text, the primary button, ground-truth reference lines, table header rules, focus outlines, and the "fit" dots for selected projects.
- **Ink 2** (ink-2) / **Ink 3** (ink-3): secondary text (labels, figure values) and tertiary text (captions, metadata, axis ticks).
- **Hairline** (hairline): section rules, list and row separators, plate borders, and the line-button stroke.
- **Gridline** (grid): figure track lines, vertical gridlines, and dividers inside a plate.
- **Baseline Gray** (baseline-gray): markers and stems for comparison methods.
- **Faint Baseline** (baseline-faint): hollow and pale bar fills, text-link underlines at rest, `·` separators, the dashed cross-reference box, and the scrollbar thumb.
- **Night** (night) with **Night Line**, **Night Ink** and **Night 3**: used only in the contact close band. They set its background, its rules, its primary text and its secondary text.

### Named Rules
**The Her-Result Rule.** Ultramarine marks her method, her measured result, or a credential she holds (PI, award, a sampler she implemented). It never appears on navigation, buttons, links, headings or decoration. When the accent colors something that is not hers, the figure lies.

**The Baseline-Is-Gray Rule.** A comparison method, prior value or competing model is drawn in baseline gray, or as a hollow gray ring for a "from" value. It is never drawn in a second hue. The system has exactly two series colors.

## Typography

**Display Font:** Pretendard Variable (fallbacks: Pretendard, Apple SD Gothic Neo, Malgun Gothic, system-ui)
**Body Font:** Pretendard Variable, the same family
**Label/Mono Font:** JetBrains Mono 400/500 (fallbacks: ui-monospace, Menlo, Consolas)

**Character:** One neutral Korean grotesque does all the speaking, pulled tight at the large sizes with heavy variable weights (720–760). Mono is reserved for what a plot or bibliography would print in fixed width: tick labels, figure values, figure numbers, P-addresses, DOIs, repo names and grant IDs.

### Hierarchy
- **Display** (760, clamp 2.35–3.75rem, line-height 1.08, −0.035em): the role title in the first viewport. The detail-page h1 uses 760 at clamp 1.9–2.9rem with line-height 1.18.
- **Headline** (730, clamp 1.55–1.95rem, line-height 1.25, −0.025em): section headings in the sticky column, and the contact heading.
- **Title** (720, clamp 1.3–1.6rem, line-height 1.32): route-plate project titles. Paper titles use 680 at 1.125rem.
- **Body** (400, 16px, line-height 1.7; 15.5px under 720px wide): running text. Detail prose uses line-height 1.85 with a 42em measure. Paper abstracts use a 46em measure.
- **Label** (400–650, 12–14.5px): captions, metadata, dt labels, table headers (500, 12.5px). These stay in sentence case with no tracking.
- **Figure mono** (500, 11–13px): ticks (11px), values (12.5px), Fig./Table numbers (12.5px), P-addresses (13px, 15px on detail pages).

### Named Rules
**The Tabular Rule.** The body sets `font-feature-settings: "tnum" 1` so every number in Pretendard aligns in columns. The mono class resets features to normal.

**The Mono-Means-Identifier Rule.** JetBrains Mono appears only on a value, a tick, or an address (Fig. n, Pnn, DOI, repo, RS-grant ID, years in tables). Prose, labels and headings never use it.

## Layout

The layout is a 12-column grid with 24px column gaps inside a 1240px wrap and a fluid gutter (clamp 16–40px). The fixed top bar is 64px tall and gains a hairline bottom border once the page scrolls. In the first viewport, the claim column spans 5 columns and the Fig. 1 plate spans 7. At 1100px or narrower that becomes 6 and 6, and at 900px or narrower the two stack with the figure 48px below. Report sections put a sticky heading in columns 1–3 (top offset bar + 32px) and the body in columns 4–12. At 1100px or narrower the heading becomes static and full width. Section padding is clamp 80–136px, with a full-width hairline on top. A route plate pairs a text column with a figure column at 1.05fr:1fr, and plates are separated by a hairline. The project index is a five-column row grid (address · title · key result · category · period). Under 720px it collapses to named areas. Definition lists use a 200px term column (170px on the timeline). The detail view narrows to a 920px reading column.

## Elevation & Depth

The surfaces are flat. No surface casts a shadow. Depth has two sources: the step from plot-ground to plate (a white plate on a cool ground) and 1px hairline borders. Shadow values appear only as drawing devices inside figures and controls. The ultramarine 3px halo ring marks a "me" marker, an inset 1.5px ring draws a hollow "from" marker, and an inset 1px ring is the line button's stroke. All three are strokes, not elevation.

### Named Rules
**The Plate-Not-Card Rule.** A container is a figure plate: white, a 1px hairline border, 8px radius, no shadow. It exists to hold a figure, image or table. It is never a decorative card for wrapping a link.

## Shapes

Corners are gentle and few. Plates and buttons use 8px. Nav links, hover rows and the profile photo use 6px. An image plate nested inside a panel uses 4px. Figure markers are full circles: 11px for measured values, 10px hollow rings for prior values, 7px ink dots for evidence bullets, and 6px dots for selected projects. Reference lines are 1.25px dashes, or 1.5px for her own reference. The figure stem is 1px gray, or 2px ultramarine for the "me" row. Heavy rules are structural: a 1px ink rule under table headers and on top of the detail info strip, and a 2px ink rule on top of AV question blocks.

## Components

### Buttons
- **Shape:** gently rounded (8px), 46px tall, 0 20px padding, 600 weight at 15.5px. A 17px SVG icon can sit before the label.
- **Primary:** ink fill with white text, used for the résumé download.
- **Line:** transparent, with an inset 1px hairline stroke and ink text, used for email.
- **Hover / Active:** primary moves to ink-2. Line moves to a plate fill with a baseline-gray stroke. Active scales to 0.97. Transitions run 200ms, and the transform uses the house ease.

### Navigation
- The top bar sits on plot-ground. Links are 14.5px ink-2 with 8px 10px padding and a 6px radius, and they hover to a sunk fill with ink text. The CTA "연락하기" is a solid ink pill (8px 14px).
- At 900px or narrower, a 44px toggle with a stroked SVG opens a full-width drop panel. Its items are 16px, divided by gridlines, and the CTA becomes a centered full-width button. The panel fades and translates 8px over 200ms.

### Filter Tabs
- Text-only tabs on a shared hairline baseline: 14.5px ink-3 with a count in 12px. The active tab turns ink at 600 weight, and a 2px ink underline scales in from the left over 250ms.

### Figure Plate (signature)
- A white plate with a hairline border and 8px radius. The header pairs a mono "Fig. n" with a 650 caption title. Lettered panels (a)(b) are separated by a gridline.
- Each row is a grid: label (32% of the width, with a small subtitle), track, then a right-aligned mono value. A track is a 1px grid line holding a gray stem from the baseline (or "from" value) to the marker. The "me" row has a 650-weight label, a 2px ultramarine stem, an ultramarine marker with a halo, and an ultramarine-ink value.
- An overlay draws vertical gridlines at the ticks plus one dashed reference line labeled in mono 11px. The line is ink for ground truth and ultramarine when she set it. Below it sits a mono tick axis. A footer legend lists only the encodings actually present (본인 방법 · 결과, 비교 기준, 이전 값, 정답, 직접 설정한 기준선), followed by "모든 값은 논문 · 실험 실측치".
- **Motion:** the final position is the default, so the figure is correct without JS. A `.pre` state parks markers and stems at the baseline. On intersection (rootMargin −12%), the markers travel to their measured values once, over 900ms on cubic-bezier(.23,1,.32,1), staggered 70ms per row after 120ms. On hover, sibling rows fade to 0.45 opacity. Every figure carries a role="img" aria-label that lists every value.

### Detail Bar
- A label | 8px track | mono value grid. The fill is faint baseline gray, scaled from the left. The highlighted row uses an ultramarine fill, an ink label and an ultramarine-ink value.

### Index Row
- A project row with the mono P-address first. On "fit" projects the address turns ink at 600 weight and gets a 6px ink dot. The row continues with a 620-weight title and a one-line ellipsized meta, then the key result, category and year. Rows are separated by hairlines and hover to a plate fill with a 6px radius.

### Reference Entry
- A 132px status column followed by the title, source, abstract and mono DOI links. A pending entry prints its status as plain ink-3 text, never as a badge.

### Close Band
- The single dark block (night). It holds a headline, a large underlined email (clamp 1.6–2.9rem, 2px night-3 underline at a 10px offset) and link rows separated by night-line rules. Arrow icons nudge 2px on hover.

## Do's and Don'ts

### Do:
- **Do** render every chart from data through the figure engine (lollipop, or before→after dot plot), with real tick values and an aria-label that lists every value.
- **Do** reserve her-result (#2B45D4) and her-result-ink (#2238B8) for her method, her measured result, PI and award cells, and skills she implemented herself.
- **Do** draw ground truth as a 1.25px dashed ink line with a mono label, and draw baselines in baseline gray.
- **Do** number figures and tables continuously (Fig. 1 in the first viewport, Fig. 2 onward on the route plates) and cite projects by their stable Pnn address in mono, inline before the title.
- **Do** keep surfaces flat: a white plate, a 1px hairline (#DCE0E6) and an 8px radius.
- **Do** run the entrance motion once per figure on cubic-bezier(.23,1,.32,1) for 900ms with a 70ms row stagger, and make prefers-reduced-motion collapse all transitions.
- **Do** print statuses ("투고 준비 중", PI, award) as inline text in the table or reference column.

### Don't:
- **Don't** use ultramarine on navigation, buttons, links, headings or ornament.
- **Don't** add a second series hue. Comparisons are gray, and prior values are hollow gray rings.
- **Don't** draw decorative or illustrative charts, gradient hero art or card grids. A figure that does not plot measured numbers does not ship.
- **Don't** put kickers or eyebrow labels above headings. The P-address sits inline before the heading, and the category line sits below it.
- **Don't** use drop shadows for elevation.
- **Don't** set prose, labels or headings in JetBrains Mono.
- **Don't** use a dark section anywhere except the contact close band.
