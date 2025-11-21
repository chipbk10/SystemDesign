## ✅ AWS CloudWatch
- **What it is**: A monitoring and observability service for AWS resources and applications.
- **Purpose**: Collects metrics, logs, and events so you can:
  - Monitor resource performance (CPU, memory, network).
  - Set alarms to trigger actions (e.g., send notifications, auto-scale).
  - Visualize data in dashboards.
- **Key point**: Helps you detect issues and automate responses.

## ✅ Types of Automated Responses

### Scaling Resources
- If CPU usage on an EC2 instance exceeds a threshold, CloudWatch can trigger an Auto Scaling policy to add more instances.
- So the flow looks like this:
  - **CloudWatch Alarm** detects high CPU usage.
  - **Alarm** triggers **Auto Scaling** policy → adds more EC2 instances.
  - **Load Balancer** automatically includes new instances in its target group and starts routing traffic to them.

### Restarting or Stopping Instances
- If an instance becomes unhealthy, CloudWatch can invoke an AWS Systems Manager Automation document or an AWS Lambda function to restart or stop it.
  
### Sending Notifications
CloudWatch alarms can send alerts via Amazon SNS (email, SMS, or push notifications) when thresholds are breached.

### Triggering Lambda Functions
- For example, if disk space is low, CloudWatch can trigger a Lambda function to clean up logs or move data to S3.
- Executing Remediation Scripts
  -Automatically run scripts through AWS Systems Manager to fix issues like applying patches or updating configurations.

### Custom Workflows
- Integrate with EventBridge to route events to other AWS services or external systems for complex automation.
