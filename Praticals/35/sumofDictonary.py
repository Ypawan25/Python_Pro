# Write a python program to combine two dictionaries by adding values for common
# keys for example,
# D1 = {‘a’:100, ‘b’:200, ‘c’:300}
# D2 = {‘a’:300, ‘b’:200, ‘c’:400}
# Combined dictionary is { ‘a’ : 400, ‘b’ : 400, ‘c’ : 700}

D1 = {"a":100, "b":200, "c":300}
D2 = {"a":300, "b":200, "c":400}
D3 ={}

for key in D1:
  D1[key] += D2[key]

print(D1)  
