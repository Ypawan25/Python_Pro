
# #sum of two numbers

# def sum(x,y):
#     print("sum is ",x+y)
# a = 10
# b=23

# sum(a,b)
sum = 0
def average(*nums):
    sum =0
    for num in nums:
        sum= sum+num
    avg = sum/len(nums)
    return avg


x = average(1,2,3,4)

print(x)
