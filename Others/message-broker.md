I.**Message Broker**
- is a middleware component that facilitates communication between different parts of a system by managing the exchange of messages
- decouples the sender and receiver, allowing them to operate independently and asynchronously

II.**Functions**
1.**Decoupling**: producers don't need to know who consumes the messages or when the message is handled
2.**Queuing**: messages are held in a queue until consumers are ready to process them
3.**Routing**: directs messages to the right recipients based on rules or topics
4.**Reliability**: ensures messages aren't lost (e.g., by persisting them to disk)

