# Q.1 Write a program to compute the wage of daily labour as per the following rules:
# a) For first 4 hrs. Rs 30/- per hr
# b) For next 4 hrs. Rs 40/- per hr
# c) For next 2 hrs. beyond 8 hrs. Rs 50/- per hr extra
# d) For rest Rs 60/- per hr extra

hour = int(input("Enter the hour for wages  "))

if (hour > 10):
  hour = hour - 10
  print("Wages is ", (hour * 60) + (4 * 30) + (4 * 40) + (2 * 50))
elif (hour > 8):
  hour = hour - 8
  print("Wages is ", (hour * 50) + (4 * 30) + (4 * 40))
elif (hour > 4):
  hour = hour - 4
  print("Wages is ", (hour * 40) + (4 * 30))
else:
  print("Wages is ", (hour * 30))
