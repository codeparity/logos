# logos

The leader site for **Codeparity — The Religion of 9 Choices**.
The book is in the works and will live at codeparity.com; this repo is
the doorway, hosted on GitHub Pages at
<https://codeparity.github.io/logos/>.

The symbol: an ancient wheel re-read as a grid. Time runs left to right
(past · now · future), the self runs top to bottom (why · how · feels).
Nine boxes, always running. Two currents cross at the centre: *solve*
rises from the bottom and takes apart; *coagula* enters from the
top-left and binds.

## Files

- `index.html` — one-screen, no-scroll landing. The symbol's nine boxes
  are clickable; the right panel explains each and funnels to the book.
  Deep links work: `#feels-now`, `#book`, `#premise`, …
- `design.html` — style the symbol in your own terminal colorscheme
  (gruvbox, nord, dracula, …), download it as SVG/PNG plus a brochure of
  the whole site in your theme. `?scheme=gruvbox` preselects a theme.
- `logos.svg` — the symbol's source geometry, unstyled.
- `codeparity_pallette.gpl` — the greyscale ramp both pages draw from.
- `design-guide.md` — content and voice notes pulled from the manuscript.

Everything is static, dependency-free HTML/CSS/JS — no build step.
