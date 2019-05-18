
# generator [-50, -43, -36, -29, -22, -15, -8, -1, 6, 13, 20, 27, 34]
items = [x for x in range (-50,35,7)]


squared = list(map(lambda x: x**2, items))
print(squared)


tripled = map(lambda x:x**3, items)
map(lambda a:a+1, items)
print(list(tripled))