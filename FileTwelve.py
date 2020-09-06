# Input a digit and a number.
# Check whether the digit is contained in that number.

digit_count = 0
number_count = 0
while digit_count < 1:
    digit_str = input("Enter the digit")
    if len(digit_str) != 1:
        print(" one digit only and a valid number!!!")
        continue
    try:
        digit = int(digit_str)
    except ValueError:
        print(" not a valid number")
        continue
    digit_count += 1
while number_count < 1:
    number_str = input("Enter the number")
    try:
        number = int(number_str)
    except ValueError:
        print(" not a valid number")
        continue
    number_count += 1
if digit_str in number_str:
    print("YESSS")
else:
    print("Nooooo")