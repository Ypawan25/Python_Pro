# Q.1 Create a list variable L and ask the user to input 10 integer elements into the list. Then
# iterate over complete list using loop to calculate:
# a. Square of elements of list L having even index and store it in a new list L2
# b. Cube of elements of list L having odd index and store it in a new list L3

L = [1,2,3,4,5,6,7,8,9,10]
for i in range(10):
  L.append(int(input("enter the number")))

print(L)
L2=[]

for index, num in enumerate(L):
  if(index%2==0):
    L2.append(num*num)
  else:
    L2.append(num*num*num)

print(L2)
