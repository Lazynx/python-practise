string = input("Input your string: ")
if string == ''.join(reversed(string)):
    print(f"Your string: {string} is a palindrome")
else:
    print(f"Your string: {string} is not a palindrome")
