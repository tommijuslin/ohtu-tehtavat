import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.statistics = Statistics(
            PlayerReaderStub()
        )
    
    def test_listalla_esiintyva_pelaaja_loytyy(self):
        player = self.statistics.search("Lemieux")

        self.assertEqual(player.name, "Lemieux")

    def test_listalta_puuttuvan_pelaajan_etsiminen_palauttaa_oikean_arvon(self):
        player = self.statistics.search("Juslin")

        self.assertEqual(player, None)

    def test_joukkuehaku_palauttaa_oikean_maaran_pelaajia(self):
        players = self.statistics.team("EDM")

        self.assertAlmostEqual(len(players), 3)

    def test_pisteporssi_palauttaa_listan_oikein(self):
        players = self.statistics.top_scorers(5)

        self.assertEqual(players[0].name, "Gretzky")