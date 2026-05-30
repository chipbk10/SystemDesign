**Example: Canary Deployments / Progressive Rollouts**

**Objective**:  
Safely release new code changes to users without risking a full outage.

**Simple Real-World Scenario**:

The development team wants to release a new version of the payment service.

**What SRE does**:

- SRE sets up a **canary deployment** strategy:
  - First, release the new version to only **1%** of real users (or 1% of servers).
  - Automatically monitor key metrics for 30 minutes to 1 hour (error rate, latency, success rate, etc.).
  - If everything looks good, gradually increase traffic: 5% → 10% → 25% → 50% → 100%.
  - If something goes wrong (SLO violation), automatically roll back to the previous stable version.

**Key SRE Responsibilities**:
- Designing the rollout strategy (percentage, duration, rollback criteria).
- Setting up monitoring and automated rollback.
- Defining “what good looks like” during the canary period.
- Reducing the blast radius of bad deployments.

**Benefit**: Instead of breaking the service for **all users** at once, problems affect only a small percentage — and can be fixed very quickly.
