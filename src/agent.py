from src.rag_pipeline import retrieve_docs
from src.tools import mock_lead_capture
from src.workflow import state
from src.llm import generate_response


def run_agent(user_input):

    msg = user_input.lower().strip()

    # STEP 1 — lead capture state
    if state["intent"] == "lead":

        if state["name"] is None:
            state["name"] = user_input
            return "Thanks! What is your email?"

        elif state["email"] is None:
            state["email"] = user_input
            return "Which creator platform do you use?"

        elif state["platform"] is None:
            state["platform"] = user_input

            result = mock_lead_capture(
                state["name"],
                state["email"],
                state["platform"]
            )

            state["intent"] = None

            return f"Lead captured successfully: {result}"

    # STEP 2 — greeting
    if msg in ["hi", "hello", "hey"]:
        return "Hello! How can I help you with AutoStream?"

    # STEP 3 — purchase intent
    if "buy" in msg or "signup" in msg or "try" in msg:
        state["intent"] = "lead"
        return "Great! May I have your name?"

    # STEP 4 — RAG knowledge retrieval for ANY question
    docs = retrieve_docs(user_input)

    if docs:
        context = "\n".join([doc.page_content for doc in docs])
        return generate_response(context, user_input)

    return "I'm not sure about that. Could you ask something about AutoStream?"
