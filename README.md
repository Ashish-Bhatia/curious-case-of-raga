# Curious Case of RaGa

A source-linked Rahul Gandhi fact-check website. Plain HTML, CSS and JavaScript, published with GitHub Pages from the root of main. No dependencies or build step.

## Files
- index.html: complete readable articles, including sources and limitations
- styles.css: responsive dark editorial design
- app.js: navigation, search, topic filtering, chronological ordering and article links
- data/checks.json: structured copy of the 38 published checks

Update both the page and structured data together. Label paraphrases, distinguish interested sources from independent evidence, state verification gaps, and date substantive corrections within each article. Never infer intent from an inaccurate statement.

## Deployment
GitHub Settings → Pages → Deploy from a branch → main → / (root).

## Rebuild
The previous working tree was replaced in October 2026. Git history remains available for recovery. No history rewrite or repository deletion was performed.

## Research update, 18 October 2026
Added vacancy-count and returned-banknote checks. Vacancy comparisons retain date and coverage differences. The currency return calculation is reproducible from linked parliamentary figures and does not establish laundering or policy intent.

Added historical checks on loan write-offs versus waivers and the distinction between insurance and pending ex-gratia benefits in the July 2024 Agniveer dispute. Narrow verdict scope and missing account-level records are explicit.

## Ten-claim batch, 18 October 2026
Added ten distinct checks: manufacturing share; India–Pakistan youth unemployment; OBC secretaries; the 2023 women’s reservation mechanism; Article 15(5); and five contextual video checks concerning apprenticeships, reservations, survey beneficiaries, arithmetic and the Wayanad office attack. Numerical gaps remain labelled unverified. Source-publication dates are distinguished where the event timestamp was not certified.

## Next ten-claim batch, 17 October 2026 (UTC)
Added checks on the election-commissioner selection panel, official-duty protection, youth share of unemployment, the 22-person wealth comparison, Maharashtra voter growth, and five separate contextual image/video claims. Exact wealth and two-period electoral-roll comparisons remain unverified. Legal findings concern the historical 2023 text, not subsequent litigation. Published video comparisons are credited and playback limitations stated. Existing design preserved.

## Historical context and next ten claims, 18 October 2026
All 38 checks now include a structured historical section, historical sources, and a statement of what a before/after comparison does or does not establish. The ten new checks cover UPA farm-debt relief, poverty, LPG, petrol/diesel baseline dates, SECC 2011, MGNREGA, RTI, RTE, food-security entitlements, and land acquisition. A source-link correction is recorded in the Article 15(5) check and the public corrections section. No existing verdict changed.

## Content generation
Edit `data/checks.json`, then run `python scripts/render_checks.py`. Each check requires `history.scope`, `history.before_2014` (paragraphs), `history.comparison`, and `history.sources`. Historical context is not an alternative test for the claim itself. The renderer updates all articles, topic options and counts, and embeds the tracked CSS and JavaScript in the page. Keep page-level copy outside the article container.
