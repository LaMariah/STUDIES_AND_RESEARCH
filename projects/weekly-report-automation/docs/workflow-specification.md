# Workflow specification

## Name and goal

Weekly Activity Report Automation Prototype

Goal: transform structured activity records into a consistent, review-ready weekly report.

## Owner and users

- Workflow owner and reviewer: authorized internal owner
- Report recipient after approval: approved stakeholder
- Data contributor: authorized project contributor

## Trigger and schedule

- Schedule: recurring weekly run in the organization's approved timezone
- Manual fallback: run the report builder from the command line

## Inputs

System of record: private structured activity log.

Required fields:

- Week
- Week Of
- Work Done
- Hours Spent
- Improvements Made
- Ideas and Opportunities
- Possible Outcomes
- Status

Updates from unsupported channels must be logged manually before the scheduled run.

## Ordered steps

| Step | System | Action | Validation | Failure response | Approval |
| ---: | --- | --- | --- | --- | --- |
| 1 | Activity database | Read weekly log records | Required fields exist | Stop and alert owner | No |
| 2 | Report builder | Filter current reporting window | Dates parse correctly | Flag invalid record | No |
| 3 | Report builder | Check duplicate identifiers | IDs are unique | Stop to prevent double counting | No |
| 4 | Report builder | Calculate hours and group activities | Numeric hours | Flag invalid hours | No |
| 5 | Report builder | Create report draft | Record count reconciles | Save error log | No |
| 6 | Notification system | Send draft to workflow owner | Delivery confirmed | Preserve draft and retry once | No |
| 7 | Workflow owner | Review content and sensitive details | Checklist completed | Correct and regenerate | Yes |
| 8 | Workflow owner | Release approved report | Recipient verified | Use manual fallback | Yes |

## Duplicate prevention

Each activity needs a unique activity identifier. Repeated identifiers stop the run before a report is produced.

## Retry and timeout policy

- Data read: retry once after five minutes
- Report generation: no blind retry after validation errors
- Draft email: retry once after ten minutes
- Repeated failure: notify the workflow owner and preserve the report file

## Audit fields

- Run ID
- Reporting date
- Record count
- Total hours
- Items needing review
- Input activity identifiers
- Generation timestamp in production
- Delivery status in production

## Acceptance criteria

- Required fields validate
- Duplicate activity IDs fail safely
- Reporting window returns the expected records
- Total hours reconcile with input rows
- Needs Review items create a visible warning
- No external email is sent before the draft is created
- Final delivery requires human approval

## Manual fallback

Export the activity log as CSV, run the local Python script, review the Markdown report, and send the approved version manually.

## Limitations

- Unsupported-channel updates require manual entry.
- The public implementation does not connect to the production activity database.
- The public implementation does not send email.
- Measured time savings and error reduction are not yet available.
