**Developed production-ready GenAI Agent for Intelligent Loan Decisioning**

- Built an **agentic GenAI solution** on Google Cloud that automates commercial loan pre-qualification and initial risk assessment for small and medium businesses. 
- Leveraged **GitHub Copilot** extensively for rapid development, along with custom **prompts, agent skills, and instruction files** to create reliable, reusable agent behaviors and context-aware workflows.
- Designed and deployed a **Python-based FastAPI microservice** on GCP that integrates **Vertex AI** (Gemini models) for natural language understanding of loan applications and supporting documents.
- Used **LangChain** to orchestrate multi-step reasoning chains and tool-calling (document analysis, credit data lookup, policy rule checking), and **Google ADK (Agent Development Kit)** to build and manage the core autonomous agent logic.
- The agent processes incoming loan requests in real time, extracts key information from PDFs and unstructured data, applies bank risk policies, flags edge cases for human review, and returns a recommendation with clear explanations.

**Business Impact:**
- Reduced average loan pre-qualification time from **3–5 days to under 15 minutes**.
- Handled **~65% of straightforward applications end-to-end** without analyst involvement.
- Improved consistency of initial risk scoring and cut manual review workload by approximately 40%.
