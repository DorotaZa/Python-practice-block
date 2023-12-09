#getting the highest score without using the max function

print("Enter a list of student scores:")
student_scores = input().split()
for n in range(0, len(student_scores)): #without +1, because range() doesnt't include the the end range number
    student_scores[n] = int(student_scores[n])

max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score

print(f"The highest score of {student_scores} score list is: {max_score} ")