## Project Blueprint: AI Trend Aggregator Agent (MVP)
- This document outlines the high-level architecture and component design for the Minimum Viable Product (MVP) of an automated business intelligence agent.
------------------------------
## 📋 Product Overview
- The agent automatically collects daily trending discussions on a specific niche topic, filters and summarizes the information using an LLM, generates a clean text-only PDF report, and delivers it to non-technical business subscribers via email every morning.
------------------------------
## 🏗️ System Architecture
```
[ Static Frontend (GoDaddy) ] ──(User Subscribes)──► [ Backend API (Render/Railway) ]
                                                              │
                                                       (Saves Subscriber)
                                                              ▼
[ GitHub Actions (8:00 AM Cron) ] ──(Secure Trigger)──► [ Google Sheets DB ]
                                                              │
                                                      (Runs 5-Step Brain)
                                                              ▼
                                                   [ Subscriber Inboxes ]
```
## 1. Frontend & Ingestion

* Hosting: Hosted as a simple, static HTML form on an existing GoDaddy domain.
* Functionality: Collects user emails and subscription requests.
* Security (CORS): The FastAPI backend explicitly enables CORSMiddleware to safely allow cross-origin requests coming only from the GoDaddy domain.

## 2. Database & Storage

* Technology: Google Sheets API.
* Why: Replaces localized SQLite files which risk getting wiped out on ephemeral cloud hosting providers (like Render/Railway). It serves as a persistent, free data store that is easy to view manually.

## 3. The Automation Trigger

* Technology: GitHub Actions.
* Workflow: A cron job executes daily at 8:00 AM. It sends a secure POST request to the backend server's /run-agent endpoint.
* Endpoint Protection: To prevent unauthorized access, the endpoint checks for a custom API Key sent via the request header (X-API-KEY).

------------------------------
## 🧠 The Brain Workflow (Executed Daily at 8:00 AM)

  Step 1: Fetch Emails ──► Step 2: Gather Reddit Data ──► Step 3: Markdown & LLM
                                                                   │
  Step 5: Email Out     ◄──   Step 4: Create Text PDF   ◄──────────┘


   1. Fetch Subscribers: The script connects to the Google Sheets API and pulls the active email subscription list into system memory.
   2. Gather Social Data: The agent queries the Reddit API to grab the top 25 hot posts from r/redditdev focusing on the narrow scope topic: "AI for small business automation".
   3. Clean & Summarize:
   * The raw JSON payload from Reddit is stripped of all metadata.
      * The remaining titles and text bodies are compiled into a single token-efficient Markdown string.
      * This string is sent to GPT-4o-mini, which processes Markdown naturally and generates a high-level business intelligence summary.
   4. Local PDF Generation: The raw text summary is passed into the open-source FPDF2 Python library to build a simple, minimalist layout PDF file directly on the server for free.
   5. Delivery & Cleanup: The script logs into an email server via standard Python smtplib using an encrypted SMTP app password. It loops through the subscriber list, attaches the PDF, sends the emails, and immediately deletes the temporary PDF from the server.

------------------------------
## 🔒 Security Practices

* Zero Hardcoding: No sensitive credentials or API tokens are allowed inside the code repository.
* Secret Management:
* Local development uses a .env file added directly to .gitignore.
   * Production keys (OpenAI API key, Google Credentials, Email Passwords) are injected directly into the hosting environment variables (Render/Railway settings) and GitHub Repository Secrets.

------------------------------
## 🚀 Next Steps to Kick Off Development
If you are ready to start writing code, we can begin building the foundations in this order:

   1. Step 1: Write the foundational FastAPI server script complete with your security CORS headers.
   2. Step 2: Write the script that authenticates with Reddit and parses raw data into Markdown.
   3. Step 3: Implement the Google Sheets integration and LLM prompt handler.

Which codebase piece would you like to generate or map out first?


