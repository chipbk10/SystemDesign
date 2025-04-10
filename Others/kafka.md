I.**Apache Kafka**
- is a distributed event streaming platform that evolved from a [message broker]() concept, but goes beyond traditional brokers.
- it's designed for high-throughput, scalable, and fault-tolerant handling of real-time data streams

II.**Function**
- categorize messages by topics
- topics are split into partitions for parallel processing and scalability
- a Kafka cluster store and manage data on many brokers (servers)
- messages are kept for a set period (e.g., 7 days) or indefinitely, unlike traditional brokers that delete after delivery
- Kafka handles millions of messages per second, while RabbitMQ (a traditional message broker) excels at lower volumes with low latency
- Kafka can scale horizontally with more brokers and partitions, while traditional brokers scale vertically or with clustering (e.g., adding more RabbitMQ broker to handle)
