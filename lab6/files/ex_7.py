with open("test1.txt", "r") as reading_file:
    with open("test2.txt", "w") as written_file:
        for i_row in reading_file.readlines():
            written_file.write(i_row)
