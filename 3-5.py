#input scores, get the average + total scores entered, total students
#unknown at first

studentNos = 0
sumMarks = 0

score=int(input("Score? not 0 to 100 to quit"))

while score>= 0 and score <= 100:
    studentNos += 1
    sumMarks += score
    score = int(input("Next? end if <0 or >100"))

print("%d students, average %.2f"%(studentNos, sumMarks/studentNos))
