import re


string = input("Input your string: ")
print(re.findall("[A-Z][a-z]+", string))
