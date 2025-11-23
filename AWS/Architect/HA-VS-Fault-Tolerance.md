They’re related but **not the same**:

### ✅ **High Availability (HA)**

*   **Goal**: Minimize downtime by designing systems that stay available even if some components fail.
*   **How**: Redundant resources, multi-AZ deployments, load balancers.
*   **Example**: If one EC2 instance fails, traffic is routed to another healthy instance.

### ✅ **Fault Tolerance**

*   **Goal**: Continue operating **without interruption** even when components fail.
*   **How**: Built-in mechanisms for automatic failover and recovery.
*   **Example**: A database cluster where if the primary node fails, a standby node takes over instantly without service disruption.

***

**Key Difference**:

*   **HA** focuses on **availability** (reduce downtime).
*   **Fault Tolerance** focuses on **continuous operation** (no downtime at all).

Think of it like this:

*   HA = “If something breaks, we recover quickly.”
*   Fault Tolerance = “If something breaks, users don’t even notice.”
