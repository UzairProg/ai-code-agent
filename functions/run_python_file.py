import os
import subprocess

def run_python_file(working_directory, file_path: str, args=[]):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(abs_working_dir, file_path))

    print(abs_file_path, abs_working_dir)

    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(abs_file_path):
        return f'Error: File "{file_path}" not found.'
    
    if not abs_file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        # Build the command: python <file> <args>
        cmd = ["python", abs_file_path] + [str(a) for a in args]
        result = subprocess.run(
            cmd,
            cwd=abs_working_dir,
            timeout=30,
            capture_output=True,
            text=True  # return strings instead of bytes
        )

        stdout = result.stdout.strip()
        stderr = result.stderr.strip()

        final_str = "STDOUT:\n" + (stdout if stdout else "<empty>") + "\n\n" + "STDERR:\n" + (stderr if stderr else "<empty>") + "\n"

        if result.returncode != 0:
            final_str += f"\nExit Code: {result.returncode}"

        return final_str
    except Exception as e:
        return f'Error: Can\'t run the python file: "{file_path}" - {e}'