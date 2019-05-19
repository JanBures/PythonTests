slevaSTR = 0
mena = "Kč"

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
    if not cenaSTR:              # přidá výchozí hodnotu
        cenaSTR = 0.0
    else:
        try:
           cenaSTR = float(cenaSTR) # convert string input to float
        except(ValueError):
            print("chybné zadání!")
            exit()
    return cenaSTR


def getDiscount():
    """
    získej výši slevy od uživatele
    :return: výše slevy float
    """
    slevaSTR = 0.0
    slevaSTR = input("zadej slevu v procentech:").strip()
    try:
        slevaFL = float(slevaSTR)
    except(ValueError):
        print("Chybné zadání!")
        exit()
    return slevaFL


def spocitejSlevu():
    """
    výpočet konečné slevy
    :return:
    """
    cena = getPrice()           # získej cenu produktu od uživatele
    sleva = getDiscount()       # získej výši slevy od uživatele
    vyse_slevy = 0.0
    cena_po_sleve = (cena * ((100 - sleva) * 0.01))
    vyse_slevy = round(cena - cena_po_sleve, 2)
    sdeleni = "částka {} {} po {}% slevě je {} {}".format(cena, mena, sleva, round(cena_po_sleve, 2), mena)
    print(sdeleni)
    print("Zlevněno o ", vyse_slevy)

spocitejSlevu()

