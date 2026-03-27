### External Hooks (Webhooks)
- enable outside services to send data into OpenClaw via HTTP POST requests.
- They act as callback URLs that external platforms (such as GitHub, Stripe, or Gmail) can call when an event happens.
- Webhooks are configured in openclaw.json with mappings to convert incoming payloads into agent messages or actions.
- A secure tunnel (such as Tailscale Funnel) is usually required to make the local Gateway reachable from the internet.

