## 3. 💸 Scenario: The Resource Drain (Testing Frugality vs. Ownership)

You discover an unused test environment in the cloud, provisioned by a former team member, that is currently costing the company $3,000 per month. The resources have been idle for six months. You are unsure if anyone needs it for future testing, and contacting the former team member is difficult.

**Question:** Rank the following actions from most effective to least effective:

* **A.** Immediately delete the test environment resources to stop the $3,000 monthly bleed, aligning with **Frugality**.
* **B.** Send an email to the last known team alias asking if the resource is needed, and if you receive no response in one week, delete it.
* **C.** Spend time tracing the resource's permissions and usage logs to determine its last activity and who created it before making a deletion decision.
* **D.** Mark the resource for deletion, but only ask your manager for final approval before deleting it.

| Rank | Choice | Primary LP Alignment | Rationale |
| :--- | :--- | :--- | :--- |
| **1** | **C** | **Dive Deep; Frugality** | The best choice. Before taking the drastic action of deletion, you use **Dive Deep** skills to gather the necessary data to make an informed decision. This ensures you uphold **Frugality** without accidentally destroying a potentially critical resource. |
| **2** | **B** | **Bias for Action; Frugality** | A good practical choice. It satisfies **Frugality** by setting a deadline for cost reduction and uses **Bias for Action** to move quickly. It assumes a lack of response is permission to delete, which is usually safer than immediate deletion. |
| **3** | **A** | **Frugality** | Violates **Dive Deep** and **Ownership**. While highly **Frugal**, immediately deleting a resource that might be critical to another service (even if it appears idle) shows a lack of **Ownership** and investigation. |
| **4** | **D** | **Ownership** | Violates **Ownership** by delegating the decision to the manager. As the engineer who discovered the waste, you should present a solution based on facts, not just ask for permission to act on an unknown. |
