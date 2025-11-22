### Application Load Balancer (ALB)
- An Application Load Balancer serves as the single point of contact for clients.
- The load balancer distributes incoming application traffic across multiple targets, such as EC2 instances, in multiple Availability Zones.
- It distributes traffic, does not scale resources.

### Network Load Balancer (NLB)
- Network Load Balancer is best suited for load balancing of Transmission Control Protocol (TCP), User Datagram Protocol (UDP) and Transport Layer Security (TLS) traffic where extreme performance is required.
- It distributes traffic, does not scale resources.

### ELB
- @Todo
