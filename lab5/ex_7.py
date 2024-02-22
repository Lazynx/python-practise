import re


with open("row.txt", "r", encoding="UTF-8") as file:
    lines = file.readlines()
    for i_line in lines:
        stripped_line = i_line.strip()
        print(re.sub("_([a-z])", lambda x: x.group(1).upper(), stripped_line))
