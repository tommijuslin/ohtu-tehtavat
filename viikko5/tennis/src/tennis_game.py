class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_score += 1
        else:
            self.player2_score += 1
    
    def get_draw_score(self):
        score = {
            0: "Love-All",
            1: "Fifteen-All",
            2: "Thirty-All",
            3: "Forty-All"
        }

        if self.player1_score in score:
            return score[self.player1_score]
        else:
            return "Deuce"
    
    def get_advantage(self):
        if self.player1_score > self.player2_score:
            return "Advantage player1"
        else:
            return "Advantage player2"

    def get_win(self):
        if self.player1_score > self.player2_score:
            return "Win for player1"
        else:
            return "Win for player2"
    
    def get_uneven_score(self):
        score = {
            0: "Love",
            1: "Fifteen",
            2: "Thirty",
            3: "Forty"
        }

        return f"{score[self.player1_score]}-{score[self.player2_score]}"

    def get_score(self):
        score = ""

        if self.player1_score == self.player2_score:
            score = self.get_draw_score()
        elif self.player1_score >= 4 or self.player2_score >= 4:
            result = abs(self.player1_score - self.player2_score)
            if result == 1:
                score = self.get_advantage()
            else:
                score = self.get_win()
        else:
            score = self.get_uneven_score()

        return score
