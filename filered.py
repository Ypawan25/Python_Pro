with open("text.txt") as f:
  data = f.read()
  if(data.__contains__("rain")):
    print("Yes")
  else:
   print("No")