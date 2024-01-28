import re


string = input("Input your string: ")
print(re.sub("_([a-z])", lambda x: x.group(1).upper(), string))
