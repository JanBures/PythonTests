from itertools import *

from human import human
from file_handler import *
from regexp import *
from generators import *


#Lukas = human("Lukášovec")
#Lukas.rozeberJmeno()
#Lukas.pridej_dite("Pavlík")
#Lukas.maDeti()

f = Filehandler("maily.txt")
print("počet mailů v souboru je:", f.get_mail_count(),".")
h = Regexp()
#h.print_mails(f.get_file_content())


# vygeneruje čísla 0,1,8,27,64 až 729
# range spustí cykl 100x. i se umocní třetí odm. a všechny čísla nižší 1000 se uloží
petky = [i**3 for i in range(100) if i**3 < 1000]
print(petky)

# 5 az 9 nasobeno 12
x = [n*12 for n in range(5,10)]
print(x)


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






