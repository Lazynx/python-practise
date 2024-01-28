from functools import reduce


my_list = [i for i in range(1, 11)]
print(reduce(lambda prev_el, el: prev_el * el, my_list))
