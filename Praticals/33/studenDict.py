
# Q.2 Create a dictionary consisting of student’s name as Key and student’s marks as Values
# (store 10 elements for this question). Perform the following operations on dictionary:

# a. Calculate the sum of all the values in the dictionary
# b. Display all the values where student’ marks is greater than 50
# c. Display all the Keys where student name begins with letter ‘A’ or ‘S’.
# d. Create a function to display marks i.e. dictionary value for a given key
# e. Create a function that asks for a student name to remove. It the student exists
# in the dictionary then remove it otherwise print the message ‘student doesn’t
# exist’.

stud_marks = {
  "pawan": 98,
  "hamja": 96,
  "saty": 74,
  "ashihs": 63,
  "mukesh": 19,
  "salman": 77,
  "prakhar": 37,
  "shikhar": 22,
  "sanju": 54
}

sum = 0
# A. Calculate the sum of all the values in the dictionary
print("________________________________")
for key in stud_marks:
  sum += stud_marks[key]
print("sum is ", sum, " \n")

# B Display all the values where student’ marks is greater than 50
print("______________________________\n")
for key in stud_marks:
  if (stud_marks[key] > 50):
    print(key, " ", stud_marks[key])

print("_______________________________\n")
# C Display all the Keys where student name begins with letter ‘A’ or ‘S’.
for key in stud_marks:
  if (key[0] == "a" or key[0] == "s"):
    print(key)


def displayMarks(key):
  for ans in stud_marks:
    if (ans == key):
      print(f"marks of {key} is ", stud_marks[key])


# D Create a function to display marks i.e. dictionary value for a given key
print("_______________________________\n")
displayMarks("saty")

# E Create a function that asks for a student name to remove. It the student exists in the dictionary then remove it otherwise print the message ‘student doesn’t exist’.
print("_______________________________\n")


def deleteStudent(name):
  done = False
  for key in stud_marks:
    if (key == name):
      stud_marks.pop(name)
      done = True
      print("student deleted")
      break
  if (done == False):
    print("student doesn’t exist")


deleteStudent("suraj")
print(stud_marks)
