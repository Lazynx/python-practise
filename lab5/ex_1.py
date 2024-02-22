import re


with open("row.txt", "r", encoding="UTF-8") as file:
    lines = file.readlines()
    for i_line in lines:
        stripped_line = i_line.strip()
        match = re.fullmatch("ab*", stripped_line)
        if match:
            print(f"Your string: {stripped_line} was matched")
        else:
            print(f"Your string: {stripped_line} wasn't matched")