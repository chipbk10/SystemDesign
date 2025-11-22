### ✅ **What is AWS Local Zones?**

*   A **Local Zone** is an **extension of an AWS Region** located in a specific metro area.
*   It brings **compute, storage, and database services closer to end-users** who need **single-digit millisecond latency**.
*   Ideal for:
    *   Real-time gaming
    *   Media & entertainment
    *   Machine learning inference
    *   Hybrid workloads (where part of the app runs on-prem)

***

### **Key Points**

*   Local Zones **host core services** like EC2, EBS, ECS, EKS, and sometimes RDS.
*   They are **linked to a parent Region** for full AWS service access.
*   Different from **Edge Locations** (which are for CDN via CloudFront) and **Wavelength Zones** (which are inside 5G networks).

***

✅ **Quick Placement**:

*   **Networking → AWS Global Infrastructure**:
    *   Regions
    *   Availability Zones
    *   Local Zones
    *   Wavelength Zones
    *   Edge Locations

***

**Exam Tip**:  
If the question mentions **low latency for metro areas without deploying full Regions**, the answer is **Local Zones**.
