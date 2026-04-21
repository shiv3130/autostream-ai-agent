# AutoStream AI Agent – Social-to-Lead Conversational Workflow

## Project Overview

This project implements a **Conversational AI Agent** for a fictional SaaS company called **AutoStream**, an AI-powered platform that helps content creators automatically edit videos.

The objective of the agent is to simulate a real-world **AI sales assistant** that can:

* Understand user intent
* Answer product-related questions
* Retrieve accurate information using a **RAG (Retrieval Augmented Generation) pipeline**
* Detect high-intent users who are ready to sign up
* Capture qualified leads using a backend tool

Unlike traditional rule-based chatbots, this system combines **LLM reasoning, vector search, and conversational state management** to provide accurate and context-aware responses.

The agent interacts with users through a conversational interface and guides them from **product inquiry to lead conversion**.

---

# Agent Capabilities

The AutoStream AI Agent supports the following core capabilities:

### 1. Intent Detection

The agent identifies user intent and classifies conversations into three categories:

* **Greeting**
* **Product inquiry**
* **High-intent lead**

Example:

```
User: Hi
Agent: Hello! How can I help you with AutoStream?

User: What is the pricing?
Agent: (retrieves pricing from knowledge base)

User: I want to try the Pro plan
Agent: Great! May I have your name?
```

---

### 2. RAG-Based Knowledge Retrieval

The system uses **Retrieval Augmented Generation (RAG)** to answer product questions using a local knowledge base.

Product data is stored in:

```
data/knowledge_base.md
```

This file contains:

* AutoStream pricing
* Product features
* Company policies

The pipeline works as follows:

```
User Question
      ↓
Vector Search (FAISS)
      ↓
Retrieve Relevant Documents
      ↓
LLM generates contextual answer
```

This approach ensures that the agent provides **accurate responses grounded in the product documentation**.

---

### 3. Lead Qualification & Tool Execution

When the agent detects **high purchase intent**, it starts a lead-capture workflow.

The agent collects the following information:

* Name
* Email
* Creator Platform (YouTube, Instagram, etc.)

Once all information is gathered, the agent triggers a backend tool:

```python
def mock_lead_capture(name, email, platform):
    print(f"Lead captured successfully: {name}, {email}, {platform}")
```

This simulates sending a qualified lead to a CRM or marketing system.

---

# How to Run the Project Locally

Follow these steps to run the project locally.

## 1. Clone the repository

```bash
git clone https://github.com/yourusername/autostream-agent.git
cd autostream-agent
```

---

## 2. Create a virtual environment

```bash
python3 -m venv ml_env
source ml_env/bin/activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Add your Gemini API key

Create a `.env` file in the root directory:

```
GEMINI_API_KEY=your_api_key_here
```

---

## 5. Run the agent

```bash
python run.py
```

---

## Example Interaction

```
User: hi
Agent: Hello! How can I help you with AutoStream?

User: what is the pricing
Agent: AutoStream offers two plans:
       Basic Plan – $29/month
       Pro Plan – $79/month

User: I want to try the pro plan
Agent: Great! May I have your name?

User: Shiva
Agent: What is your email?

User: shiva@email.com
Agent: Which creator platform do you use?

User: YouTube
Agent: Lead captured successfully
```

---

# Architecture Explanation

This project uses a modular **agent-based architecture** inspired by modern GenAI systems.

The core workflow consists of:

```
User Input
     ↓
Intent Detection
     ↓
RAG Knowledge Retrieval
     ↓
LLM Reasoning
     ↓
Lead Qualification
     ↓
Tool Execution
```

### Why LangGraph / Agent Architecture

LangGraph (or similar agent orchestration frameworks) is well suited for building conversational agents because it allows developers to design **state-driven workflows** rather than simple linear prompts.

This approach enables:

* Structured conversation flows
* Conditional decision making
* Tool integration
* Stateful interactions

Although this implementation uses a lightweight custom workflow, the structure is compatible with LangGraph-style agent orchestration.

### State Management

Conversation state is stored in a shared state object:

```python
state = {
    "intent": None,
    "name": None,
    "email": None,
    "platform": None
}
```

This enables the agent to remember user information across multiple conversation turns.

For example:

```
User: I want to try Pro
Agent: What is your name?

User: Shiva
Agent: What is your email?
```

The agent remembers that it is currently in **lead-capture mode**, ensuring that the correct questions are asked sequentially.

This state-driven approach ensures **clean conversation management and controlled tool execution**.

---

# WhatsApp Deployment (Webhook Integration)

In a real-world scenario, this AI agent could be deployed as a **WhatsApp conversational assistant** using webhook-based messaging.

The architecture would look like this:

```
User (WhatsApp)
        ↓
WhatsApp Business API
        ↓
Webhook Server
        ↓
AI Agent Backend
        ↓
Response returned to WhatsApp
```

### Deployment Steps

1. A user sends a message through WhatsApp.

2. The WhatsApp Business API forwards the message to a **webhook endpoint**.

3. The webhook server sends the message to the AI agent.

4. The agent processes the request using:

   * intent detection
   * RAG knowledge retrieval
   * lead qualification logic

5. The agent generates a response using the LLM.

6. The response is sent back through the webhook to the user.

If the user expresses high intent, the lead information collected by the agent could be sent to:

* CRM systems (HubSpot, Salesforce)
* Marketing automation tools
* Internal lead databases

This design enables businesses to automatically convert **social media conversations into qualified leads**.

---

# Project Structure

```
autostream-agent
│
├── src
│   ├── agent.py
│   ├── rag_pipeline.py
│   ├── llm.py
│   ├── tools.py
│   └── workflow.py
│
├── data
│   └── knowledge_base.md
│
├── notebooks
│
├── run.py
├── requirements.txt
└── README.md
```

---

# Technologies Used

* Python
* Gemini LLM API
* LangChain components
* FAISS vector search
* Sentence Transformers embeddings

---

# Future Improvements

Possible enhancements include:

* FastAPI backend deployment
* LangGraph workflow orchestration
* Docker containerization
* Integration with WhatsApp Business API
* CRM integration for real lead management
=======
