# limit ai to these things
import os 
import sys

working_directory = "/home/hexcore_linux_ui/workspace/ai-gent/ask-nicely"

print("hello from get files info.py")

print(f"this is working directory; {working_directory}")
print(f"this is current directory: {os.getcwd()}")
print("lets get started . . . ")

def get_files_info(working_directory, directory="."):
    abs_directory = os.path.abspath(directory)
    
    if working_directory not in abs_directory:
        return print(f'Error: Cannot list "{directory}" is outside permitted space.')
        

get_files_info(working_directory)