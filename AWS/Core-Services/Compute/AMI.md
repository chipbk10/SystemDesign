### ✅ **Amazon Machine Image - AMI**

*   A **machine image** that contains:
    *   Operating system
    *   Pre-installed software
    *   Configurations
*   Used to **launch EC2 instances** with that exact setup.
*   Think of it as a **snapshot of a server**.

***

### ✅ **CloudFormation Template**

*   A **JSON or YAML file** that defines AWS resources and their configuration.
*   Used to **provision infrastructure as code** (e.g., EC2 instances, VPCs, S3 buckets).
*   You can reference an **AMI ID** inside a CloudFormation template when creating EC2 instances.

***

✅ **The AMI must exist in the same AWS region where you are launching the EC2 instance.**

*   AMIs are region-bound because they are stored in region-specific S3 buckets.
*   If your AMI is in **us-east-1**, you cannot directly use it in **eu-west-1**.
*   To use it in another region, you must **copy the AMI** to that region first.

***

**Why this matters:**  
When you specify `ImageId` during instance launch, AWS looks for that AMI **within the selected region**. If it’s not there, the launch will fail.
