def gen(num):
    for i_num in range(num + 1):
        if i_num % 4 == 0 and i_num % 3 == 0:
            yield i_num


x = gen(100)
for i in x:
    print(i)
