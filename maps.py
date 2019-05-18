from copy import deepcopy

# [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]
l = [x for x in range (1,15,2)]
lenum = [x for x in enumerate(l)]

print("máme list:\n", lenum)

d = dict(lenum)
print("převedený na slovník:\n",d)

print(lenum.extend(lenum))
print(lenum)


start=0
lenum_new = []
#přečíslování seznamu
for i,y in lenum:
    print(i,y)
    lenum_new.append([start,y])
    start+=1

print(lenum_new)


x = deepcopy(l)
print(lenum_new)

isinstance()