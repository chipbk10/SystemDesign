**Example: On-Call and Incident Response**

**Objective**:  
Be the first line of defense when something breaks in production and restore service quickly.

**Simple Real-World Scenario**:

A critical payment service suddenly starts failing for users (error rate jumps from 0.01% to 5%).

**What SRE does**:

- SRE is **on-call** (usually in a weekly rotation).
- When the alert fires at 2 AM, SRE gets paged on their phone (PagerDuty).
- SRE follows a pre-written **runbook** (step-by-step guide) to:
  1. Check dashboards and logs to understand the issue.
  2. Decide whether to rollback the latest deployment.
  3. Restart services, scale up pods, or failover to another region.
  4. Communicate with the team and stakeholders during the incident.
- After the issue is fixed, SRE writes a **postmortem** (blameless report) to document what happened, why it happened, and how to prevent it in the future.

**Key SRE Responsibilities in this example**:
- Creating and maintaining good alerts (not too noisy).
- Writing clear runbooks for common failures.
- Being on-call and handling incidents.
- Driving improvement after incidents (preventing the same problem from recurring).

---

This is one of the most important and visible parts of SRE work.
