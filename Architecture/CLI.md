## Command-Line Interface (CLI)

A Command-Line Interface (CLI) is a standalone executable program that allows users and scripts to interact with a system using text-based commands. A CLI acts as a client of backend services by translating commands into API requests and presenting the results in a human-readable format. While CLIs can be invoked manually or from automation scripts, they operate by spawning a separate process and communicating via standard input and output, rather than through in-process function calls like an SDK.

### Example

Assume the system exposes an API endpoint to list users:

    GET /users

A user can retrieve the list of users using the CLI:

```bash
example-cli users list
```

The CLI sends a request to the API, processes the response, and formats the output for display in the terminal:

```text
ID   Name
1    Alice
2    Bob
```

### Explanation

In this example:

*   The CLI command is mapped to an API call.
*   The backend behavior is entirely defined by the API.
*   The CLI is responsible for request execution, authentication handling, and output formatting.
*   The same API may be accessed by other clients, such as GUIs, SDKs, or automated scripts.

CLIs are well suited for manual operations, scripting, and automation, but they remain clients of the API and do not replace programmatic integration through SDKs.
