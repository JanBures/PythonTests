def fibon(start,amount):
    """
    Fibonacci function
    :param start: sequence start
    :param amount: number of steps
    :return: generated next fibonacci number
    """
    a = start
    b = start
    for i in range(amount):
        yield a
        a,b = b,a+b


# start fibonacci from nubmer 5
for i in fibon(50,10):
    print(i)