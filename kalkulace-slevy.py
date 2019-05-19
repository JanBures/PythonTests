slevaSTR = 0

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
    """
    získej cenu produktu od uživatele
    :return: cena produktu float
    """
    cenaSTR = 0.0
    cenaSTR = input("zadej cenu:").strip()
    cenaSTR = float(cenaSTR)
    return cenaSTR


def getDiscount():
    """
    získej výši slevy od uživatele
    :return: výše slevy float
    """
    slevaSTR = 0.0
    slevaSTR = input("zadej slevu v procentech:").strip()
    slevaFL = float(slevaSTR)
    return slevaFL


def spocitejSlevu():
    cena = getPrice()           # získej cenu produktu od uživatele
    sleva = getDiscount()       # získej výši slevy od uživatele
    vyse_slevy = cena - sleva   # sleva vyšíslena v měně
    poSleve = (cena * ((100-sleva)*0.01))
    sdeleni = "částka {}Kč po {}% slevě je {}Kč".format(cena, sleva, round(poSleve,2))


    print(sdeleni)
    print("Zlevněno o ", vyse_slevy)

spocitejSlevu()

