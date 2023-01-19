# Q.3 (i) Write a Python Program to display Fibonacci Sequence (first 20 terms) using
# Recursion.
# (ii) Write a Python Program to find factorial of a number using Recursion.


def factorial(n):
  if (n == 0):
    return 1
  if (n == 1):
    return 1
  else:
    return n* factorial(n - 1)


x = factorial(3)

print(x)


def fibonacy(n):
  if(n==1):
    return 1
  if(n==0):
    return 0
  else:
    return fibonacy(n-1)+fibonacy(n-2)


y = fibonacy(20)
print(y)
