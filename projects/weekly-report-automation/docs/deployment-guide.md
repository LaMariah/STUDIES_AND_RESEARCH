# Deployment guide

## Public portfolio mode

Use the included synthetic CSV and local command. No credentials are required.

```bash
python src/build_weekly_report.py \
  --input data/sample_weekly_log.csv \
  --reference-date 2026-09-11 \
  --output output/weekly_report.md
```

Run tests with:

```bash
python -m unittest discover -s tests -v
```

## Production architecture

The private production version should use:

1. A timezone-aware weekly scheduler
2. A read-only integration with the private activity database
3. Secret storage for database and notification credentials
4. A report-generation step with validation and duplicate checks
5. Draft delivery to the workflow owner only
6. Manual approval before external delivery
7. Run logging and failure alerts

## Required secrets

Do not commit these values:

- Database integration token
- Private data-source identifier
- Notification service credentials
- Sender and recipient identifiers

Use the selected automation platform's encrypted secret store.

## Release checklist

- [ ] Test account or staging data used
- [ ] Required fields validated
- [ ] Duplicate test passed
- [ ] Missing-data test passed
- [ ] Empty-week test passed
- [ ] Authentication-failure test passed
- [ ] Draft reaches the workflow owner only
- [ ] Human approval confirmed
- [ ] Manual fallback tested
- [ ] Workflow owner accepts the recovery procedure

## Scheduling note

Use a timezone-aware scheduler. A fixed UTC cron time may shift relative to local time when daylight-saving rules change.
