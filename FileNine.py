# enter three exam scores
# exam pass score is equal to  40 or greater
# at least two exams must be passed
# the average should be 50 and up

j = 0
score_list = []
while True:
    try:
        score1 = int(input(" Enter Your first score"))
    except ValueError:
        print("Ooops, not valid, reenter please ")
        continue
    score_list.append(score1)
    break
while True:
    try:
        score2 = int(input(" Enter second score please"))
    except ValueError:
        print("Ooops, not valid, reenter")
        continue
    score_list.append(score2)
    break
while True:
    try:
        score3 = int(input(" Enter third score"))
    except ValueError:
        print("Ooops, not valid, reenter")
        continue
    score_list.append(score3)
    break
for i in range(3):
    if score_list[i] < 40:
        j += 1
if j <= 1 and sum(score_list) / 3 >= 50:
    print("Passed!")
else:
    print("Failed......")
