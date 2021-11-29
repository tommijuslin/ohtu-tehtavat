KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        self._kapasiteetti = max(0, kapasiteetti)
        self._kasvatuskoko = max(0, kasvatuskoko)
        self._alkiot = [None] * self._kapasiteetti
        self._alkioiden_maara = 0

    def kuuluu(self, alkio):
        return alkio in self._alkiot

    def lisaa(self, alkio):
        if not self.kuuluu(alkio):
            self._alkiot[self._alkioiden_maara] = alkio
            self._alkioiden_maara += 1

            if self._alkioiden_maara == len(self._alkiot):
                self.kasvata()

            return True

        return False

    def poista(self, alkio):
        if not self.kuuluu(alkio):
            return False

        for i in range(self._alkioiden_maara):
            if alkio == self._alkiot[i]:
                self._alkiot[i] = None
                self.siirra_alkioita_vasemmalle(i)
                self._alkioiden_maara -= 1
                break

        return True

    def siirra_alkioita_vasemmalle(self, poistetun_indeksi):
        for i in range(poistetun_indeksi, self._alkioiden_maara - 1):
            apu = self._alkiot[i]
            self._alkiot[i] = self._alkiot[i + 1]
            self._alkiot[i + 1] = apu

    def kopioi_taulukko(self, vanha, uusi):
        for i in range(len(vanha)):
            uusi[i] = vanha[i]
    
    def kasvata(self):
        taulu_old = self._alkiot
        self.kopioi_taulukko(self._alkiot, taulu_old)
        self._alkiot = [None] * (self._alkioiden_maara + self._kasvatuskoko)
        self.kopioi_taulukko(taulu_old, self._alkiot)

    def mahtavuus(self):
        return self._alkioiden_maara

    def to_int_list(self):
        taulu = [None] * self._alkioiden_maara

        for i in range(len(taulu)):
            taulu[i] = self._alkiot[i]

        return taulu

    @staticmethod
    def yhdiste(a, b):
        joukko = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        yhdiste = a_taulu + b_taulu

        for alkio in yhdiste:
            joukko.lisaa(alkio)
        
        return joukko

    @staticmethod
    def leikkaus(a, b):
        joukko = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        leikkaus = list(set(a_taulu) & set(b_taulu))

        for alkio in leikkaus:
            joukko.lisaa(alkio)

        return joukko

    @staticmethod
    def erotus(a, b):
        joukko = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        erotus = set(a_taulu) - set(b_taulu)

        for alkio in erotus:
            joukko.lisaa(alkio)

        return joukko

    def __str__(self):
        return "{" + (', ').join(str(alkio) for alkio in self.to_int_list()) + "}"
