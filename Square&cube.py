# Q.1 Create a list variable L and ask the user to input 10 integer elements into the list. Then
# iterate over complete list using loop to calculate:
# a. Square of elements of list L having even index and store it in a new list L2
# b. Cube of elements of list L having odd index and store it in a new list L3

L = []
L2 = []
L3 = []
for i in range(10):
  print("Enter number ", i + 1)
  num = int(input())
  L.append(num)

print(L)
for index, num in enumerate(L):
  if (index % 2 == 0):
    L2.append(num * num)
  else:
    L3.append(num**3)

print(L2)
print(L3)
