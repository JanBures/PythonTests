class human:
    name = ""
    druh = "clovek"
    rychlost_chuze = 5
    seznam_deti = []

    def __init__(self, name):
        self.name = name
        print("Ahoj, jsem", self.name,"!")
        self.pocet_deti = 0

    def dychej(self):
        print("dycham")

    def prejmenuj(self, name):
        self.name = name

    def pridej_dite(self, jmeno):
        self.seznam_deti.append(jmeno)


    def rozeberJmeno(self):
        num_of_letters = len(self.name)
        letters = []
        zipped_letters = []
        for l in self.name:
            print("přidávám", l ,"do listu letters[]")
            letters.append(l)
        print(letters)
        for l,n in zip(enumerate(letters, start=1), letters):
            print(l)
            zipped_letters.append(l)
        print(zipped_letters)

    def maDeti(self):
        self.pocet_deti = len(self.seznam_deti)
        if len(self.seznam_deti) >0:
            print ("počet dětí:", self.pocet_deti)
        else:
            print("nemá děti")

        print("ověření přes negaci NOT ")
        if not self.seznam_deti:
            print("nemá děti")
        else:
            print("má děti")
