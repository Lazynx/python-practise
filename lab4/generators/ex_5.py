def gen(num):
    for i_num in range(num, -1, -1):
        yield i_num


x = gen(10)
for i in x:
    print(i)
