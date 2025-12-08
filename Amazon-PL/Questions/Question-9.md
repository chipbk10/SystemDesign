## 1. 📢 Scenario: The Customer-Facing Incident (Testing Ownership vs. Earn Trust)

A critical service you own fails unexpectedly, causing a small number of customer orders to be delayed. You suspect the root cause is a dependency service managed by another team, but you are not 100% certain. Stakeholders are demanding an immediate explanation for the delay.

**Question:** Rank the following actions from most effective to least effective:

* **A.** Immediately tell stakeholders that the **external dependency is the cause** and that the other team is working on a fix, diverting blame to manage expectations.
* **B.** State that the issue is currently under investigation, but **send the other team a quick message** asking them to confirm their service status before sending a public update.
* **C.** Immediately inform stakeholders that the service **you own** is currently experiencing an outage and provide a time window for the next update, without mentioning the dependency.
* **D.** Spend 30 minutes **Diving Deep** to confirm the root cause is indeed the dependency before communicating anything to stakeholders.

| Rank | Choice | Primary LP Alignment | Rationale |
| :--- | :--- | :--- | :--- |
| **1** | **C** | **Ownership; Earn Trust** | This is the highest standard. Even if a dependency is at fault, you **own** the customer experience. You communicate quickly, **take ownership** of the failure (it's *your* service that is down for the customer), and manage expectations, which builds **Earn Trust**. |
| **2** | **B** | **Bias for Action; Earn Trust** | This is a strong second. It satisfies **Bias for Action** by communicating quickly and attempts to verify the facts, but it still delays a formal update and relies on the speed of the other team. |
| **3** | **D** | **Dive Deep** | Violates **Bias for Action**. When a critical incident is customer-facing, communication takes precedence over detailed analysis. Time spent proving the root cause is time lost informing customers. |
| **4** | **A** | **Ownership; Earn Trust** | Highly violates **Ownership** and **Earn Trust**. Blaming another team (even if they are the cause) without official confirmation is unprofessional and damages inter-team trust. |
