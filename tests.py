# from AiCodeAgent.functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

def main():
    # print(get_file_content("calculator", "main.py"))
    # print("\n\n")
    # print(get_file_content("calculator", "pkg/calculator.py"))
    # print("\n\n")
    # print(get_file_content("calculator", "/bin/cat"))
    # print("\n\n")
    # print(get_file_content("calculator", "pkg/does_not_exist.py"))
    print(get_file_content("calculator", "lorem.txt"))

main()