# limit ai to these things
import os 
import sys

working_directory = os.getcwd()


print("hello from get files.py")
print(f"checking path; {working_directory}")


def get_files_info(working_directory, directory="."):
    log_text = print(f"{os.path.join(working_directory, directory)}")

    return log_text
