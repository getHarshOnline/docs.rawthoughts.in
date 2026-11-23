---
title: "RawFish UI contract"
---

<a id="rawfish&#45;ui&#45;contract"></a>

Build cockpit screens from shared tokens and primitives\. Screen files arrange those components; the components own color, type, spacing and state\. Use this contract when changing the prototype UI\. Its rules do not choose the fresh rebuild's design\.

## The six rules {#the-six-rules}

Each rule exists because a screen built without a shared system breaks it in a predictable way\. The numbers are stable: code and gates cite them\.

### 1\. Spacing belongs to a primitive, so text never collides {#1-spacing-belongs-to-a-primitive-so-text-never-collides}

Two pieces of text never sit as adjacent inline nodes\. Every title and caption, or label and value, lives inside a primitive \(`LabelRow`, a `Panel` header\) whose flex or grid `gap` owns the spacing\. If two texts touch, the primitive is missing\. Typical failures: a card title and its caption running together as one line, helper prose injected into the step list, a label column overlapping a message column, a strip clipped at the top of a panel\.

### 2\. State is a variant of a primitive, never a rewrite of its label {#2-state-is-a-variant-of-a-primitive-never-a-rewrite-of-its-label}

A locked or disabled control is dimmed to `--t4` and gives its reason in an adjacent chip or a `title` tooltip\. Nothing writes the state into content: no tab labelled \"UPLOAD DISABLED\", no gate reason printed inside the primary button, no unreachable step drawn struck through\. `text-decoration: line-through` is banned everywhere\. A disabled control without a visible reason is a defect\.

### 3\. One concept has one control, rendered once {#3-one-concept-has-one-control-rendered-once}

A concept is rendered once, by one primitive\. If it is echoed elsewhere, the echo is the same primitive in the same variant\. Showing a source choice as both a console tab and a chip, or readiness as both full\-width rows and chips, breaks this rule\.

### 4\. Colour carries meaning, and there are two chromatic tokens {#4-colour-carries-meaning-and-there-are-two-chromatic-tokens}

`--accent` means the active item or the primary action, and nothing else\. `--danger` means an error or a halt, and nothing else\. Identity and data are shown with weight, opacity and position, never hue, so lanes and cohorts get no colours of their own and the accent is never used for emphasis\. The one exception is `--target`, a yellow flash used only to highlight a linked target and fading in 900 milliseconds\.

### 5\. Type has fixed roles {#5-type-has-fixed-roles}

Noto Sans is for human text: titles, body and buttons\. JetBrains Mono is for machine text only: numbers, counters, identifiers, hashes, phase and status strings, the console and step numbers\. Fonts are set only through the `--f-*` role tokens, and both families are self\-hosted\. A raw `font-size:` or `font:` with a literal pixel value in a screen file fails the build\.

### 6\. The shell owns density {#6-the-shell-owns-density}

The top bar carries the brand, the step spine and one mono context line \(lane, phase, environment\), nothing else\. Helper prose lives in the step's panel body\. Run metrics live in the console's status line\. A pane exists only when it has content: the graph pane mounts only once a graph exists, and the console is a 34 pixel line unless a run is streaming\.

## The order of work {#the-order-of-work}

The steps below are done in this order\. A screen counts as done only when the steps before it hold\.

### Step 1\. The token sheet is the only source of paint {#step-1-the-token-sheet-is-the-only-source-of-paint}

The token block in `frontend/src/styles/rawfish.css` is the single source of truth\. It defines exactly these tokens, and no other colour, shadow, radius, type or spacing tokens exist\. The `--rf-*` namespace is not used anywhere\.

```css
:root {
  /* colour: the only chromatic tokens in the product */
  --accent: #FF5722;
  --danger: #B23A2E;

  /* surfaces and ink */
  --ink: #141410;
  --paper: #ffffff;
  --bg: #f1f1ee;
  --line: rgba(20,20,15,0.14);
  --line-strong: rgba(20,20,15,0.30);

  /* text tiers: hierarchy comes from opacity, not new greys */
  --t1: #141410;
  --t2: rgba(20,20,16,0.60);
  --t3: rgba(20,20,16,0.42);
  --t4: rgba(20,20,16,0.26);

  /* families */
  --sans: 'Noto Sans', system-ui, sans-serif;  /* human text */
  --mono: 'JetBrains Mono', monospace;         /* machine text only */

  /* type roles: the only legal font declarations */
  --f-display: 600 23px/1 var(--sans);       /* step title */
  --f-title:   600 15px/1.2 var(--sans);     /* card or panel title */
  --f-body:    400 13.5px/1.55 var(--sans);
  --f-btn:     600 12px/1 var(--sans);
  --f-label:   600 10px/1 var(--mono);       /* uppercase, letter-spacing 1px */
  --f-value:   600 12px/1 var(--mono);
  --f-num:     600 30px/1 var(--mono);       /* stat numerals */

  /* spacing scale */
  --s1: 4px; --s2: 8px; --s3: 12px; --s4: 16px; --s5: 20px; --s6: 26px;
}
```

