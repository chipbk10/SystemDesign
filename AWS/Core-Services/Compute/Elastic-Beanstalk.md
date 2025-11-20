## Manual Setup Without Elastic Beanstalk
- Provision EC2 instances
- Choose AMI, install OS, patch it.
- Deploy your application code
- Upload code and dependencies (or build a container image).
- Configure scaling and load balancing
- Install and configure an Elastic Load Balancer.
- Set up storage
- Configure S3 for static assets or backups.
- Manage networking and security
- Set up VPC, security groups, IAM roles.
- Monitor and update
- Install monitoring agents, handle updates manually.

## ✅ With Elastic Beanstalk
- You just upload your application code.
- AWS automatically:
  - Provisions EC2, installs OS and runtime.
  - Sets up load balancer and auto-scaling.
  - Integrates with S3 for storage.
  - Configures monitoring (CloudWatch).
- You still pay for underlying resources, but management is automated.

## What You Still Configure
- EC2 instance type (CPU, RAM, storage).
- OS platform version (Amazon Linux, Windows).
- Scaling policies (min/max instances).
- Environment variables for your app.
- Security settings (IAM roles, security groups).
- S3 bucket settings (encryption, lifecycle policies).
- Custom integrations (e.g., Lambda triggers for S3 events, custom VPC settings).

## Why?
- Elastic Beanstalk is **PaaS**, not fully managed like Lambda. It gives you convenience but still allows customization because:
  - Apps have different performance needs.
  - Compliance/security requirements vary.
  - You might need custom networking or storage configurations.
