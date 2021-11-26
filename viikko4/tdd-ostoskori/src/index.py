# testikoodi tänne jos tarvetta
from ostoskori import Ostoskori
from tuote import Tuote


def main():
    kori = Ostoskori()
    maito = Tuote("Maito", 3)
    kori.lisaa_tuote(maito)
    kori.lisaa_tuote(maito)

    print(len(kori.ostokset()))


if __name__ == "__main__":
    main()
