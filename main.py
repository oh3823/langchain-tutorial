import os
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage
from dotenv import load_dotenv

load_dotenv()

model = init_chat_model("gemini-2.0-flash", model_provider="google_genai")

messages = [
    SystemMessage("Translate the following from English into Italian"),
    HumanMessage("hi!"),
]

for token in model.stream(messages):
    print(token.content, end="|")