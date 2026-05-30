**Example: Chaos Engineering**

**Objective**:  
Proactively find weaknesses in the system by intentionally breaking things in a controlled way — before real customers experience the failure.

**Simple Real-World Scenario**:

Instead of waiting for a real outage, the SRE team does the following:

- Once a month, they randomly shut down 1 database replica in production (during low traffic hours).
- Or they inject artificial network latency between services.
- Or they kill random pods in Kubernetes.
- They observe how the system reacts: Does it auto-recover? Do alerts fire? Does the user experience stay acceptable?

**What SRE does**:
- Designs safe chaos experiments.
- Uses tools like **Chaos Monkey**, **Litmus Chaos**, or **Gremlin**.
- Runs experiments on non-critical services first, then gradually on more important ones.
- Documents findings and works with teams to fix discovered weaknesses (e.g., missing retries, weak failover, single points of failure).

**Key SRE Responsibility**:
Turning “unknown weaknesses” into “known weaknesses” and fixing them before they cause real incidents.

**Famous Principle**:  
“The best way to avoid failure is to fail constantly — but on your own terms.”

---

This is one of the more advanced and interesting SRE practices.

Would you like a clean **documentation summary** for this example, or shall we go to the **next example**?  

Reply with **“summary”** or **“next”**.
