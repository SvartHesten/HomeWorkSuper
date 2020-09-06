# get average of five numbers
# do not use arrays

i = 1
total = 0
while i < 6:
    try:
        number = float(input(" Enter current number:"))
    except ValueError:
        print(f" Not valid,  {i - 1} real numbers entered")
        continue
    total += number
    i += 1
average = total / 5
print(average)

