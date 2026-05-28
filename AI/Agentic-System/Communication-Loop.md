## Summary 1: Agent and LLM Communication Loop
Because LLMs are entirely stateless and have no built-in access to the internet, they rely on an Agent wrapper program to act as their memory, hands, and feet. This dynamic is a strict, asynchronous back-and-forth communication flow

## Step 1: User Request to Agent

* Action: You ask the Agent, "What is the weather now in Hanoi?"
* Payload: The Agent packages this text with a system prompt and a JSON list of definitions for external tools it controls (like a get_weather function). It sends this entire package as Request 1 to the LLM.

## Step 2: LLM Tool Selection

* Action: The LLM reads the request, realizes it lacks live data, and looks at the available tool list.
* Payload: The LLM intercepts the text response and instead generates Response 1, returning a precise JSON instruction containing tool_calls. This instruction specifies the exact function name and arguments it needs (e.g., get_weather(location: "Hanoi")).

## Step 3: Agent Tool Execution

* Action: The Agent receives Response 1, stops, extracts the instructions, and executes the local API code to fetch the weather for Hanoi.
* Payload: The Agent gathers the raw data (e.g., {"temp": 32, "unit": "C"}) and constructs Request 2. This request includes the entire history (Request 1 + Response 1) appended with the new raw data labeled under role: "tool".

## Step 4: Final Answer Generation

* Action: The LLM reads the complete history. It recognizes the context, accepts the raw temperature data, and synthesizes it into conversational text.
* Payload: The LLM responds with Response 2 ("It is currently 32°C and sunny in Hanoi."). The Agent reads this text and prints it onto your screen.

```json
{
  "model": "gpt-4o",
  "messages": [
    { "role": "system", "content": "You are a helpful assistant." },
    
    // --- Turn 1: Your first question (Request 1) ---
    { "role": "user", "content": "What is the weather now in Hanoi?" },
    
    // --- Turn 1: LLM asks for the tool (Response 1) ---
    {
      "role": "assistant",
      "content": null,
      "tool_calls": [
        { "id": "weather_01", "type": "function", "function": { "name": "get_weather", "arguments": "{\"location\":\"Hanoi\"}" } }
      ]
    },
    
    // --- Turn 2: Agent sends tool data (Request 2 Part A) ---
    { "role": "tool", "tool_call_id": "weather_01", "content": "{\"location\": \"Hanoi\", \"temperature\": 32, \"unit\": \"C\"}" },
    
    // --- Turn 2: LLM answers you (Response 2 / Request 2 Part B) ---
    { "role": "assistant", "content": "It is currently 32°C and sunny in Hanoi." },
    
    // --- Turn 3: Your new question ---
    { "role": "user", "content": "Is Hanoi hotter than Brussels?" }
  ],
  "tools": [
    // (The get_weather tool definition is still included here)
  ]
}
```
