## 2. 🗃️ Scenario: The Data Storage Decision (Testing Frugality vs. Think Big)

You are leading the design for a new logging service. The system must store customer usage data for regulatory compliance. You have two options: 1) Use the existing, inexpensive in-house solution which requires manual management (1 hour per week) or 2) Purchase a new, fully managed, high-performance cloud solution which is 10x more expensive but can scale infinitely and requires zero maintenance.

**Question:** Rank the following actions from most effective to least effective:

* **A.** Choose the expensive, managed cloud solution because it aligns with **Think Big** and future-proofs the system against all growth.
* **B.** Choose the existing in-house solution to uphold **Frugality** and save costs, justifying the 1 hour of manual time as acceptable overhead.
* **C.** Choose the existing in-house solution but allocate time in the next sprint to automate the manual management task to achieve zero cost and zero maintenance.
* **D.** Present both options to your manager with the cost-benefit analysis (cost vs. maintenance time) and recommend the cost-saving option.

| Rank | Choice | Primary LP Alignment | Rationale |
| :--- | :--- | :--- | :--- |
| **1** | **C** | **Frugality; Invent and Simplify; Insist on the Highest Standards** | This is the ideal **Invent and Simplify** answer. It achieves the low-cost goal (**Frugality**) and solves the maintenance problem permanently by building an automated, high-standard solution, making the in-house tool viable for the future (**Think Big**). |
| **2** | **B** | **Frugality** | A purely **Frugal** choice. While cost-conscious, it accepts the recurring hour of manual work, failing to demonstrate a drive to **Invent and Simplify** the process, which is a key part of the SDE role. |
| **3** | **A** | **Think Big** | Violates **Frugality**. While the solution is scalable, you must explore less expensive options first. Spending 10x more to solve a maintenance problem that only costs 1 hour/week is a poor ROI decision. |
| **4** | **D** | **Ownership** | Violates **Ownership**. While asking for input is fine, the action delegates the core decision and solution to the manager rather than proposing a fully-vetted, optimal recommendation (like C). |
