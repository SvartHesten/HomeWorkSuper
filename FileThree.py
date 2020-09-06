# based ot two angles of a triangle
# calculate the third angle

angle1_count = 0
angle2_count = 0
while angle1_count < 1:
    try:
        angle1 = float(input("Enter first angle:"))
    except ValueError:
        print("Ախպեր, սխալ է")
        continue
    angle1_count += 1
while angle2_count < 1:
    try:
        angle2 = float(input("Enter second angle"))
    except ValueError:
        print("Непорядок дружок, некорректный ввод, так не пойдет")
        continue
    angle2_count += 1
if (angle1 > 0 and angle2 > 0) and (angle1 + angle2 < 180):
    print(f" The third angle is equal to: { 180 -angle1 - angle2}")
else:
    print(" These are not valid angles for triangle")
