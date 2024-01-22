def generate_permutations(string, current=""):
    if not string:
        print(current)
    else:
        for i in range(len(string)):
            remaining_chars = string[:i] + string[i + 1:]
            generate_permutations(remaining_chars, current + string[i])


if __name__ == "__main__":
    generate_permutations("test")
