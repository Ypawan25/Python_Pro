# Q.3 Write a program to find mean of values in the dictionary? For Example: Input : test_dict =
# {“Sachin” : 5, “is” : 4, “Best” : 4, “Player” : 3, “India”:4}
# then the mean of the values is 4 as output

test_dict = {"Sachin" : 10, "is" : 8, "Best" : 4, "Player" : 3, "India":4 , "and" :80}
sum = 0
count =0
for key in test_dict:
  sum += test_dict[key]
  count = count+1
  

print(sum/count)