class Summa:
    def __init__(self, sovellus, io):
        self._sovellus = sovellus
        self._io = io

    def suorita(self):
        luku = int(self._io())
        self._sovellus.plus(luku)


class Erotus:
    def __init__(self, sovellus, io):
        self._sovellus = sovellus
        self._io = io

    def suorita(self):
        luku = int(self._io())
        self._sovellus.miinus(luku)


class Nollaus:
    def __init__(self, sovellus):
        self._sovellus = sovellus

    def suorita(self):
        self._sovellus.nollaa()


class Kumoa:
    def __init__(self, sovellus):
        self._sovellus = sovellus
    
    def suorita(self):
        self._sovellus.kumoa()
