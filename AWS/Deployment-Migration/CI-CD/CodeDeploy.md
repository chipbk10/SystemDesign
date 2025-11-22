### ✅ **What is AWS CodeDeploy?**

AWS CodeDeploy is a **deployment automation service** that helps you **deploy application code to EC2 instances, on-prem servers, or Lambda functions** without manual intervention. It ensures **safe, repeatable, and controlled deployments**.

***

### ✅ **Example Use Case**

Imagine you have a new version of your web app:

*   Instead of SSH-ing into each EC2 instance and updating code manually, you use **CodeDeploy** to:
    *   Pull the new code from **GitHub or S3 or CodeCommit**.
    *   Deploy it to all EC2 instances.
    *   Optionally use **blue/green or rolling deployments** to avoid downtime.

***

**Why use it?**

*   Automates deployments.
*   Reduces human error.
*   Supports rollback if something fails.

