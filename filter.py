
#[-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
cisla = [x for x in range(-10,10)]
#vytiskni cisla
print(cisla)


"""
filtr 
"""
# odfiltrujce čísla větší než 0
f = list(filter(lambda x:x<0, cisla))

print(f)
