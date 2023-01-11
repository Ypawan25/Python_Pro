# progam to generate diffrenet file for diffrenet tables

for i in range(1, 21):
  with open(f"table/multiple_of_{i}", 'w') as f:
    for j in range(1, 11):    
      f.write(f"{i} X {j} = {i*j} \n")
  print("done table of ", i)
