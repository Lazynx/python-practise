import re


string = input("Input your string: ")
print(re.sub("([A-Z])", lambda x: " " + x.group(1), string))
