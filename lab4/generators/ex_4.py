def squares(a_num, b_num):
    for i_num in range(a_num, b_num + 1):
        yield i_num ** 2


x = squares(0, 10)
for i in x:
    print(i)
    