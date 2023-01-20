# Q.2 Write a function that takes a string as parameter and returns a string with every successive repetitive character replaced by ‘!’
# Example: SCHOOL may become SCH!!L.


def stringfunction(str):
  dic = {}
  str1 = ""

  for i in str:
    if (i in dic):
      dic[i] += 1
    else:
      dic[i] = 1

  for key in dic:
    if (dic[key] == 1):
      str1 += key
    else:
      for i in range(dic[key]):
        str1 += "!"
  return str1


print(stringfunction("SCHOOOL"))
