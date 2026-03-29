# Internal MCP

## Example
- An user asks **Claude Desktop** to **list all files in a folder** on his local machine

### Step 1 - User types the prompt
- List all files and folders in `/Users/john/Documents/Projects` for me please!

### Step 2 - Claude Desktop receives the Prompt
- Claude Desktop will send to the Claude Model
  - the current prompt
  - conversation history
  - all discovered tool definitions (translated from MCP into Claude’s tool format). E.g., `list_directory`, `read_file`, `write_file`, etc.
  - internal system prompt (how to use tools)

### Step 3 - Claude Model reasons
- The Claude model receives the prompt + tool list
- It understands the request and sees that the tool `list_directory` matches perfectly.
- It decides to use the tool and outputs a structured tool call:
```
{
  "type": "tool_use",
  "id": "toolu_abc123...",
  "name": "list_directory",
  "input": {
    "path": "/Users/john/Documents/Projects"
  }
}
```

### Step 4 - MCP Client intercepts the Tool Call
- Claude Desktop receives the API response.
- The built-in MCP Client:
  - Detects the tool_use block.
  - Looks up which MCP server provides the tool named list_directory (your Filesystem MCP server).
  - Converts the tool call into a JSON-RPC request.
  - Sends it to the Filesystem MCP server via STDIO (local communication).

### Step 5 - Filesystem MCP Server Executes
- The Filesystem MCP server:
  - Receives the JSON-RPC request for `list_directory`.
  - Checks that the path is inside the allowed directories you configured (sandboxing).
  - Performs the actual operation (fs.readdir on your Mac).  
  - Returns the result (list of files and folders) back to the MCP Client.
 
### Step 6 - Result is Sent Back to the Model
- Claude Desktop creates a tool_result block containing:
  - The original tool_use_id
  - The directory listing result from the server
- It sends this back to the Claude model in a new API call.

### Step 7 - Claude Model Generates Final Response
- The model receives the tool result.
- It now has the real list of files.
- It generates a natural language answer, for example:
  - “Here are the contents of the folder:[DIR]  MyApp  
  - [FILE] README.md (2.3 KB)  
  - [FILE] package.json ...”

### Step 8 - Displayed to User
- Claude Desktop shows the final response to you.











