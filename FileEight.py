# Enter just three numbers
# sort them all  in ascending order

i = 1
flist = []
while i < 4:
    try:
        num = int(input("Enter the  current number"))
    except ValueError:
        print(" not a valid number")
        continue
    flist.append(num)
    i += 1
flist.sort()
j = 0
while j < 3:
    print(f" {flist[j]}  ", end="")
    j += 1

