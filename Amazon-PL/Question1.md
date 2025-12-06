### **Example: The Quick Fix vs. The Clean Code**

**Scenario:** You find a major, customer-facing bug in production. A quick-and-dirty fix exists that will resolve the issue in 30 minutes, but it introduces technical debt (messy, uncommented code) that will cause maintenance issues later. A proper, clean, and robust fix will take 3 hours.

**Question:** Rank the following actions from most effective to least effective:

* **A.** Implement the quick 30-minute fix immediately to get the service running, and then schedule the proper refactoring for next week.
* **B.** Spend the full 3 hours on the clean, robust fix to ensure high code quality, even though the customers will experience 3 more hours of downtime.
* **C.** Ask another team member to review the quick fix before deployment to ensure it doesn't cause a new, separate issue.
* **D.** Deploy the quick fix immediately without review, knowing it's just a temporary measure.

| Choice | Principle Mapping | Rationale |
| :--- | :--- | :--- |
| **B** | **Insist on the Highest Standards**; **Customer Obsession** | The core issue is customer pain. While speed matters (**Bias for Action**), the *proper* solution (B) ensures the issue is fully resolved with quality, preventing future recurrence and minimizing technical debt, aligning with **Insist on the Highest Standards**. **A** is a close second, as it prioritizes speed, but **B** is often the "most correct" answer by Amazon standards if the 3-hour delay is acceptable. |
| **A** | **Bias for Action**; **Deliver Results** | Getting the service working *fast* is crucial. If the quick fix is genuinely a **temporary patch**, deploying it and immediately planning the clean fix (B) is a strong choice. **A** is usually better than **B** if the bug is catastrophic. |
| **C** | **Earn Trust**; **Ownership** | While helpful for quality, it doesn't solve the problem itself and is an intermediary step. Asking for review takes time that could be spent fixing the bug. |
| **D** | **Bias for Action** (misapplied) | This neglects **Insist on the Highest Standards** and **Earn Trust** (by skipping review). Blindly rushing a fix is a common mistake. |
