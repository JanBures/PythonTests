

def strToFloatPrice(n):
    """
    Prevede cislo ze stringu do float a provede zmenu desetinne carky na tecku.
    :param n: clear number in string
    :return: float
    """
    cislo = n
    if("," in cislo):
        cislo = cislo.replace(",",".")
    try:
        cislo = float(cislo)
    except:
        print("chyba")
    return cislo

def getPrice():
    cena = 0.0
    cenaCLR = 0.0
    cena = strToFloatPrice(cenaSTR)
    cenaSTR = input("zadej cenu:").strip()
    return cena


def getDiscount():
    slevaSTR = 0.0
    slevaSTR = input("zadej slevu v procentech:").strip()
    slevaFL = float(slevaSTR)
    return slevaFL

def spocitejSlevu():
    cena = getPrice()
    sleva = getDiscount()
    poSleve = (cena * ((100-sleva)*0.01))
    sdeleni = "částka {}Kč po {}% slevě je {}Kč".format(cena, round(sleva), poSleve)
    print(sdeleni)

spocitejSlevu()

