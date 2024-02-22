import re


with open("row.txt", "r", encoding="UTF-8") as file:
    lines = file.readlines()
    for i_line in lines:
        stripped_line = i_line.strip()
        print(re.sub("([A-ZА-Я])", lambda x: (" " if x.start() != 0 else "") + x.group(1), stripped_line))
