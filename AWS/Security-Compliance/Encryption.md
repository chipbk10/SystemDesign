## ✅ Encryption at Rest
- **What it means**: Data is encrypted when stored on disk (e.g., in S3, EBS, RDS).
- **Purpose**: Protects data if storage media is compromised.
- **AWS services**: S3, EBS, RDS, DynamoDB all support encryption at rest using AWS **KMS** keys.

## ✅ Encryption in Transit
- **What it means**: Data is encrypted while moving between systems (e.g., client → AWS service).
- **Purpose**: Protects data from interception during transfer.
- **AWS services**: Use **TLS/HTTPS** for API calls, SSL for database connections.
