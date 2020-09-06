# Input two numbers and test if
# they are divisible by the other one

test1_count = 0
test2_count = 0
while test1_count < 1:
    try:
        test1 = int(input("Enter the first number:"))
    except ValueError:
        print("Ooops, not a valid one")
        continue
    test1_count += 1
while test2_count < 1:
    try:
        test2 = int(input(" Enter the second number:"))
    except ValueError:
        print("Ooops, not valid")
        continue
    test2_count += 1
if test1 % test2 == 0 or test2 % test1 == 0:
    print(" they are divisible and value is 1")
else:
    print("not divisible, value is 0")
