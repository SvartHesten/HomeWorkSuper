# Enter a number
# reverse first and last digits
# print resulting number

while True:
    try:
        number = int(input("Enter number please"))
    except ValueError:
        print("not a valid number")
        continue
    number_str = str(number)
    print(number_str)
    break
if len(number_str) > 1 and number_str[len(number_str) - 1] != "0":
    str_list = list(number_str)
    str_list[0], str_list[len(str_list) - 1] = str_list[len(str_list) - 1], str_list[0]
    new_num_str = "".join(str_list)
    for i in range(len(new_num_str)):
        print(new_num_str[i], end="")
else:
    print(number_str)
