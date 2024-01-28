import re


string = input("Input your string: ")
print(re.sub("([A-Z])", lambda x: "_" + x.group(1).lower(), string))
