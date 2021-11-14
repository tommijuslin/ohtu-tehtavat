import requests
from player import Player

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    response = requests.get(url).json()

    # print("JSON-muotoinen vastaus:")
    # print(response)

    players = []
    finnish_players = [player for player in response if player['nationality'] == 'FIN']

    for player_dict in finnish_players:
        player = Player(
            player_dict['name'],
            player_dict['team'],
            player_dict['goals'],
            player_dict['assists']
        )

        players.append(player)

    # print("Oliot:")

    for player in players:
        print(player)


if __name__ == "__main__":
    main()
