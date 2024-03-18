import re

string = "The Golf Is The King Of Spots"

match = re.findall("[A-Z]", string)

with open("letters.txt", "w") as file:
    for i in range(len(match)):
        if i + 1 != len(match):
            file.write(match[i] + "\n")
        else:
            file.write(match[i])

# print(len(match))

