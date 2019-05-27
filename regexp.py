import re

class Regexp:

    def extract_mails(self, content):
        """
        Vytáhne ze stringu mailové adresy
        :param content: string s email adresami
        :return: list očištěných adres
        """
        mail_regex = re.compile('[a-zA-Z]1[-_\w\.]+@[-\w\.]+\.[a-zA-Z0-9]{1,3}')
        maily = mail_regex.findall(content)
        return maily

    def extract_mails2(self, content):
        """
        stejný princip jako metoda výše, s použitím
        :param content:
        :return:
        """
        pattern = (r'[a-zA-Z]{1}[-_\w\.]+@[-\w\.]+\.[a-zA-Z0-9]{1,3}')
        maily = re.findall(pattern, content)
        return maily


    def print_mails(self, content):
        maily = self.extract_mails2(content)
        for mail in maily:
            print(mail)