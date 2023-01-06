# kbc program for playing KBC

ques = ["Who developed Python Programming Language? \n a) Wick van Rossum \n b) Rasmus Lerdorf \n c) Guido van Rossum \n d) Niene Stom",
       "Which type of Programming does Python support? \n a) object-oriented programming \n b) structured programming \n c) functional programming \n d) all of the mentioned",
       "Is Python case sensitive when dealing with identifiers? \n a) no \n b) yes \n c) machine dependent \n d) none of the mentioned",
       "Which of the following is the correct extension of the Python file? \n a) .python \n b) .pl \n c) .py \n d) .p",
       "Is Python code compiled or interpreted? \n a) Python code is both compiled and interpreted \n b) Python code is neither compiled nor interpreted \n c) Python code is only compiled \n d) Python code is only interpreted"]
           
solu = ["c","d","b","c","a"]
totalAmount =0
for i in range(len(ques)):
  print("Question ",i+1, " for amount of ",(i+1)*1000,"\n")
  print(ques[i],"\n")
  ans = input("Enter your answere  \n")
  if(ans==solu[i]):
    print("It's the correct answere you won Rs",(i+1)*1000," for this question \n")
    print("\n")
    totalAmount = totalAmount + (i+1)*1000
    if(i==len(ques)-1):
      print("Amazing You have given all the correct ans \n ")
      print("You have Won the game with Total Amount Rs ",totalAmount)
  else:
    print("Oh no... This is wrong answere")
    print("You won Total amount Rs",totalAmount)
    break
print("Thanks for playing. ")    
    
  
  
  


