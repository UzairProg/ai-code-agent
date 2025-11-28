import os

# - README.md: file_size=1032 bytes, is_dir=False
# - src: file_size=128 bytes, is_dir=True
# - package.json: file_size=1234 bytes, is_dir=False

'''
 here, we'll provide the working directory in which ai can scan.. 
 and the directory will be within the working directory
 so that the agent will be restricted only the the working directory that we provided.. and can't go else where

 os.path.abspath() - doesnt check if the path exists or not, it just converts the given path to absolute path

'''
def get_files_info(working_directory, directory="."):
    abs_working_directory = os.path.abspath(working_directory) # convert the given path to absolute path
    abs_directory = "" # if given a wrong path it will return that path as it is

    # print(working_directory, directory)
    # print("Absolute working directory:", abs_working_directory)
    # print("Absolute target directory:", abs_directory)

    if directory == "." or directory == "./" or directory == None:
        abs_directory = abs_working_directory
    else:
        abs_directory = os.path.abspath(os.path.join(abs_working_directory, directory))

    # print("Absolute target directory:", abs_directory)
    print(working_directory, directory)
    if not abs_directory.startswith(abs_working_directory):
        return (f'Error: Cannot list "{directory}" as it is outside the permitted working directory')

    if not os.path.exists(abs_working_directory): # making sure the path given really exists
        return f'Error: The working directory "{working_directory}" does not exist.'
    
    if not os.path.exists(abs_directory):
        return f'Error: The directory path "{directory}" does not exist.'
    
    # check if direactory is really a directory
    if not os.path.isdir(abs_directory):
        return f'Error: The file path "{directory}" is not a directory.'
    
    contents = os.listdir(abs_directory) #list all the directories in the given path
    # print("Contents:", contents)
    final_response = ""
    for content in contents:
        content_path = os.path.join(abs_directory, content)
        is_dir = os.path.isdir(content_path)
        file_size = os.path.getsize(content_path)
        final_response += f"{content} - file_size={file_size} bytes, is_dir={is_dir}\n"
    
    return final_response