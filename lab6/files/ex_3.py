import os


def check_path(path):
    if os.path.exists(path):
        print(f"The path '{path}' exists.")

        directory, filename = os.path.split(path)

        print(f"Directory: {directory}\n"
              f"Filename: {filename}")
    else:
        print(f"The path '{path}' does not exist.")


path1 = os.getcwd() + "/ex_1.py"
path2 = "/home/user/Downloads/"

check_path(path1)
check_path(path2)
