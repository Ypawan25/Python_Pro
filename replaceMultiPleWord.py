# replacing word in file

list = ["star", "sky","how","the"]
with open("text.txt") as f:
  data = f.read()
  print(data)
  for lis in list:
   data = data.replace(lis, "#######")
with open("text.txt",'w') as file:  
  print(data, "********\n")
  file.write(data)
  print("done")
