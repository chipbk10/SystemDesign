# Channels

- Channels are modular adapters that connect the OpenClaw Gateway to external messaging platforms such as WhatsApp, Telegram, Discord, Slack, Signal, and iMessage.
- They handle authentication, real-time messaging, and event normalization. Multiple channels can operate simultaneously under one Gateway.
- Each channel (or group of channels) can be bound to a specific agent and LLM. This allows different messaging apps to use different models, thinking levels, or specialized agents (for example, WhatsApp using Claude 4 while Discord uses a local model).Channel-to-agent/LLM binding is configured in openclaw.json or via the Control UI.




