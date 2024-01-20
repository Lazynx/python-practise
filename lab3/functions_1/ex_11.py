def is_pali(string):
    reversed_str = ""
    for i in reversed(range(len(string))):
        reversed_str += string[i]
    if reversed_str == string:
        return True
    else:
        return False


print(is_pali("aba"))
print(is_pali("abb"))
