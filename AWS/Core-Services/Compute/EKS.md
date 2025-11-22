### ✅ **What is Amazon EKS?**

Amazon **Elastic Kubernetes Service (EKS)** is a **managed Kubernetes service** on AWS. It lets you run **Kubernetes clusters** without managing the control plane yourself.

***

### ✅ **Why EKS if ECS exists?**

*   **ECS** = AWS-native container orchestration (simpler, fully AWS-managed).
*   **EKS** = Kubernetes-based orchestration (open-source standard, multi-cloud portability).
*   If your team already uses **Kubernetes** or wants **vendor-neutral orchestration**, EKS is the choice.
*   Kubernetes offers **advanced features** like custom controllers, CRDs, and a huge ecosystem of tools.

***

### ✅ **Example Use Case**

You have a microservices app and want:

*   **Kubernetes features** (Helm charts, custom operators).
*   Ability to **move workloads between AWS and on-prem** easily.
*   Use **Kubernetes-native tools** like Prometheus, Istio.

Steps:

1.  Create an EKS cluster via AWS console or CLI.
2.  Deploy your app using **kubectl** and Kubernetes manifests.
3.  EKS manages the control plane; you manage worker nodes (or use Fargate for serverless pods).

***

**In short:**

*   Use **ECS** if you want AWS simplicity.
*   Use **EKS** if you need **Kubernetes ecosystem and portability**.
