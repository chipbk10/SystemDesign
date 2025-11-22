# AWS

## Cloud Concept
- [6 Advantages of Cloud Computing](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Cloud-Concept/Advantages-Cloud-Computing.md)
  - pay-as-you-go, economies, easily-scale-out-in, speed, no-infrastructure-maintenance, go-global
- [Global Infrastructure](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Cloud-Concept/Global-Infrastructure.md)
  - Data Center, Availability Zone (AZ), Region, Edge Location (CDN)
- [Share Responsibility Model](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Cloud-Concept/Share-Responsibility-Model.md)

## Core Services

### Database
- [RDS](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Core-Services/Database/RDS.md)
- [Aurora](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Core-Services/Database/Aurora.md) - serverless
- [DynamoDB](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Core-Services/Database/DynamoDB.md) - serverless
- [DocumentDB](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Core-Services/Database/DocumentDB.md)
- [Neptune](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Core-Services/Database/Neptune.md)
- [Keyspaces](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Core-Services/Database/Keyspaces.md) - serverless
- [Redshift](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Core-Services/Database/Redshift.md)

### Storage
- [S3](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Core-Services/Storage/S3.md) - serverless
- [EBS](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Core-Services/Storage/EBS.md)
- [EFS](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Core-Services/Storage/EFS.md)
- [Store Gateway](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Core-Services/Storage/Store-Gateway.md)

### Compute
- [AMI](https://github.com/chipbk10/SystemDesign/tree/master/AWS/Core-Services/Compute/AMI.md)
- [EC2](https://github.com/chipbk10/SystemDesign/tree/master/AWS/Core-Services/Compute/EC2.md)
- [Lambda](https://github.com/chipbk10/SystemDesign/tree/master/AWS/Core-Services/Compute/Lambda.md)
- [Batch](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Core-Services/Compute/Batch.md)
- [Elastic Beanstalk](https://github.com/chipbk10/SystemDesign/tree/master/AWS/Core-Services/Compute/Elastic-Beanstalk.md)
- [ECR](https://github.com/chipbk10/SystemDesign/tree/master/AWS/Core-Services/Compute/ECR.md)
- [ECS](https://github.com/chipbk10/SystemDesign/tree/master/AWS/Core-Services/Compute/ECS.md)
- [EKS](https://github.com/chipbk10/SystemDesign/tree/master/AWS/Core-Services/Compute/EKS.md)
- [Fargate](https://github.com/chipbk10/SystemDesign/tree/master/AWS/Core-Services/Compute/Fargate.md)

## Monitoring & Management
- [X-Ray](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Monitoring-Management/X-Ray.md)
- [System Manager](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Monitoring-Management/System-Manager.md)
- [CloudTrail](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Security-Compliance/CloudTrail.md)
- [CloudWatch](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Security-Compliance/CloudWatch.md)
- [Config](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Security-Compliance/Config.md)
- [Health](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Monitoring-Management/Health.md)
- [Service Health Dashboard](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Monitoring-Management/Service-Health-Dashboard.md)

### Networking
- [Load Balancer](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Core-Services/Networking/Load-Balancer.md)
  - Application Load Balancer (**ALB**), Network Load Balancer (**NLB**), **ELB**

## Security & Compliance
- [Organizations](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Security-Compliance/Organizations.md)
- [Inspector](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Security-Compliance/Inspector.md)
- [IAM](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Security-Compliance/IAM.md)
- [IAM Identity Center](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Security-Compliance/IAM-Identity-Center.md)
- [KMS](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Security-Compliance/KMS-SecretsManager.md)
- [Secret Manager](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Security-Compliance/KMS-SecretsManager.md)
- [CloudHSM](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Security-Compliance/CloudHSM.md)
- [Amazon Macie](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Security-Compliance/Amazon-Macie.md)

## Deployment & Migration
- [Auto Scaling](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Deployment-Migration/Auto-Scaling.md)
- [CloudFormation](https://github.com/chipbk10/SystemDesign/tree/master/AWS/Deployment-Migration/CloudFormation.md)
- [OpsWorks](https://github.com/chipbk10/SystemDesign/tree/master/AWS/Deployment-Migration/OpsWorks.md)
  
### CI/CD
- [CodeCommit](https://github.com/chipbk10/SystemDesign/tree/master/AWS/Deployment-Migration/CI-CD/CodeCommit.md), [CodeDeploy](https://github.com/chipbk10/SystemDesign/tree/master/AWS/Deployment-Migration/CI-CD/CodeDeploy.md), [CodePipeline](https://github.com/chipbk10/SystemDesign/tree/master/AWS/Deployment-Migration/CI-CD/CodePipeline.md)

## Pricing & Billing
- [Pricing Models](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Pricing-Billing/Pricing-Models.md)
  - On-Demand, Reserved, Spot, Saving Plans, Dedicated Host
- [Cost Explorer](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Pricing-Billing/CostExplorer-Budget.md)
- [Budget](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Pricing-Billing/CostExplorer-Budget.md)
- [Pricing Calculator](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Pricing-Billing/Pricing-Calculator.md)
- [TCO](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Pricing-Billing/TCO.md)

## Machine Learning
- [Sage-Maker](https://github.com/chipbk10/SystemDesign/tree/master/AWS/Machine-Learning/Sage-Maker.md)
- [Rekognition](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Machine-Learning/Rekognition.md)
- [Lex](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Machine-Learning/Lex.md)
- [Polly](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Machine-Learning/Polly.md)
- [Transcribe](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Machine-Learning/Transcribe.md)
- [Translate](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Machine-Learning/Translate.md)

## Support
- [APN Consulting Partners](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Support/APN-Consulting-Partner.md)
- [APN Technology Partners](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Support/APN-Technology-Partners.md)
- [Concierge Support Team](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Support/Concierge-Support-Team.md)

## Others
- OpsWorks, Lightsail, GuardDuty, AWS MFA (virtual, hardware, u2f)

## [Terms](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Terms.md)

## [Exam Tips](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Exam-Tips.md)
