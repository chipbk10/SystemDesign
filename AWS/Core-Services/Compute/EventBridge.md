*   **Lambda** is the **compute engine** that runs your code.
*   It **doesn’t generate events** by itself; it **reacts to events** from other sources like:
    *   **Amazon S3** (file upload)
    *   **DynamoDB Streams**
    *   **API Gateway**
    *   **EventBridge** (scheduled or custom events)

***

### **EventBridge vs Lambda**

*   **EventBridge** = Event **producer and router** (decides *when* and *why* something happens).
*   **Lambda** = Event **consumer and executor** (runs the logic when triggered).

Think of it like:

*   **EventBridge** = “Alarm clock” (schedules or routes events).
*   **Lambda** = “Action” (what happens when the alarm rings).

***

✅ Together, they form a **serverless workflow**:  
EventBridge triggers Lambda → Lambda executes your backup process.
