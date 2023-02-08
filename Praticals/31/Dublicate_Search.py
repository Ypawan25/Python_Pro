# Q.3 (i) Write a Programme to check if an element exists in the list or not. If that element does not exist then add that particular element in the List.
# (ii) Write a Programme to check if there is a duplicate element Present in the list or not.
# If that is present in the list then remove it from the List.

list = [1,2,3,4,4,5,6,7,7]

s = set(list)
l=[]

num =int(input("Enter the number to check"))

if(num in list):
  print("Number is present")
else:
   print("Number is not present")
   list.append(num)
   print("List after adding the number")
   print(list)
if(len(s)==len(list)):
  print("List has no dublicates")
else:
  print("List has dublicate \n")
  print("List after removing dublicates is \n")
  for i in s:
    l.append(i)
print(l)  