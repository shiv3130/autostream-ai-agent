def classify_intent(user_message):

    msg = user_message.lower()

    if any(word in msg for word in ["hi", "hello"]):
        return "greeting"

    if any(word in msg for word in ["price", "pricing", "plan"]):
        return "pricing_inquiry"

    if any(word in msg for word in ["buy", "signup", "sign up", "try pro"]):
        return "high_intent"

    return "general_query"
