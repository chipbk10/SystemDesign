**Example: Postmortem (Blameless Post-Incident Review)**

**Objective**:  
Learn from production incidents so the same problem does not happen again.

**Simple Real-World Scenario**:

There was a major outage for 45 minutes because a new deployment caused a database timeout. After the service was restored, the SRE organizes a postmortem.

**What SRE does**:

- Schedules a blameless postmortem meeting with all involved teams.
- Collects timeline of events (what happened, when, and why).
- Focuses on **systemic issues**, not blaming individuals (e.g. “Deployment process was risky” instead of “John deployed badly”).
- Identifies root causes (e.g., missing monitoring, no canary, weak testing).
- Creates action items such as:
  - Add a new alert for database connection pool
  - Improve canary duration
  - Update the runbook
- Tracks these action items until they are completed.

**Key SRE Responsibilities in this example**:
- Driving the postmortem process.
- Making sure the culture stays blameless.
- Converting incident learnings into concrete improvements (prevention).
- Sharing the postmortem with wider teams.

This is one of the most important ways SREs continuously improve system reliability.

---