The sheet also carries the `--target` flash from rule 4 and a few layout measures used by the shell \(`--console-h`, `--control-h`, `--dock-w`, `--dock-w-wide`\)\.

### Step 2\. Every visual element is one of the primitives {#step-2-every-visual-element-is-one-of-the-primitives}

Each primitive lives in one file under `frontend/src/cockpit/primitives/`, is imported everywhere it is used, and selects its variants through props\. Nothing else may define these styles\. A new visual need extends a primitive; it never adds inline style to a screen\.

| Primitive | Anatomy and props | Rules |
| --- | --- | --- |
| `Panel` | optional header \(title in `--f-label`, plus meta\) and a body | hairline `--line`, radius 0, no shadow; the header owns its padding and gap |
| `Card` | a `Panel` without a header, padding `--s4` | none beyond `Panel` |
| `Chip` | `variant`: default, accent or caution | one padding \(3px 8px\), `--f-label`; caution uses a `--danger` glyph, not a new background |
| `Button` | `role`: primary, default or quiet; optional `reason` | a disabled button requires `reason`, shown beside it \(chip or tooltip\), never inside the label |
| `LabelRow` | label \(`--f-label`, `--t3`\) and value \(`--f-value`\) | the only way to render a caption and value pair; owns the gap |
| `Meter` | label, value, percentage | a 5 to 9 pixel track in `--line`; fill `--t1` for data, `--accent` only for a budget or the primary item |
| `SentimentTrack` | a value from \-1 to \+1 | a position on the track with a centre tick; monochrome |
| `StepHeading` | number \(mono, accent\), title \(`--f-display`\), hint \(mono, no wrap\) | identical on every step |
| `StepSpine` | steps, each with `state`: done, active, reachable, locked or halted | locked is `--t4` with a `title` reason; active is accent with a 2 pixel underline; halted uses `--danger`; never struck through |
| `Console` | a 34 pixel mono status line that expands into a log | expands only while a run streams; the log is a fixed\-width grid of time, tag and message |

### Step 3\. The shell fixes where everything goes {#step-3-the-shell-fixes-where-everything-goes}

The top bar holds the brand, the `StepSpine` and one mono context line\. The active step owns the work surface: its dock is 484 pixels wide, or 720 pixels when the step is dense, and on Scenario it stands alone\. The graph pane \(300 pixels, with a hairline on its left\) mounts only when a graph exists, and never on Scenario\. The `Console` stays collapsed unless a run is streaming\.

The six steps \(`scenario`, `build`, `cohorts`, `preflight`, `simulate`, `findings`\) are each data plus a composition of primitives\. A step file may declare layout only \(grid, flex, gap and width using the `--s*` scale\); it may not declare paint \(colour, background, border, font, shadow or radius\)\.

When a run halts, the spine marks the step as halted, the console shows the error with a hint on how to fix it, and the step offers \"duplicate as draft\" so the operator can edit a copy\. A frozen field says the same thing in its reason\.

### Step 4\. Run the static interface checks {#step-4-run-the-static-interface-checks}

Every gate passes before screen work counts as done\. `process/check_ui_contract.sh` runs them from the repository root as gates U1 to U10: type only from role tokens \(U1\), no raw hex colours \(U2\), no shadows \(U3\), radius 0 everywhere \(U4\), no strikethrough \(U5\), no state words in labels \(U6\), no `--rf-*` tokens \(U7\), no raw colour functions outside the token file \(U8\), no inline paint bindings \(U9\), and screens that declare layout only \(U10, a ratchet toward zero against `process/ui_paint_baseline.txt`\)\. The core of the first six, as plain shell:

```bash
# paint may only come from tokens and primitives
grep -rn "font-size\|font:" frontend/src --include='*.vue' | grep -v "var(--f" | grep -v tokens && exit 1
grep -rnE "#[0-9a-fA-F]{3,8}" frontend/src --include='*.vue' | grep -v tokens && exit 1
grep -rn "box-shadow" frontend/src | grep -v "none" && exit 1
grep -rn "border-radius" frontend/src | grep -vE "border-radius: ?0" && exit 1
# state is never written into content
grep -rn "line-through" frontend/src && exit 1
grep -rniE "disabled\"?>|DISABLED<" frontend/src --include='*.vue'   # review: no state words in labels
```

These static checks enforce the listed source constraints\. They do not establish readable spacing or that each concept appears as one control\. Review the rendered layout too: visual acceptance takes a screenshot of each step at 1280 by 800 and checks six things:

1. The `StepHeading` block is pixel\-identical in size and position on every step\.
2. Every button is one of the three roles, and every chip one of the three variants\.
3. No two text nodes sit side by side without a parent that owns the gap\.
4. At most two chromatic colours are visible on any screen: the accent and, when there is an error, danger\.
5. No disabled control lacks a visible reason beside it\.
6. The console is at most 40 pixels tall unless a run is streaming, and there is no graph pane on Scenario\.

This is the proof\-of\-concept UI manual\. The fresh rebuild's target and this tree's current departures are separated in [the product contract](/rawfish/rebuild-target), and the current codebase is described in [the architecture](/rawfish/architecture)\.
