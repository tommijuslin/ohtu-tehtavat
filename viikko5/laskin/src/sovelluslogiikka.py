class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulos = [tulos]

    def miinus(self, arvo):
        self.tulos.append(self.tulos[-1] - arvo)

    def plus(self, arvo):
        self.tulos.append(self.tulos[-1] + arvo)

    def nollaa(self):
        self.tulos.append(0)

    def aseta_arvo(self, arvo):
        self.tulos.append(arvo)
    
    def kumoa(self):
        if len(self.tulos) > 1:
            self.tulos.pop()
