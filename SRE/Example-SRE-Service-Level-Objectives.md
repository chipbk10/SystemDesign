### SRE Example: Defining SLOs (Service Level Objectives)

**Objective**:  
Decide and set clear, measurable reliability targets for a service so everyone knows “how good is good enough”.

**Simple Real-World Scenario**:

- The product team wants the checkout service to be “highly available”.
- SRE works with them and defines:

  - **SLO**: 99.9% of checkout requests must succeed (return success) over a 30-day period.
  - **Latency SLO**: 95% of requests must complete in under 300 milliseconds.
  - **Error Budget**: The team is allowed only 0.1% errors (roughly 43 minutes of bad experience per month).

**What SRE actually does in this example**:
- Helps define realistic and business-aligned SLOs.
- Implements monitoring in Prometheus/Grafana to track these SLOs.
- Creates dashboards showing **error budget consumption**.
- When the error budget is burning too fast, SRE can push back on new features and prioritize reliability work.

**Why this is important**:  
Instead of vague promises (“the system should be fast”), there is now a clear, numbers-based target that both developers and SREs can measure and work towards.
