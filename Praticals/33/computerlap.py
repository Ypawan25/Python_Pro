# Q.1 Write a python program to input day (Monday to Sunday) and time (HH format with AM/ PM) from the user. The Computer Lab in your institute is open only on‘Wednesday’ from 12 to 1 pm and ‘Friday’ from 10 to 11 am, then display the following
# message as output based on day & time entered by the user:
# a. ‘Computer Lab is open’
# b. ‘Computer Lab is closed’

day = input("Enter the day \n")
time = input("Enter time in hour with AM/PM \n")
if ((day == "monday") and (time == "12pm" or time == "1pm")
    or (day == "friday") and (time == "10am" or time == "11am")):
  print("Computer Lab is open")
else:
  print("Computer Lab is closed")
