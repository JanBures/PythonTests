from random import randint

# zip
jmena = ["Pavel","Lukáš","Robert", "Marek", "Franta"] #definice jmen
cisla = [randint(10,20) for y in range(len(jmena))]
z=dict(zip(cisla,jmena))
print(z)



#výpis obsahu slovníku
for key in z:
    res = "Klíč: {} \t Hodnota: {}".format(key,z[key])
    print(res)
