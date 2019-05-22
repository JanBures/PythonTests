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

# same solution with sum() function
y = sum(nums)
print("sum function: ",y)


nums.append("abc")  # exception TypeError raise test
nums.append("def")  # exception TypeError raise test
nums.append("ghi")  # exception TypeError raise test

# same solution with function
def sumar(x):
    """
    Sumarize all items in list
    :param x: list with items to sumarize
    :return: int sumarized input parameter
    """
    suma = 0
    err_counter = 0
    for i in x:
        try:
            suma+=i
        except TypeError:   # if values are not numbers
            err_counter +=1
            continue
    print("počet chyb:", err_counter)
    return suma

print("same solution with function sumar():",sumar(nums))
