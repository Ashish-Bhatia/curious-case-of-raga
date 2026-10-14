# The Curious Case of RaGa

> A satirical editorial project with a strict evidence standard. Big claims. Bigger scrutiny. Actual sources.

This public repository contains the static website for **The Curious Case of RaGa**, an investigative archive assessing Rahul Gandhi's public statements and allegations. Satire is permitted as an editorial device. Fact findings are never selected in advance.

## Website deployment

GitHub → this repository → **Settings → Pages → Build and deployment → Deploy from a branch → main / (root) → Save**.

Expected project URL after publication: https://ashish-bhatia.github.io/curious-case-of-raga/

No npm, servers, paid hosting or API keys are required. The site consists of HTML, CSS, JavaScript and a versioned JSON evidence ledger.

## File map

- \`index.html\`: accessible site sections and case detail dialog
- \`styles.css\`: responsive noir editorial design
- \`app.js\`: search, filters, institutional links, timeline, interactive hypothetical quiz, publication gate
- \`data/cases.json\`: canonical case dataset; starts empty, not populated with assumptions
- \`CASE_SCHEMA.md\`: publication rules and a sample record
- \`.nojekyll\`: publish raw static files
- \`README.md\`: project operations

## Editorial standard

A claim is marked False only if authoritative evidence directly refutes it. A demonstrably false claim does **not** by itself prove deliberate deception. Possible outcomes: False, Misleading, Unsubstantiated, Partly true, Supported, True, Disputed, Unresolved, Opinion / prediction.

Every public case must have:
1. An attributable original statement with date and source URL.
2. Exact claim text and relevant context.
3. At least two linked sources, including an authenticated primary record.
4. Reasoning that directly connects each source to the verdict.
5. \`publication_status: "published"\`, \`review_status: "approved"\`, and \`primary_source_verified: true\`.

Cases without these fields do not render. The approving editor must examine the originals, not simply set flags. Review new contradictory evidence and correct the case visibly. The JSON ledger is public and version-controlled.

## How to add a case

Follow \`CASE_SCHEMA.md\` and append a complete object to the JSON array in \`data/cases.json\`. Check JSON syntax before committing. The website reads the dataset on page load. Do not publish guessed quotations, unsupported labels, uncited allegations, or personal information.

## Contributions and corrections

Open a GitHub Issue containing the exact quotation, date, original source and the evidence in dispute. A public issue is a research lead, not a verified finding.

This website is independent political commentary. It is not affiliated with a political party, electoral authority, government institution, or Rahul Gandhi.
