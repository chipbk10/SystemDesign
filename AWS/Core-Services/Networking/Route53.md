### **Route 53**

*   **Purpose**: Route 53 manages domain names and routes traffic to AWS resources or external endpoints.
*   **Key Features**:
    *   **DNS Resolution**: Converts domain names to IP addresses.
    *   **Routing Policies**: Simple, Weighted, Latency-based, Geolocation, Failover.
    *   **Health Checks**: Monitors endpoints for availability.
    *   **Domain Registration**: You can buy and manage domains.

***

### **Scenario**: A user wants to access `www.example.com` hosted on an EC2 instance behind an Elastic Load Balancer (ELB).

1.  **User enters URL**: `www.example.com` in their browser.
2.  **DNS Query to Route 53**:
    *   The browser asks Route 53: “What is the IP address for `www.example.com`?”
3.  **Route 53 checks the hosted zone**:
    *   Finds the record (e.g., an **A record** or **Alias record**) pointing to the ELB (or ALB, or CloudFront)
4.  **Route 53 responds with IP**:
    *   Returns the IP address of the ELB.
5.  **Traffic flows to ELB**:
    *   The browser sends the request to the ELB.
6.  **ELB forwards to EC2**:
    *   The load balancer distributes traffic to healthy EC2 instances in multiple AZs.
7.  **Response back to user**:
    *   EC2 processes the request and sends the response back through the ELB → user.

***

✅ **Key Role of Route 53**: It only handles **DNS resolution** (mapping domain names to IP addresses). It does **not** carry the actual traffic—after DNS resolution, traffic flows directly to the resource.

***
