from tekoaly import tekoaly as default_tekoaly
from tekoaly_parannettu import tekoaly_parannettu as default_tekoaly_parannettu
from peli import Peli


class KiviSaksetPaperi:
    def __init__(self, tekoaly=default_tekoaly, tekoaly_parannettu=default_tekoaly_parannettu):
        self._tekoaly = tekoaly
        self._tekoaly_parannettu = tekoaly_parannettu

    def kaynnista(self):
        while True:
            self.tulosta_ohjeet()

            vastaus = input()

            if vastaus.endswith("a"):
                kaksinpeli = Peli.vs_pelaaja()
                kaksinpeli.pelaa()
            elif vastaus.endswith("b"):
                yksinpeli = Peli.vs_tekoaly(self._tekoaly)
                yksinpeli.pelaa()
            elif vastaus.endswith("c"):
                haastavampi_yksinpeli = Peli.vs_tekoaly(self._tekoaly_parannettu)
                haastavampi_yksinpeli.pelaa()
            else:
                break

    def tulosta_ohjeet(self):
        print("Valitse pelataanko"
                "\n (a) Ihmistä vastaan"
                "\n (b) Tekoälyä vastaan"
                "\n (c) Parannettua tekoälyä vastaan"
                "\nMuilla valinnoilla lopetetaan"
        )
