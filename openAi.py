from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize the OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)

messages = [
    {
        "role": "system",
        "content": "You are a helpful assistant.",
    }
]

def get_response(msg):
    messages.append(
        {
            "role": "user",
            "content": msg,
        }
    )

    completion = client.chat.completions.create(
        messages=messages,
        model="gpt-3.5-turbo",
    )

    answer = completion.choices[0].message.content

    messages.append(
        {
            "role": "assistant",
            "content": answer,
        }
    )

    return completion.choices[0].message.content

    # clear the messages
def clear_messages():
    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant.",
        }
    ]

    #return print("Messages cleared")