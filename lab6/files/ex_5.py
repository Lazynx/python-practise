with open("test1.txt", "a") as file:
    my_list = [i for i in range(10)]
    file.write(str(my_list))
