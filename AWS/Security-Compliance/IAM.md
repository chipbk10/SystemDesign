## ✅ What is AWS IAM?
- **AWS Identity and Access Management (IAM)** is a global service that lets you manage access to AWS resources securely.

### IAM User:
- Represents a person or application inside your AWS account.
- Has long-term credentials (password or access keys).
- Used for admins, developers, or automation scripts.

### IAM Role:
- A permission set that can be assumed temporarily by AWS services or external identities.
- Provides temporary credentials via AWS STS.
- Used for EC2, Lambda, or end-users (e.g., via Cognito).

### Policies:
- JSON documents that define what actions are allowed or denied.

### Scope: 
- IAM is global, not region-specific.

### Billing
- IAM is a free service
