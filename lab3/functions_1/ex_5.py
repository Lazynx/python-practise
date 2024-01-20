from itertools import permutations


def permutation(string):
    perms = permutations(string)

    for i_perm in perms:
        print("".join(i_perm))


if __name__ == "__main__":
    permutation("test")
