def square(num):
    for i in range(num + 1):
        yield i ** 2


x = square(5)
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
