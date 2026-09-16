# Fundraising measurement plan

## Purpose

This plan defines the minimum data needed to connect communications, donor action, and institutional funding while protecting donor and beneficiary privacy.

## Individual donor journey

### Events to track

- Mission page viewed
- Beneficiary story viewed with consent controls
- Video completed
- Email subscription completed
- Donation page viewed
- Donation started
- Donation completed
- Thank-you message delivered
- Impact update opened
- Repeat donation completed

### Required dimensions

- Anonymous visitor or consented supporter identifier
- Acquisition channel
- Campaign name
- Content theme
- Device category
- Country or broad region
- New or returning supporter status
- Event timestamp

Do not collect beneficiary medical details or unnecessary donor attributes for marketing analysis.

## Institutional funding journey

Track each funder separately through research, eligibility, contact, proposal, review, decision, award, and reporting. Store application deadlines, requested documents, responsible owner, and next action.

## Core calculations

```text
Donation completion rate = completed donations / donation starts
Visitor-to-donor rate = completed donations / awareness visitors
Repeat-donor rate = donors with a later gift / all donors
Proposal success rate = funded proposals / decided proposals
Funding cycle time = award date - prospect qualification date
```

## Reporting rhythm

- Weekly: website and donation-path performance
- Monthly: donor acquisition, repeat giving, and campaign comparison
- Quarterly: institutional pipeline, proposal outcomes, and funding concentration
- Annually: impact, retention, income mix, and data-quality review

## Privacy controls

- Collect only fields required for fundraising operations.
- Separate beneficiary information from donor analytics.
- Define access roles for donor and financial records.
- Record consent and lawful-use status.
- Set retention periods for inactive records.
- Publish only aggregated results.

## Current limitations

The public project has no raw web analytics, donation exports, donor records, grant amount, or verified conversion counts. The included funnel is an educational example and should not be used as an organizational performance report.
