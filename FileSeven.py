# enter a number, test if multiple of 3, 5, 7
# output appropriate message

number_count = 0
str0 = "is"
str3 = " multiple of  3"
str5 = " multiple of 5"
str7 = " multiple of 7 "
while number_count < 1:
    try:
        number = int(input(" Enter the number:"))
    except ValueError:
        print(" Not a valid one")
        continue
    number_count += 1
if number % 3 != 0 and number % 5 != 0 and number % 7 != 0:
    print(f" {number} is not divisible by any ")
else:
    if number % 3 == 0:
        str0 += str3
    if number % 5 == 0:
        str0 += str5
    if number % 7 == 0:
        str0 += str7
    print(f"{number}   " + str0)

