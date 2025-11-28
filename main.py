import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from AiCodeAgent.functions.functions.get_files_info import get_files_info # from  dir.name_of_file import func_name

def main():

    load_dotenv()
    API_KEY = os.getenv("GEMINI_API_KEY")

    client = genai.Client(
        api_key=API_KEY
    )

    # print(sys.argv) # argv[0] - main.py

    if len(sys.argv) < 2:
        print("I need a prompt")
        sys.exit(1)
    verbose_flag = False
    if len(sys.argv) == 3 and sys.argv[2] == "--verbose":
        verbose_flag = True
    prompt = sys.argv[1]

    result = get_files_info("./", "calculator")
    print(result)
    # messages = [
    #     types.Content(role="user", parts=[types.Part(text=prompt)])
    # ]

    # response = client.models.generate_content(
    #     model="gemini-2.5-flash", contents=messages
    # )

    # print(response.text)

    # if verbose_flag:
        # print("prompt token:",response.usage_metadata.prompt_token_count) # get the no of tokens used in prompting
        # print("response token:",response.usage_metadata.candidates_token_count) # get the no of tokens in response

main()