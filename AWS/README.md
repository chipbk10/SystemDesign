# AWS

## Cloud Concept
- [6 Advantages of Cloud Computing](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Cloud-Concept/Advantages-Cloud-Computing.md)
  - pay-as-you-go, economies, easily-scale-out-in, speed, no-infrastructure-maintenance, go-global
- [Types of Cloud Computing](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Cloud-Concept/Type-Cloud-Computing.md)
  - IaaS, PaaS, SaaS
- [Global Infrastructure](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Cloud-Concept/Global-Infrastructure.md)
  - Data Center, Availability Zone (AZ), Region, Edge Location (CDN)
- [Share Responsibility Model](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Cloud-Concept/Share-Responsibility-Model.md)

## Well-Architected Framework
- [6 Pillars](https://github.com/chipbk10/SystemDesign/tree/master/AWS/Architect)
  - Operational Excellence (Agility, Automation, Monitoring),
  - Security,
  - Reliability (HA, Fault Tolerance),
  - Performance Efficiency (Elasticity, Scalability),
  - Cost Optimization (pay-as-you-go),
  - Sustainability (environment impact)
- [Principles](https://github.com/chipbk10/SystemDesign/tree/master/AWS/Architect/Principles.md)
  - High Availability (HA), Agility, Scalability, Fault Tolerance, Elasticity

## Core Services

### Database
- [RDS](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Core-Services/Database/RDS.md)
- [Aurora](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Core-Services/Database/Aurora.md) - serverless
- [DynamoDB](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Core-Services/Database/DynamoDB.md) - serverless, default encryption
- [DocumentDB](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Core-Services/Database/DocumentDB.md) - default encryption
- [Neptune](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Core-Services/Database/Neptune.md) - default encryption
- [Keyspaces](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Core-Services/Database/Keyspaces.md) - serverless
- [Redshift](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Core-Services/Database/Redshift.md) - default encryption

### Storage
- [S3](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Core-Services/Storage/S3.md) - serverless
- [EBS](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Core-Services/Storage/EBS.md)
- [EFS](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Core-Services/Storage/EFS.md)
- [Store Gateway](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Core-Services/Storage/Store-Gateway.md)

### Compute
- [AMI](https://github.com/chipbk10/SystemDesign/tree/master/AWS/Core-Services/Compute/AMI.md)
- [EC2](https://github.com/chipbk10/SystemDesign/tree/master/AWS/Core-Services/Compute/EC2.md)
- [Lambda](https://github.com/chipbk10/SystemDesign/tree/master/AWS/Core-Services/Compute/Lambda.md) - serverless
- [Batch](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Core-Services/Compute/Batch.md)
- [EventBridge](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Core-Services/Compute/EventBridge.md) - serverless
- [Step Function](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Core-Services/Compute/Step-Function.md) - serverless
- [Glue](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Core-Services/Compute/Glue.md)
- [EMR](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Core-Services/Compute/EMR.md) - big data, MapReduce, Hadoop
- [Elastic Beanstalk](https://github.com/chipbk10/SystemDesign/tree/master/AWS/Core-Services/Compute/Elastic-Beanstalk.md)
- [ECR](https://github.com/chipbk10/SystemDesign/tree/master/AWS/Core-Services/Compute/ECR.md)
- [ECS](https://github.com/chipbk10/SystemDesign/tree/master/AWS/Core-Services/Compute/ECS.md)
- [EKS](https://github.com/chipbk10/SystemDesign/tree/master/AWS/Core-Services/Compute/EKS.md)
- [Fargate](https://github.com/chipbk10/SystemDesign/tree/master/AWS/Core-Services/Compute/Fargate.md) - serverless
- [LightSail](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Core-Services/Compute/LightSail.md)

### Message Services
- [SNS](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Core-Services/Message/SNS.md) - serverless
- [SQS](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Core-Services/Message/SQS.md) - serverless
- [Amazon MQ](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Core-Services/Message/Amazon-MQ.md)
- [Kinesis](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Core-Services/Message/Kinesis.md)

### Networking
- [Networking](https://github.com/chipbk10/SystemDesign/edit/master/AWS/Core-Services/Networking/Networking.md)
  - VPC, Subnet, Internet Gateway, NAT Gateway, Route Table, Security Group, Network ACLs
  - VPC peering connection, VPC endpoint, Site-To-Site VPN, Direct Connect, PrivateLink, Transit Gateway
- [WaveLength](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Core-Services/Networking/WaveLength.md)
- [Local Zones](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Core-Services/Networking/LocalZones.md)
- [Route 53](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Core-Services/Networking/Route53.md)
- [Global Accelerator](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Core-Services/Networking/Global-Accelerator.md)
- [Load Balancer](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Core-Services/Networking/Load-Balancer.md)
  - Elastic Load Balancer (ELB), Application Load Balancer (**ALB**), Network Load Balancer (**NLB**), 
    
## Monitoring & Management
- [X-Ray](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Monitoring-Management/X-Ray.md)
- [System Manager](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Monitoring-Management/System-Manager.md)
- [CloudTrail](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Security-Compliance/CloudTrail.md) - default encryption
- [CloudWatch](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Security-Compliance/CloudWatch.md) - default encryption
- [Config](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Security-Compliance/Config.md)
- [Health](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Monitoring-Management/Health.md)
- [Service Health Dashboard](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Monitoring-Management/Service-Health-Dashboard.md)

## Security & Compliance
- [Organizations](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Security-Compliance/Organizations.md)
- [Inspector](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Security-Compliance/Inspector.md)
- [IAM](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Security-Compliance/IAM.md)
- [IAM Identity Center](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Security-Compliance/IAM-Identity-Center.md)
- [KMS](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Security-Compliance/KMS-SecretsManager.md)
- [CMK](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Security-Compliance/CMK.md)
- [Secret Manager](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Security-Compliance/KMS-SecretsManager.md)
- [CloudHSM](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Security-Compliance/CloudHSM.md)
- [Amazon Macie](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Security-Compliance/Amazon-Macie.md)
- [Penetration Testing](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Security-Compliance/Penetration-Testing.md)

## Deployment & Migration
- [Migration Strategies: 7R](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Deployment-Migration/Migration-Strategies.md)
  - Retire, Retain, Rehost, Replatform, Relocate, Refactor, Repurchase
- [Auto Scaling](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Deployment-Migration/Auto-Scaling.md)
- [CloudFormation](https://github.com/chipbk10/SystemDesign/tree/master/AWS/Deployment-Migration/CloudFormation.md)
- [OpsWorks](https://github.com/chipbk10/SystemDesign/tree/master/AWS/Deployment-Migration/OpsWorks.md)
- [Equivalent](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Deployment-Migration/Equivalent.md)
  
### CI/CD
- [CodeCommit](https://github.com/chipbk10/SystemDesign/tree/master/AWS/Deployment-Migration/CI-CD/CodeCommit.md), [CodeDeploy](https://github.com/chipbk10/SystemDesign/tree/master/AWS/Deployment-Migration/CI-CD/CodeDeploy.md), [CodePipeline](https://github.com/chipbk10/SystemDesign/tree/master/AWS/Deployment-Migration/CI-CD/CodePipeline.md)

## Pricing & Billing
- [Pricing Models](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Pricing-Billing/Pricing-Models.md)
  - On-Demand, Reserved, Spot, Saving Plans, Dedicated Host
- [Cost Explorer](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Pricing-Billing/CostExplorer-Budget.md)
- [Budget](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Pricing-Billing/CostExplorer-Budget.md)
- [Pricing Calculator](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Pricing-Billing/Pricing-Calculator.md)
- [TCO](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Pricing-Billing/TCO.md)
- [Compute Optimizer](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Pricing-Billing/Compute-Optimizer.md)

## Machine Learning
- [Sage-Maker](https://github.com/chipbk10/SystemDesign/tree/master/AWS/Machine-Learning/Sage-Maker.md)
- [Rekognition](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Machine-Learning/Rekognition.md)
- [Lex](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Machine-Learning/Lex.md)
- [Polly](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Machine-Learning/Polly.md)
- [Transcribe](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Machine-Learning/Transcribe.md)
- [Translate](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Machine-Learning/Translate.md)

## Support
- [Professional Services](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Support/Professional-Services.md)
- [APN Consulting Partners](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Support/APN-Consulting-Partner.md)
- [APN Technology Partners](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Support/APN-Technology-Partners.md)
- [Concierge Support Team](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Support/Concierge-Support-Team.md)
- [Partner Solutions](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Support/Partner-Solutions.md)
- [Market](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Support/Market.md)
- [CAF](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Support/CAF.md)
- [Basic Support](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Support/Basic-Support.md)
- [Developer Support](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Support/Developer-Support.md)
- [Business Support](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Support/Business-Support.md)
- [Enterprise Support](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Support/Enterprise-Support.md)
- [Abuse Team](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Support/Abuse-Team.md)

## Others
- GuardDuty, AWS MFA (virtual, hardware, u2f), AWS SDK

## [Terms](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Terms.md)

## [Exam Tips](https://github.com/chipbk10/SystemDesign/blob/master/AWS/Exam-Tips.md)
