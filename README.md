# Ghana-Online-Betting.com

Static, mobile-first affiliate site covering licensed betting and casino operators in Ghana.
No build step, no framework, no JavaScript — plain HTML with inline styles, served as-is.

## Pages

| URL | File | Title |
| --- | --- | --- |
| `/` | `index.html` | Best Betting Sites in Ghana |
| `/casino` | `casino.html` | Online casinos |
| `/aviator-crash-games` | `aviator-crash-games.html` | Aviator & crash games |
| `/betting-apps` | `betting-apps.html` | Betting apps: download & install |
| `/about-us` | `about-us.html` | About us |
| — | `404.html` | Not found (`noindex`) |

`assets/` holds every image, logo, favicon and icon referenced by the pages. Nothing in it is unused.

## URLs and hosting

Pages are linked and canonicalised **without the `.html` extension** (`/casino`, not `/casino.html`),
and every internal link is root-absolute so it resolves the same from any URL depth.

Most static hosts serve this with no configuration:

- **GitHub Pages**, **Netlify**, **Cloudflare Pages** — resolve `/casino` → `casino.html` and pick up
  `404.html` automatically. Deploy the repository root; there is no publish subdirectory.
- **Vercel** — needs the `cleanUrls` flag, which is set in `vercel.json`.

Anywhere else, map `/<slug>` → `<slug>.html` and point the 404 handler at `404.html`. If clean URLs
can't be arranged, change the `<link rel="canonical">` and `og:url` tags in each page's `<head>`, the
`<loc>` entries in `sitemap.xml`, and the internal `href`s to use `.html` — those three must always agree.

`sitemap.xml`, `robots.txt` and `site.webmanifest` all use the production domain
`https://ghana-online-betting.com` and root-absolute paths. Update them together if the domain changes.

## Local preview

Clean URLs need a server; opening the files directly over `file://` will break navigation.

```sh
python3 serve.py          # http://localhost:8000
```

`serve.py` mirrors production: it resolves `/casino` to `casino.html` and serves `404.html` for
anything missing. Plain `python3 -m http.server` will not — it 404s on every extension-less URL.

## Conventions

Worth knowing before editing:

- **Styling is inline.** There is no stylesheet. Fonts (Inter, Space Grotesk) load from Google Fonts,
  preconnected, `display=swap`, and only the weights actually used are requested.
- **Palette** — Ghana flag colours plus a violet accent: red `#CE1126`, gold `#FCD116`,
  green `#006B3F`, dark green `#04331F`, violet `#6D28D9`, cream `#FDFBF3` / `#FAF5E9`, black `#0A0A0A`.
- **Mobile-first.** Body copy is 16px and never smaller; only tracked-out uppercase micro-labels drop
  to 13px. Tap targets are 44px or larger. The sticky header carries the brand strip and a "top"
  button only — the nav pills sit below it and scroll away.
- **Tables reflow, they don't scroll.** Below 560px every table stacks into labelled blocks. Each
  `<td>` carries a `data-label` matching its column header; keep those in sync when editing a table.
- **Images** carry intrinsic `width`/`height`, `loading="lazy"` and `decoding="async"` below the fold.
  Above-fold images stay eager.
- **FAQ accordions** are native `<details>` / `<summary>`; the `+`/`−` glyph is CSS-only.
- **Structured data** — `Organization` on all pages, `WebSite` on home and about, `FAQPage` on the
  four content pages, `Person` for both authors. Edit the JSON-LD in the `<head>` alongside the copy
  it describes.
- **Outbound reference links** are `rel="nofollow"`. Keep new ones that way.

## Known gaps

- Affiliate cards' "Claim Bonus" / "Get App" CTAs currently point at `/` — they need real tracking links.
- The About Us copy invites readers to "send us a message using the form below"; there is no contact
  form yet, so either the form or that sentence needs to land.
- No affiliate/commercial disclosure statement, which an affiliate site should carry.
- `Organization` schema has no `sameAs` (social profiles) or contact point.
