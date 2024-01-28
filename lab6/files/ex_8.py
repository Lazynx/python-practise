import os


path = os.getcwd() + "/test2.txt"

if os.path.exists(path):
    if os.access(path, os.W_OK):
        os.remove(path)
