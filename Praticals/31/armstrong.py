# Q.1 Write a program to print all Armstrong number in a given range.

start = int(input("Enter start value : "))
end = int(input("Enter end value : "))

for num in range(start, end + 1):
  sum = 0

  temp = num

  while (temp > 0):
    digit = temp % 10
    sum = sum + digit**3
    temp = temp // 10
  if (sum == num):
    print(sum)
