### ✅ **AWS Elastic Load Balancing (ELB)**

*   **ELB** is the general service that automatically distributes incoming application or network traffic across multiple targets (like EC2 instances, containers, IP addresses) in one or more Availability Zones.
*   It improves **fault tolerance**, **scalability**, and **availability**.

AWS ELB offers **three main types of load balancers**:

1.  **Application Load Balancer (ALB)** – Layer 7 (HTTP/HTTPS)
2.  **Network Load Balancer (NLB)** – Layer 4 (TCP/UDP)
3.  **Gateway Load Balancer (GWLB)** – For third-party virtual appliances

### Application Load Balancer (ALB)
- An Application Load Balancer serves as the single point of contact for clients.
- The load balancer distributes incoming application traffic across multiple targets, such as EC2 instances, in multiple Availability Zones.
- It distributes traffic, does not scale resources.

### Network Load Balancer (NLB)
- Network Load Balancer is best suited for load balancing of Transmission Control Protocol (TCP), User Datagram Protocol (UDP) and Transport Layer Security (TLS) traffic where extreme performance is required.
- It distributes traffic, does not scale resources.

### GWLB
- @Todo
