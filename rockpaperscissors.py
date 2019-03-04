from abc import ABC, abstractmethod


class InvalidMoveException(Exception):
    pass


class Round(object):

    def play(self, player1, player2):
        if player1 == "Rock":
            if player2 == "Scissors":
                return 1
            if player2 == "Paper":
                return 2
            if player2 == "Rock":
                return 0

        if player1 == "Paper":
            if player2 == "Rock":
                return 1
            if player2 == "Scissors":
                return 2
            if player2 == "Paper":
                return 0

        if player1 == "Scissors":
            if player2 == "Paper":
                return 1
            if player2 == "Rock":
                return 2
            if player2 == "Scissors":
                return 0

        raise InvalidMoveException()


class GameListener(ABC):

    @abstractmethod
    def game_over(self, winner):
        pass


class Game(object):

    def __init__(self, listener):
        self.player_1_score = 0
        self.player_2_score = 0
        self.listener = listener

    def play_round(self, player1, player2):
        result = Round().play(player1, player2)
        if result == 1:
            self.player_1_score += 1
        if result == 2:
            self.player_2_score += 1

        if self.player_1_score == 2:
            self.listener.game_over(1)

        if self.player_2_score == 2:
            self.listener.game_over(2)
