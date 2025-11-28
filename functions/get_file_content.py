import os
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(abs_working_dir, file_path))

    print(abs_working_dir, abs_file_path)

    if file_path == "" or file_path == None:
        return f'"{file_path}" is not a valid file path'
    
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(abs_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    if not os.path.isdir(abs_working_dir):
        return f'"{abs_working_dir} is not a dir'
    
    try:
        file_content_string = ""
        with open(abs_file_path, "r") as f:
            file_content_string = f.read()
            if len(file_content_string) > MAX_CHARS:
                file_content_string = file_content_string[:MAX_CHARS] 
                file_content_string += f'[...File "{file_path}" truncated at 10000 characters]'
    except Exception as e:
        return f"Exception Error: {e}"
    
    return file_content_string
        