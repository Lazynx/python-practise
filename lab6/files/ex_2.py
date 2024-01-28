import os


path = os.getcwd()


print(f"Path existence: {os.access(path, os.F_OK)}\n"
      f"File reading: {os.access(path, os.R_OK)}\n"
      f"File writing: {os.access(path, os.W_OK)}\n"
      f"Path executability: {os.access(path, os.X_OK)}")
