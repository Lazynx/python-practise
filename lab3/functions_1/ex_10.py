def unique_el(nums):
    unique = []
    for i in nums:
        if i not in unique:
            unique.append(i)
    return unique


print(unique_el([1, 1, 2, 3, 1, 6, 6, 1, 9]))
