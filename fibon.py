def fibon(start):
    a = 1
    b = 1
    for i in range(start,100):
        yield a
        a,b = b,a+b


for i in fibon(5):
    print(i)