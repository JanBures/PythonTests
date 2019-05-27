l = ["a","b","c","d","b","d","f","e","f"]
#m = ["z","b","n","t","e"]


duplicates = set()

for i in l:
    if l.count(i) > 1:
        duplicates.add(i)

print(duplicates)



duplicates2 = set(x for x in l if l.count(x) > 1)
print(duplicates2)