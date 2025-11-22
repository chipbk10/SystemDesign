### ✅ **AWS Batch**

AWS Batch is a **fully managed service for running batch computing jobs** at any scale. It automatically provisions compute resources (EC2 or Fargate) and schedules jobs based on your requirements.

***

### ❌ **Is AWS Batch serverless?**

No, AWS Batch is **not truly serverless** like AWS Lambda.

*   It **feels serverless** because you don’t manage servers directly, but under the hood, AWS Batch uses **EC2 instances or Fargate tasks**.
*   You pay for the compute resources while jobs run.

***

### ✅ **Is AWS Batch a Lambda?**

No.

*   **Lambda** = short-lived, event-driven functions (max 15 min).
*   **Batch** = long-running, resource-heavy jobs (hours or days).

***

### ✅ **Use Cases**

*   **High-performance computing (HPC)**: Scientific simulations, genomics.
*   **Data processing**: ETL jobs, image/video rendering.
*   **Machine learning**: Training models on large datasets.
*   **Financial risk modeling** or **engineering simulations**.

***
