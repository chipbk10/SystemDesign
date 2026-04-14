## API‑First Architecture:

- In modern software systems, the core functionality is implemented as backend services that expose their capabilities through stable, well‑defined APIs. 
- These APIs act as the primary interface to the system’s business logic and data, independent of how the system is accessed.
  - It means that the core system behaves the same way regardless of who or what is calling it.
- User‑facing applications such as web or mobile GUIs, as well as developer‑focused tools like CLIs, scripts, and integrations, are all clients of these APIs.
- This separation of concerns allows the core system to remain reusable, scalable, and evolvable, while client applications can be added, changed, or replaced without impacting the underlying logic.
