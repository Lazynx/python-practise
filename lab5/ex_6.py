import re


string = input("Input your string: ")
print(re.sub("[ ,.]", ":", string))
