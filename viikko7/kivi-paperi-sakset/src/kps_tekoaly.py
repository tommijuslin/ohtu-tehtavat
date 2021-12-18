from kps import KPS


class KPSTekoaly(KPS):
    def _toisen_siirto(self, ensimmaisen_siirto):
        tokan_siirto = self._tekoaly.anna_siirto()

        print(f"Tietokone valitsi: {tokan_siirto}")
        self._tekoaly.aseta_siirto(ensimmaisen_siirto)

        return tokan_siirto
