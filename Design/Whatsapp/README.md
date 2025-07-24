# Question
- Let's design a scalable online chat application (similar to Whatsapp or Slack)

# Clarify Requirements

## Functional Requirements
- The user can chat with another in an individual chat
- The user can chat with others in a group chat
- A chat message contains text, image, video, icon, etc
- In an individual chat, one user can see if other has read the message
- In (individual or group) chat, one user can see if other's typing
- The user can see all his (individual or group) chats in the history
- The user can see if others are online or offline
- The user can receive notifications for new messages in chats they've joined
- Optional:
  - the users can edit/delete their own messages in a chat
  - the users can delete a chat (but still visible from other users' view)
  - the users can leave a group chat

## Non-Functional Requirements
- Scalability: The system can handle millions of (individual or group) chats at a time
- Latency: The system ensures a low latency message delivery
- Security: The system encrypts all chats in database
- Availability: the system ensures 99,9% uptime (e.g., 8.76 hours downtime per year), even when some components fail (e.g., regional outages)
- Reliability:
  - no message (text, icon, image, video, etc) loss during delivery
  - the system ensures the messages in correct order (Please confirm)
- Consistency: all users must eventually see the same state of shared chats (please confirm)

