import os
import langchain
from langchain.chains import ConversationChain
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory

os.environ["OPENAI_API_KEY"] = "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"

langchain.verbose = True

chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0, max_tokens=100)
conversation = ConversationChain(
    llm=chat,
    memory=ConversationBufferMemory()
)

while True:
    user_message = input("You: ")
    ai_message = conversation.predict(input=user_message)
    print(f"AI: {ai_message}")