import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Import all the tool functions
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.run_python_file import run_python_file
from functions.write_file import write_file

# Define the function declarations for Gemini
function_declarations = [
    {
        "name": "get_files_info",
        "description": "Lists all files and directories in a specified directory. Returns file sizes and whether each item is a directory.",
        "parameters": {
            "type": "object",
            "properties": {
                "working_directory": {
                    "type": "string",
                    "description": "The base working directory that restricts access"
                },
                "directory": {
                    "type": "string",
                    "description": "The target directory to list (relative to working_directory). Use '.' for current directory."
                }
            },
            "required": ["working_directory"]
        }
    },
    {
        "name": "get_file_content",
        "description": "Reads and returns the content of a file. Files are truncated at 10000 characters.",
        "parameters": {
            "type": "object",
            "properties": {
                "working_directory": {
                    "type": "string",
                    "description": "The base working directory"
                },
                "file_path": {
                    "type": "string",
                    "description": "Path to the file to read (relative to working_directory)"
                }
            },
            "required": ["working_directory", "file_path"]
        }
    },
    {
        "name": "run_python_file",
        "description": "Executes a Python file and returns its stdout, stderr, and exit code.",
        "parameters": {
            "type": "object",
            "properties": {
                "working_directory": {
                    "type": "string",
                    "description": "The base working directory"
                },
                "file_path": {
                    "type": "string",
                    "description": "Path to the Python file to execute"
                },
                "args": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "Command-line arguments to pass to the script"
                }
            },
            "required": ["working_directory", "file_path"]
        }
    },
    {
        "name": "write_file",
        "description": "Writes content to a file. Creates parent directories if they don't exist.",
        "parameters": {
            "type": "object",
            "properties": {
                "working_directory": {
                    "type": "string",
                    "description": "The base working directory"
                },
                "file_path": {
                    "type": "string",
                    "description": "Path where the file should be written"
                },
                "content": {
                    "type": "string",
                    "description": "The content to write to the file"
                }
            },
            "required": ["working_directory", "file_path", "content"]
        }
    }
]

# Map function names to actual Python functions
function_map = {
    "get_files_info": get_files_info,
    "get_file_content": get_file_content,
    "run_python_file": run_python_file,
    "write_file": write_file
}

def execute_function_call(function_call):
    """Execute a function call from Gemini and return the result"""
    function_name = function_call.name
    function_args = function_call.args
    
    if function_name not in function_map:
        return f"Error: Unknown function '{function_name}'"
    
    try:
        # Call the actual Python function with the provided arguments
        result = function_map[function_name](**function_args)
        return str(result)
    except Exception as e:
        return f"Error executing {function_name}: {str(e)}"

def main():
    load_dotenv()
    API_KEY = os.getenv("GEMINI_API_KEY")

    if len(sys.argv) < 3:
        print("Usage: python main.py <working_directory> <prompt> [--verbose]")
        print("Example: python main.py ./calculator 'List all Python files in this directory'")
        sys.exit(1)

    working_directory = sys.argv[1]
    prompt = sys.argv[2]
    verbose_flag = "--verbose" in sys.argv
    
    # Validate working directory exists
    if not os.path.exists(working_directory):
        print(f"Error: Working directory '{working_directory}' does not exist")
        sys.exit(1)
    
    if not os.path.isdir(working_directory):
        print(f"Error: '{working_directory}' is not a directory")
        sys.exit(1)
    
    # Initialize the Gemini client
    client = genai.Client(api_key=API_KEY)
    
    # Inject working directory context into the prompt
    system_message = f"""You are a helpful AI code assistant with access to tools.
You can ONLY access files within this working directory: {os.path.abspath(working_directory)}

IMPORTANT: For ALL function calls, you MUST use working_directory="{working_directory}"
Do not ask the user for the working_directory - it is always "{working_directory}"

Available tools:
- get_files_info: List files and directories
- get_file_content: Read file contents
- run_python_file: Execute Python scripts
- write_file: Create or modify files

User's request: {prompt}"""
    
    # Start the conversation with the user's prompt
    messages = [
        types.Content(
            role="user",
            parts=[types.Part(text=system_message)]
        )
    ]
    
    print(f"\n{'='*60}")
    print(f"WORKING DIRECTORY: {os.path.abspath(working_directory)}")
    print(f"USER: {prompt}")
    print(f"{'='*60}\n")
    
    # Conversation loop - handle function calls iteratively
    max_iterations = 10
    iteration = 0
    
    while iteration < max_iterations:
        iteration += 1
        
        # Generate response with function calling enabled
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=messages,
            config=types.GenerateContentConfig(
                tools=[types.Tool(function_declarations=function_declarations)]
            )
        )
        
        if verbose_flag:
            print(f"\n[Iteration {iteration}]")
            print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
            print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
        
        # Get the first candidate
        candidate = response.candidates[0]
        
        # Check if there are function calls
        function_calls = []
        for part in candidate.content.parts:
            if part.function_call:
                function_calls.append(part.function_call)
        
        if function_calls:
            # Execute all function calls
            print(f"\n[AI is calling {len(function_calls)} function(s)...]")
            
            function_responses = []
            for fc in function_calls:
                print(f"  → {fc.name}({dict(fc.args)})")
                result = execute_function_call(fc)
                
                if verbose_flag:
                    print(f"    Result: {result[:200]}..." if len(result) > 200 else f"    Result: {result}")
                
                function_responses.append(
                    types.Part(
                        function_response=types.FunctionResponse(
                            name=fc.name,
                            response={"result": result}
                        )
                    )
                )
            
            # Add the assistant's response (with function calls) to messages
            messages.append(candidate.content)
            
            # Add function responses to messages
            messages.append(
                types.Content(
                    role="user",
                    parts=function_responses
                )
            )
            
            # Continue the loop to get the next response
            continue
        
        else:
            # No function calls - we have a final text response
            if candidate.content.parts and candidate.content.parts[0].text:
                final_response = candidate.content.parts[0].text
                print(f"\n{'='*60}")
                print(f"AI RESPONSE:")
                print(f"{'='*60}")
                print(final_response)
                print(f"\n{'='*60}\n")
            else:
                print("\n[No response generated]")
            
            break
    
    if iteration >= max_iterations:
        print("\n[Warning: Maximum iterations reached]")

if __name__ == "__main__":
    main()