def spy_game(nums):
    sequence = [0, 0, 7]
    idx = 0

    for i_num in nums:
        if i_num == sequence[idx]:
            idx += 1
            if idx == len(sequence):
                return True

    return False


print(spy_game([1, 2, 4, 0, 0, 7, 5]))
print(spy_game([1, 0, 2, 4, 0, 5, 7]))
print(spy_game([1, 7, 2, 0, 4, 5, 0]))
