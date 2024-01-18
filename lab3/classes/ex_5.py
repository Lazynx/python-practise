from math import sqrt

my_list = [i for i in range(1, 100)]

for i in range(1, len(my_list) + 1, 2):
    new_list = list(filter(lambda x: x % i or x == i, my_list))

for i in new_list:
    print(i)
