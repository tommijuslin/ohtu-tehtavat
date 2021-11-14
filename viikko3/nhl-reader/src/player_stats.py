
def sort_by_points(player):
    return player.goals + player.assists


class PlayerStats:
    def __init__(self, reader):
        self._reader = reader

        self._players = self._reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        players_of_nationality = filter(
            lambda player: player.nationality == nationality,
            self._players
        )

        result = sorted(
            players_of_nationality,
            reverse=True,
            key=sort_by_points
        )

        return result
