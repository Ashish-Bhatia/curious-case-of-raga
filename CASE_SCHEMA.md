# Evidence ledger: schema and publication gate

The published website reads **data/cases.json**, an array of case objects. Start with an empty array and add researched records only. Do not copy the schema example into the live file without conducting the review.

## Example structure (illustrative placeholders, not a real case)

\`\`\`json
[
  {
    "id": "RAGA-2026-0001",
    "date": "2026-10-15",
    "headline": "Clearly described, fact-checked claim",
    "claimant": "Rahul Gandhi",
    "claim_text": "Verbatim quotation from a verified public source",
    "claim_url": "https://example.org/original-statement",
    "original_language": "English",
    "topic": "Election process",
    "institution": "Election Commission of India",
    "verdict": "Unresolved",
    "summary": "A concise conclusion with a clear scope and caveats.",
    "analysis": "Explain what the original claim says, the relevant methodology, what the source documents establish, and what they do not establish.",
    "sources": [
      {"title": "Authenticated original record", "url": "https://example.org/primary-record", "type": "primary", "date": "2026-10-15"},
      {"title": "Independent corroborating analysis", "url": "https://example.org/corroboration", "type": "independent", "date": "2026-10-15"}
    ],
    "reviewed_at": "2026-10-15",
    "publication_status": "draft",
    "review_status": "pending",
    "primary_source_verified": false
  }
]
\`\`\`

The example uses example.org placeholders and intentionally FAILS the publication gate.

## Allowed verdicts

False | Misleading | Unsubstantiated | Partly true | Supported | True | Disputed | Unresolved | Opinion / prediction

## Allowed institution values

Election Commission of India | Judiciary | Parliament | Defence and security | Economy and data | Other public claims

## Editorial review

- Preserve the original statement, archive reference, timestamp, original language and translation where applicable.
- Check exact time periods, denominators, measurement definitions and revisions.
- Seek and scrutinise the government/institutional response, relevant court findings and independent evidence.
- Distinguish lack of public proof from proof that an assertion is false.
- Separate factual propositions from rhetoric, satire, predictions and political opinions.
- Do not assert a person knowingly lied without independently persuasive evidence of intent.
- Source the claimant's statement and every important factual rebuttal; use original documents where possible.
- Mark unverified leads as drafts. Approval is a genuine human editorial action, not an automated checkbox.
- Record reasons for corrections, dates, changed verdicts and material new sources in version history or a correction note.
- No invented quotes, cherry-picked context, defamatory insinuations unsupported by evidence, or harassment.
