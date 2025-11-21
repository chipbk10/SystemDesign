## ✅ AWS KMS (Key Management Service)

- **What it is**: A managed service to create, store, and manage encryption keys.
- **Purpose**: Encrypt data at rest or in transit using AWS-managed or customer-managed keys.
- **Use cases**:
  - Encrypt S3 objects, EBS volumes, RDS databases.
  - Generate data keys for application-level encryption.
- **Key point**: You don’t handle raw keys; AWS KMS does secure storage and rotation.

## ✅ AWS Secrets Manager

- **What it is**: A service to securely store, rotate, and retrieve secrets (like DB passwords, API keys).
- **Purpose**: Avoid hardcoding secrets in code or config files.
- **Features**:
  - Automatic rotation of secrets.
  - Integration with RDS, Lambda, etc.
- **Key point**: Secrets are encrypted using KMS keys under the hood.

## ✅ Relationship:
- Secrets Manager uses KMS to encrypt secrets before storing them.
