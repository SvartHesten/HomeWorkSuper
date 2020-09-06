# input an integer and then calculate the sum
# n + nn + nnn

number_count = 0
while number_count < 1:
    number_string = input("Enter the positive integer value")
    try:
        number = int(number_string)
    except ValueError:
        print(" O o ops, not a valid number")
        continue
    number_count += 1
if number > 0:
    number1 = number * (10 ** len(number_string)) + number
    number2 = number * (100 ** len(number_string)) + number *(10 ** len(number_string)) + number
    print(f" Result equal to: {number + number1 + number2 }")
else:
    print(" next time enter a positive number")
