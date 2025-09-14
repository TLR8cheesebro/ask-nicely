# limit ai to these things
import os 
import sys

working_directory = os.getcwd()

print("hello from get files info.py")
print(f"checking path; {working_directory}")

def get_files_info(working_directory, directory="."):
    log_text = print(f"{os.path.abspath(directory)}")
    
    return log_text


if __name__ == "get_files_info":
    get_files_info(working_directory, directory=".")