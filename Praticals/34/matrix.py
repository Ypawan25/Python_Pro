# Q.2 Create a numpy array having two dimensions and shape (3,3) and perform the following operations on array elements:

# a. Calculate sum of all the columns of the array.
# b. Calculate product of all the rows of the array.
# c. Retrieve only the last two columns and last two rows from the array.
# d. Create another two dimensional array having same shape and carry out element
# wise addition of two arrays and display the result.
# e. Create a new array by multiplying every element of original array with value 2
# and display the new array
import numpy as np

mat = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

for i in range(3):
  pro = 1
  sum = 0
  for j in range(3):
    pro = pro * mat[i][j]
    sum = sum + mat[i][j]
  print(f"prduct of {i} row is {pro}")
  print(f"sum of {i} row is {sum}")
  print("**************************************")

for i in range(3):
  pro = 1
  sum = 0
  for j in range(3):
    pro = pro * mat[j][i]
    sum = sum + mat[j][i]
  print(f"prduct of {i} col is {pro}")
  print(f"sum of {i} col is {sum}")
  print("**************************************")

print("Last two row of matrix")
for i in range(3):
  if(i!=0):
    print(mat[i])

print("Last two col of matrix")
for i in range(3):
  li=[]
  for j in range(3):
    if(j!=2):
      li.append(mat[i][j])
  print(li)   