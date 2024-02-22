# v = 0
# for i in range(5):
#     a = float(input())
#     v += a
# print(v/5)
arr = [1.81, 1.092, 3.91, 0.766]
arr1 = [0.04, 0.06, 0.04, 0.06]
for time, mass in zip(arr, arr1):
    print(mass*3.5/100*(9.81-(0.6/time**2)))
    vals = mass*3.5/100*(9.81-(0.6/time**2))

