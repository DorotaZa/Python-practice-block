print("Enter the list of student heights: ")
student_heights = input().split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n]) #list of strings conversion into int
    #print(student_heights[n])

#print(student_heights)

total_height = 0
for height in student_heights:
    total_height += height
print(f"Total height of {student_heights} = {total_height}")


total_number = 0
for num in student_heights:
    total_number += 1
print(f"Total number of students = {total_number}")

average_height = round(total_height/total_number)
print(f"Average height of {total_number} = {average_height}")
