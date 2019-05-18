from itertools import *

from PythonTests.human import human
from PythonTests.file_handler import *
from PythonTests.regexp import *
from PythonTests.generators import *


#Lukas = human("Lukášovec")
#Lukas.rozeberJmeno()
#Lukas.pridej_dite("Pavlík")
#Lukas.maDeti()

f = Filehandler("maily.txt")
print("počet mailů v souboru je:", f.get_mail_count(),".")
h = Regexp()
#h.print_mails(f.get_file_content())

a = [("a",1,2),("b",1,5),("c",2,4)]

print()
for fld in a:
    print(fld)
    for subfld in fld:
        print(subfld)


it = iter(a)
print("iterace:", it.__next__())


g =  Generator()
for l in g.generate_alphabet():
    print(l)


d = {"k":155,"v":"help","y":"yes"}
print(d["k"])


for i in g.generate_odds():
    print(i)


o = g.get_odds(1, 10)
print("g.get_odds(1, 10):\n", o)

trojky = [i*3 for i in range(10)]
print("[i**3 for i in range(10)]:\n", trojky)

# vygeneruje čísla 0,1,8,27,64 až 729
# range spustí cykl 100x. i se umocní třetí odm. a všechny čísla nižší 1000 se uloží
petky = [i**3 for i in range(100) if i**3 < 1000]
print(petky)

# 5 az 9 nasobeno 12
x = [n*12 for n in range(5,10)]
print(x)


# zip
jmena=["Pavel","Lukáš","Robert"]
cisla=[2,4,6]
z=dict(zip(cisla,jmena))
print(z)


cisla = [5,10,33,55]

def double(c):
    return c*2






def incr(x):
    return x+5

def decr(x):
    return x-5

funcs=[incr,decr]
for i in items:
    val = map(lambda x:x(i), funcs)
    print(list(val))






