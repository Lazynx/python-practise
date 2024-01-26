def even_nums(num):
    for i in range(num + 1):
        if i % 2 == 0:
            yield i


x = even_nums(10)
print(', '.join(map(str, x)))
