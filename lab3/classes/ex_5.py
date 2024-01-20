my_list = [i for i in range(1, 100)]
new_list = list(filter(lambda x: all(x % i != 0 for i in range(2, int(x**0.5) + 1)) if x > 1 else False, my_list))

print(new_list)
