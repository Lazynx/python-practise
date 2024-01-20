def filter_prime(nums: list):
    new_list = []
    for i in nums:
        if i < 2:
            continue
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            new_list.append(i)

    return new_list


my_list = [i for i in range(100)]
print(filter_prime(my_list))
