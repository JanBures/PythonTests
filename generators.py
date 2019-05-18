class Generator:

    def __init__(self):
        pass

    def generate_alphabet(self):
        alp="abcdefghijklmnopqrstuvwxyz"
        for l in alp:
            yield l

    def generate_odds(self):
        start = 0
        step = 1
        num = 0
        for i in range(start,10):
            if i %2 == 0:
                yield i

    def get_odds(self, start, amount):
        odds = [i for i in range(start,amount)]
        return odds


