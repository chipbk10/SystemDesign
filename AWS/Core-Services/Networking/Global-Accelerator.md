**AWS Global Accelerator** is a **networking service** that improves the **availability and performance** of your applications by using the **AWS global network**.

***

### ✅ **What does it do?**

*   Provides **static IP addresses** that act as a fixed entry point to your application.
*   Routes user traffic through the **AWS global backbone** instead of the public internet.
*   Uses **Anycast** to direct traffic to the nearest AWS edge location for lower latency.
*   Automatically **fails over** to healthy endpoints in case of outages.

***

### ✅ **Key Benefits**

*   **Improved performance**: Reduces latency by routing traffic through AWS’s optimized network.
*   **High availability**: Health checks and automatic failover between regions.
*   **Static IPs**: Simplifies DNS and client configuration.

***

### ✅ **Use Cases**

*   Global web applications.
*   Gaming platforms.
*   APIs that need consistent low latency.
*   Disaster recovery with multi-region endpoints.

***

### ✅ **How it works**

*   You create an **Accelerator** with two static IPs.
*   Add **endpoints** (ALBs, NLBs, EC2 instances) in multiple regions.
*   Global Accelerator routes traffic to the closest healthy endpoint.
