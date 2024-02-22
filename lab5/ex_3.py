import re


with open("row.txt", "r", encoding="UTF-8") as file:
    lines = file.readlines()
    for i_line in lines:
        stripped_line = i_line.strip()
        print(re.findall("[a-z]+_", stripped_line))
