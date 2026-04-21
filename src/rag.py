import json

def load_kb():
    with open("data/knowledge_base.json") as f:
        return json.load(f)


def retrieve_answer(question):

    kb = load_kb()

    question = question.lower()

    if "price" in question or "plan" in question:
        return kb["pricing"]

    if "refund" in question:
        return kb["policies"]["refund"]

    if "support" in question:
        return kb["policies"]["support"]

    return "Let me check that for you."
