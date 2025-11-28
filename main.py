import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

os.environ.get

client = genai.Client(
    api_key=API_KEY
)

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="my name is uzair"
)

print(response.text)

print("prompt token:",response.usage_metadata.prompt_token_count)
print("response token:",response.usage_metadata.candidates_token_count)