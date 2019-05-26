
def fun1(x):
    return x+x

def fun2(x):
    return x**2

funcs = [fun1, fun2]    # list of functions to be applied bellow in lambda

for i in range(10):
    x = list(map(lambda x:x(i), funcs))
    print(x)