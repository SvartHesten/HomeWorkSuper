# Enter a number
# find difference between biggest and smallest digits

number_count = 0
while number_count < 1:
    number_str = input("Enter the  number please")
    try:
        number = int(number_str)
    except ValueError:
        print("this is  not a valid number")
        continue
    number_count += 1
    print(f"the number count is equal to  {number_count}")
if len(number_str) == 1:
    print("no minimums or maximums, only one digit")
else:
    number_list = list(number_str)
    print(number_list)
    maxi = number_list[0]
    for i in range(1, len(number_list)):
        if number_list[i] >= maxi:
            maxi = number_list[i]
    print(f" the maximum is {maxi} ")
    mini = number_list[0]
    for i in range(1, len(number_list)):
        if number_list[i] <= mini:
            mini = number_list[i]
    print(f" the minimum is equal to  {mini} ")
    maxim = int(maxi)
    minim = int(mini)
    print(f" and the difference is equal to { maxim - minim}")
