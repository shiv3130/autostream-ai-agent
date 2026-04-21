import warnings
import logging
import os

# Suppress Python warnings
warnings.filterwarnings("ignore")

# Suppress transformers logs
logging.getLogger("transformers").setLevel(logging.ERROR)

# Suppress HuggingFace hub messages
os.environ["HF_HUB_DISABLE_TELEMETRY"] = "1"
os.environ["HF_HUB_DISABLE_PROGRESS_BARS"] = "1"
os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"
os.environ["TOKENIZERS_PARALLELISM"] = "false"
os.environ["TRANSFORMERS_VERBOSITY"] = "error"

logging.getLogger("huggingface_hub").setLevel(logging.ERROR)
warnings.filterwarnings("ignore")

from src.agent import run_agent

print("\nAutoStream AI Agent Ready\n")

while True:

    user_input = input("User: ")

    if user_input.lower() in ["exit", "quit"]:
        print("Agent: Goodbye!")
        break

    response = run_agent(user_input)

    print("Agent:", response)
