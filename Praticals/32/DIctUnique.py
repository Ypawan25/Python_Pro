
# Q.2 Create a list variable L and ask the user to input 10 integer elements into the list. Write Python code to perform below given operations on the list (Do not use built-in list functions):
# a) Create a new list L1 by adding a number 10 to every element in the list L using list comprehension. Say L contains 5,15,25 then L1 contains 15,25,35
# b) Find total no. of positive and negative integers in the list
# c) Count the elements that are divisible by 5
# d) Remove the repetitive items from the list by storing all the unique elements in a new list.
# e) Create a new dictionary by counting the frequency of every element in the list.
# Store the list elements as keys of dictionary and their frequencies as the values.

L = [2, 2, 3, -4, -4, -6, -7, -8, 9, -4]
# for i in range(0, 10):
#   L.append(int(input("Enter numer ")))
print(L)

L1 = []
for i in L:
  L1.append(i + 10)
print(L1)

pos = 0
neg = 0

for i in L:
  if (i < 0):
    neg += 1
  else:
    pos += 1
print(f"Positive integer are {pos} and negative integer are {neg} \n")

print("Uniuque element in list \n")
set1 = set(L)
l = list(set1)
print(l)

dic = {}

for i in L:
  if (i in dic):
    dic[i] += 1
    
  else:
    dic[i] = 1
   

print(dic)
