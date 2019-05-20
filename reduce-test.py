from functools import reduce
"""
Reduce is a really useful function for performing some computation 
on a list and returning the result. It applies a rolling computation 
to sequential pairs of values in a list. For example, if you wanted 
to compute the product of a list of integers.
"""

# list of nums [1, 10, 19, 28, 37, 46, 55, 64, 73, 82, 91]
nums = [x for x in range(1,100,9)]
print(nums)

# sum all list items
l = reduce((lambda x,y:x+y),nums)
print("reduce and lambda: ",l)

# same solution
y = sum(nums)
print("sum function: ",y)


# same solution with function
def sumar(x):
    """
    Sumarize all items in list
    :param x: list with items to sumarize
    :return: int sumarized parameter x
    """
    suma = 0
    for i in x:
        suma+=i
    return suma

print("same solution with function sumar():",sumar(nums))
