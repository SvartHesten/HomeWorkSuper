# input a number, test if it is odd or even

name = input(" What is Your name, my friend? ")
while True:
    try:
        test_number = int(input(f" Dear {name}, please enter the number to test"))
    except ValueError:
        print("Ooops, not a valid entry......")
        continue
    if test_number % 2 == 0:
        print(f" {name}, the given  number {test_number} is even ")
        break
    elif test_number % 2 != 0:
        print(f" {name}, the given  number {test_number} is odd")
        break
print(" Have a great day!")


