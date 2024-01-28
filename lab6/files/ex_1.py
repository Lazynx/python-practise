import os


path = os.getcwd()
print(f"Directories: {[i_dir for i_dir in os.listdir(path) if os.path.isdir(i_dir)]}\n"
      f"Files: {[i_file for i_file in os.listdir(path) if os.path.isfile(i_file)]}\n"
      f"All: {os.listdir(path)}")
