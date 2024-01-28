import re


string = input("Input your string: ")
print(re.findall("[a-z]+_", string))
