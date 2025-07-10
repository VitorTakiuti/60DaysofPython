#pip install openai
#pip install python-dotenv
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "hi, how are you?"
        }
    ], 
    model="gpt-3" #Your GPT model
)

print(chat_completion.choices[0].message.content)