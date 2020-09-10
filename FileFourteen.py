# Program to compute area of rectangle or triangle
# Should prompt to which figure  type to compute for
# area should definitely  be positive

height_count = 0
base_count = 0
length_count = 0
while True:
    message_str = input(" Enter whether rectangle or triangle please ")
    if message_str != "triangle" and message_str != "rectangle":
        print("Enter a valid choice")
        continue
    break
if message_str == "triangle":
    while height_count < 1:
        try:
            height = float(input("Enter the height"))
        except ValueError:
            print("not a valid number for height")
            continue
        height_count += 1
        print(f" height count is {height_count}")
    while base_count < 1:
        try:
            base = float(input("Enter the base"))
        except ValueError:
            print("not a valid number for base")
            continue
        base_count += 1
        print(f" base count is {base_count}")

    area = height * base / 2
    if area <= 0:
        print(" Area should be positive")
    else:
        print(" Area of " + message_str + f" equal to {area}")
if message_str == "rectangle":
    while height_count < 1:
        try:
            height = float(input("Enter the height"))
        except ValueError:
            print("not a valid number for height")
            continue
        height_count += 1
        print(f" height count is {height_count}")
        while length_count < 1:
            try:
                length = float(input("Enter the length"))
            except ValueError:
                print("not a valid number for length")
                continue
            length_count += 1
            print(f" length count is {length_count}")

    area = height * length
    if area <= 0:
        print("Area should be positive")
    else:
        print(" Area of our " + message_str + f" equal to {area}")





