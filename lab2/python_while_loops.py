# ex_1
i = 1
while i < 6:
    print(i)
    i += 1


# ex_2
i = 1
while i < 6:
    if i == 3:
        break
    i += 1


# ex_3
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)


# ex_4
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")
