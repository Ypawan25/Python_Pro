# Q.3 Write a program to copy a file into another file?

file = open("first.txt","r")

data = file.read()
file.close()

f = open("second.txt","w")
f.write(data)
f.close()