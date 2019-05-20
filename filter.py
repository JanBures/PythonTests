
#[-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
nums = [x for x in range(-10, 10)]
#print nums
print(nums)


"""
filter 
"""
# filter out nums <=0
f = list(filter(lambda x:x<=0, nums))
print(f)

# filter only even numbers
x = list(filter(lambda x: x % 2 == 0, nums))
print(x)


