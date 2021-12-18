from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly


class Peli:
    @staticmethod
    def vs_pelaaja():
        return KPSPelaajaVsPelaaja()

    @staticmethod
    def vs_tekoaly(tekoaly):
        return KPSTekoaly(tekoaly)
