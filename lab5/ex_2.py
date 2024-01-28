import re


string = input("Input your string: ")
match = re.fullmatch("ab{2,3}", string)
if match:
    print(f"Your string: {string} was matched")
else:
    print(f"Your string: {string} wasn't matched")
