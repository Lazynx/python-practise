string = input("Input your string: ")

upper = sum(1 for i in string if i.isupper())
lower = sum(1 for i in string if i.lower())

print(f"Upper case letters: {upper}, lower case letters: {lower}")
