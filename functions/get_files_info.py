# limit ai to these things
import os 
import sys

working_directory = os.getcwd()
<<<<<<< HEAD
=======
directory = 

print("hello from get files.py")
print(f"checking path; {working_directory}")
print(f"checking directory; {directory}")

def get_files_info(working_directory, directory="."):
    log_text = print(f"{os.path.join(working_directory, directory)}")
>>>>>>> 1e009f2ebc7a10b09ff993295a3b616dc16cd3ca

print("hello from get files info.py")
print(f"checking path; {working_directory}")

def get_files_info(working_directory, directory="."):
    log_text = print(f"{os.path.abspath(directory)}")
    
    return log_text


if __name__ = "get_files_info":
    get_files_info(working_directory, directory=".")