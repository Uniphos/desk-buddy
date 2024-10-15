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

completion = client.chat.completions.create(
    messages=messages,
    model="gpt-3.5-turbo",
)

print(completion)