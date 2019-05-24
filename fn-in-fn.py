def calcul(func,a,b):
    """
    example of func in func like bellow, only difference is this func returns result instead of func itself
    :param func: string "add" or "sub"
    :param a: numeric value
    :param b: numeric value
    :return: numeric result based on chosen func
    """
    def add(a,b):
        return a+b

    def sub(a,b):
        return a-b

    if func == "sub":
        return sub(a,b)
    else:
        return add(a,b)


result_add = calcul("add", 5, 2)
print(result_add)

result_sub = calcul("sub", 5, 2)
print(result_sub)


def domath(func):
    """
    example of func inside of func
    :param func: "add" or "sub" = name of operation
    :return: function with two numeric parameters
    """
    def add(a, b):
        return a + b

    def sub(a, b):
        return a - b

    if func == "add":
        return add
    elif func == "sub":
        return sub



a = domath("add")
print(a(5,2))

m = domath("sub")
print(m(5,2))