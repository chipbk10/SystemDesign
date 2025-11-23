### ✅ **Amazon Simple Notification Service (SNS)**

*   **Type:** Pub/Sub messaging service.
*   **Purpose:** Send notifications to multiple subscribers (fan-out).
*   **Protocols supported:** HTTP/S, Email, SMS, Lambda, SQS.
*   **Use case:** Broadcast messages to many endpoints (e.g., alerts, notifications).
*   **Pattern:** **Publish-Subscribe**.

***

### ✅ **Amazon Simple Queue Service (SQS)**

*   **Type:** Message queue service.
*   **Purpose:** Decouple components by sending messages to a queue for asynchronous processing.
*   **Features:** Standard queues (unlimited throughput), FIFO queues (ordered delivery).
*   **Use case:** Reliable message delivery between microservices.
*   **Pattern:** **Point-to-Point**.

***

### ✅ **Amazon MQ**

*   **Type:** Managed message broker.
*   **Purpose:** Drop-in replacement for on-prem brokers like ActiveMQ or RabbitMQ.
*   **Protocols supported:** AMQP, MQTT, STOMP, OpenWire.
*   **Use case:** Migration from traditional messaging systems without code changes.
*   **Pattern:** **Broker-based messaging**.

***

### ✅ **Amazon Kinesis Data Streams**

*   **Type:** Real-time data streaming service.
*   **Purpose:** Capture and process large volumes of streaming data (e.g., logs, IoT data).
*   **Features:** Low-latency ingestion, shard-based scaling.
*   **Use case:** Real-time analytics, event-driven apps.
*   **Pattern:** **Stream processing**.

***

✅ **Quick Summary Table**

| Service   | Pattern           | Best For                             |
| --------- | ----------------- | ------------------------------------ |
| SNS       | Pub/Sub           | Notifications, fan-out messaging     |
| SQS       | Queue (async)     | Decoupling microservices             |
| Amazon MQ | Broker-based      | Migrating existing messaging systems |
| Kinesis   | Stream processing | Real-time data ingestion & analytics |
