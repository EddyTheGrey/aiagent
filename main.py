import os
from dotenv import load_dotenv
from google import genai
import argparse
from google.genai import types
from prompts import system_prompt
from functions.call_function import available_functions
from functions.call_function import call_function


i =5


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
contents = args.user_prompt 
messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

for _ in range(i):
    function_responses = []
    response = client.models.generate_content(
    model='gemini-2.5-flash', contents=messages, config=types.GenerateContentConfig(tools=[available_functions],system_instruction=system_prompt, temperature=0)
    )
    prompt_available = response.usage_metadata.prompt_token_count
    response_token = response.usage_metadata.candidates_token_count
    
    #Memory Loop for Model
    for X in response.candidates:
        messages.append(X.content)
    if not response.function_calls:
        # No function calls - model is done
        print(response.text)
        break
    

    #Function Calls
    for fc in response.function_calls:
        print(fc)
        function_call_result = call_function(fc)
        function_responses.append(function_call_result.parts[0])


    #Check for empty responses
    if not function_call_result.parts:
        raise Exception("Call function is empty")
    if function_call_result.parts[0].function_response == None:
        raise Exception("Function response is None")
    if function_call_result.parts[0].function_response.response == None:
        raise Exception("Response is None")
    #Print Responses
    if args.verbose == True:
        print(f"User prompt: {contents}")
        print(f"Prompt tokens: {prompt_available}")
        print(f"Response tokens: {response_token}")


    #print (f"Calling function: {response.function_calls[0].name}({response.function_calls[0].args})")
    print(f"-> {function_call_result.parts[0].function_response.response["result"]}")

        
    messages.append(types.Content(role="user", parts=function_responses))
    if _ == i:
        SystemExit(1)
  