# replacing word in file
with open("text.txt") as f:
  data = f.read()
  print(data)
  data = data.replace("twinkle", "#######")
with open("text.txt",'w') as file:  
  print(data, "********")
  file.write(data)
  print("done")
