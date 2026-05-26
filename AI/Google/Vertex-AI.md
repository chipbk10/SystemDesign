## Technical Cheat Sheet: Vertex AI & Model Architecture

## 1. Core Problem Solved by Vertex AI
Vertex AI is an enterprise-ready AI development platform that unifies fragmented machine learning workflows. It solves five key industry problems:

* The MLOps Gap: Consolidates disconnected tools (data prep, training, deployment, monitoring) into one seamless environment.
* Scale Failures: Automatically handles infrastructure scaling, traffic splitting, and version control.
* Model Drift: Provides continuous monitoring tools to alert engineers when real-world data accuracy drops.
* Gen AI Hallucinations: Connects Large Language Models safely to internal company data using grounding and semantic search.
* The AI Talent Gap: Offers multiple development entry points ranging from no-code dashboards to deep custom coding.

------------------------------
## 2. The 3 Implementation Pathways
When building an application (like a Customer Feedback Classifier), you have three distinct architectural paths on Vertex AI:
## A. Generative AI (LLMs / Gemini)

* How it works: You use Google's massive, pre-trained Gemini models out of the box.
* Your input: No data or code required. You write a text prompt: "Classify this text as Positive or Negative: [Email text]".
* Pricing: Pay-per-token/character. Costs $0.00 if there is no traffic.
* Pros: Immediate setup (5 minutes); no historical data or training required.
* Cons: Can become expensive at extreme volumes; potential for generic logic.

## B. Vertex AI AutoML (No-Code Machine Learning)

* How it works: You upload historical data, and Google automatically handles feature extraction, tests various proprietary architectures, and creates a highly specific model.
* Your input: Clean historical dataset (e.g., a CSV with past emails and "Positive/Negative" labels).
* Pricing: Pay upfront for training hours, then pay a continuous hourly rate to keep the hosting server running.
* Pros: Exceptionally high accuracy; zero machine learning code required from your team.
* Cons: Vendor Lock-in. Text classification models built with AutoML cannot be downloaded or exported. You must host them on Google Cloud.

## C. Custom Training (Infrastructure Only)

* How it works: Vertex AI acts purely as Infrastructure-as-a-Service (IaaS). Google provides raw, high-performance hardware (GPUs/TPUs) on-demand to run your scripts.
* Your input: Open-source Python code (scikit-learn, PyTorch, TensorFlow) to load data, clean it, and feed it into an algorithm.
* Pricing: You pay strictly for the exact minutes or hours the GPU servers run your training code.
* Pros: No Vendor Lock-in. Once training completes, you can download the resulting model file (.pkl, .h5) and host it on your in-house servers for free.
* Cons: Requires manual coding, data science expertise, and testing different algorithms yourself.

------------------------------
## 3. Key Technical Clarifications (Interview Pitfalls)

* Who owns the algorithm? In Custom Training, you do not write the mathematical algorithms from scratch. Open-source libraries (scikit-learn, TensorFlow) provide the pre-built math engines (e.g., Logistic Regression, Random Forest).
* What is the purpose of the Python code? Your Python code acts as the manager. It cleans the raw data, tokenizes it, converts text into numbers (vectors/embeddings) that math equations can read, and feeds it to the open-source algorithm.
* Why can't Vertex AI just take a list of algorithms in Custom Training? Because every dataset has a different shape. Vertex AI leaves the custom environment blank so you can write the code required to translate your specific data into the exact format your chosen open-source library demands.
* What does Google add during Custom Training? On-demand server provisioning (no need to manage complex GPU drivers or CUDA libraries manually) and automated hyperparameter tuning via Vertex AI Vizier.

------------------------------

