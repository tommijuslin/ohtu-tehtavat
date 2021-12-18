from tuomari import Tuomari


class KPS:
    def __init__(self, tekoaly=None):
        self._tekoaly = tekoaly
        self._tuomari = Tuomari()

    def pelaa(self):
        self._tulosta_ohje()

        ekan_siirto = self._ensimmaisen_siirto()
        tokan_siirto = self._toisen_siirto(ekan_siirto)

        while self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto):
            self._tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)

            self._tulosta_pelitilanne()

            ekan_siirto = self._ensimmaisen_siirto()
            tokan_siirto = self._toisen_siirto(ekan_siirto)

        self._lopeta_peli()

    def _ensimmaisen_siirto(self):
      return input("Ensimmäisen pelaajan siirto: ")

    def _toisen_siirto(self, ensimmaisen_siirto):
        return "k"

    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"

    def _tulosta_ohje(self):
        print(
            "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
        )
    
    def _tulosta_pelitilanne(self):
        print(self._tuomari)
    
    def _lopeta_peli(self):
        print("Kiitos!")
        self._tulosta_pelitilanne()
