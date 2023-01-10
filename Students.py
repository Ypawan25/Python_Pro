# Write a Python program asking user to enter marks obtained by a student in five subjects
# (raise an error if entered marks is not between the range 0 to 100) and calculate:
# a. Total marks obtained
# b. Average marks obtained
# c. Grade of student based on average marks
# i. If average is greater than equal to 85, assign grade A+
# ii. If average is greater than equal to 70 and less than 85, assign grade A
# iii. If average is greater than equal to 55 and less than 70, assign grade B
# iv. If average is greater than equal to 40 and less than 55, assign grade C
# v. If average is less than 40, assign grade D
# Also display the assigned grade.

totalmark = 0
for i in range(5):
  print("Enter marks of subject ", i + 1)
  mrk = int(input())
  if (mrk > 100 and mrk < 0):
    raise ValueError("please enter the value in range")
  else:
    totalmark = totalmark + mrk

avg = totalmark / 5

if (avg >= 85):
  grade = "A+"
elif (avg >= 70 and avg < 85):
  grade = "A"
elif (avg >= 55 and avg < 70):
  grade = "B"
elif (avg >= 40 and avg < 55):
  grade = "C"
else:
  grade = "D"

print("Grade Assign to this student is ", grade)
