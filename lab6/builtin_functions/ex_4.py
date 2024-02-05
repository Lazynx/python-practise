from time import sleep
from math import sqrt


num = int(input())
sec = int(input()) / 1000
sleep(sec)
root = sqrt(num)
print(f"Square root of {num} after {int(sec * 1000)} milliseconds is {root}")
