from os import path

class Filehandler():
    """
    Třída obsluhující soubory s daty
    """

    filename="soubor.txt"

    def __init__(self, filename):
        print("Vytvářím instanci třídy Filehandler")
        self.filename = filename
        print("Ověřuji existenci souboru", self.filename)
        self.file_existence_verification()


    def file_existence_verification(self):
        if path.exists(self.filename):
            print("Soubor", self.filename ," existuje!\nPokračujte prácí v souboru.\n---------------" )
        else:
            print("Soubor", self.filename ,"neexistuje. Zakládám ho.")
            self.create_file()
        pass


    def create_file(self):
        open(self.filename, "w+")
        self.file_existence_verification()


    def get_file_content(self):
        f = open(self.filename, "r")
        content = f.read()
        f.close()
        return content


    def vypis_obsah_souboru(self):
        print(self.get_file_content())

    def get_mail_count(self):
        content = self.get_file_content()
        mail_count = content.count("@")
        return mail_count


