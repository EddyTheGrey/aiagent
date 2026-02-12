import os
from dotenv import load_dotenv
from google import genai
import argparse
from google.genai import types



parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()
# Now we can access `args.user_prompt`

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
if api_key is None:
    raise RuntimeError("API Key not found")

client = genai.Client(api_key=api_key)
contents = args.user_prompt #"Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
response = client.models.generate_content(
    model='gemini-2.5-flash', contents=messages
)
prompt_available = response.usage_metadata.prompt_token_count
response_token = response.usage_metadata.candidates_token_count
if args.verbose == True:
    print(f"User prompt: {contents}")
    print(f"Prompt tokens: {prompt_available}")
    print(f"Response tokens: {response_token}")
print(f"Response: {response.text}")

