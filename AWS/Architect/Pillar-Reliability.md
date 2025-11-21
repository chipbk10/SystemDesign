### ✅ Reliability Pillar (AWS Well-Architected Framework)

The **Reliability pillar** ensures that your workload can **perform its intended function correctly and consistently**, even when failures occur. It focuses on:

*   **Foundations** – Proper setup of networking, IAM, and quotas.
*   **Workload Architecture** – Design for fault tolerance and redundancy.
*   **Change Management** – Monitor and manage changes to reduce risk.
*   **Recovery Planning** – Implement backup, restore, and disaster recovery strategies.

Goal: **Keep systems available and recover quickly from disruptions.**

***

### ✅ AWS Services for Reliability

1.  **Amazon Route 53**
    *   DNS service for routing traffic and implementing health checks.

2.  **Elastic Load Balancing (ELB)**
    *   Distributes traffic across multiple instances for fault tolerance.

3.  **Amazon EC2 Auto Scaling**
    *   Automatically adds/removes instances to maintain availability.

4.  **Amazon S3**
    *   Highly durable storage for backups and static content.

5.  **Amazon RDS with Multi-AZ**
    *   Provides automatic failover for databases.

6.  **Amazon CloudWatch**
    *   Monitors system health and triggers alarms for recovery actions.

7.  **AWS Backup**
    *   Centralized backup for AWS resources.

8.  **AWS Elastic Disaster Recovery (AWS DRS)**
    *   Enables fast recovery of applications in case of outages.
