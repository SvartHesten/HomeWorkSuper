# Input 3 numbers a, b, c
# A is non-zero. Write a program to solve quadratic equations.
#  may use math pow and sqrt

from math import sqrt

a_count = 0
b_count = 0
c_count = 0
while a_count == 0:
    try:
        a = int(input("Enter first number"))
    except ValueError:
        print("not a valid number")
        continue
    a_count += 1
while b_count == 0:
    try:
        b = int(input("Enter second number"))
    except ValueError:
        print(" not a valid number")
        continue
    b_count += 1
while c_count == 0:
    try:
        c = int(input("Enter third number"))
    except ValueError:
        print("not a valid number")
        continue
    c_count += 1
if a == 0:
    print("Enter valid condition")
elif (b * b - 4 * a * c) < 0:
    print(" solution does not exist")
else:
    solution1 = (- b + sqrt((b * b) - (4 * a * c))) / (2 * a)
    solution2 = (- b - sqrt((b * b) - (4 * a * c))) / (2 * a)
    if solution1 == solution2:
        print(f"solution is {solution1}")
    else:
        print(f" solutions are {solution1} and {solution2}")



