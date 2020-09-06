# Find sign of product of three numbers.
# Do not use multiplication.
# display that sign.

zero_count = 0
number_count = 0
sign_count = 0
while number_count < 3:
    num_str = input("Enter current number")
    try:
        num = int(num_str)
    except ValueError:
        print("Ooops, not valid")
        continue
    number_count += 1
    if "-" in num_str:
        sign_count += 1
    if num == 0:
        zero_count += 1
if zero_count == 0:
    if sign_count % 2 ==0:
        print("+")
    if sign_count % 2 != 0:
        print("-")
else:
    print("unsigned")



