from rockpaperscissors import Round, InvalidMoveException, Game, GameListener


class Program(object):

    def main(self):
        testsPassed = 0
        testsFailed = 0

        # output header
        print("Running RockPaperScissors tests...")

        # Round tests
        print("Round tests...")

        # rock blunts scissors
        result = Round().play("Rock", "Scissors")

        if result == 1:
            testsPassed += 1
            print("rock blunts scissors (Rock, Scissors): PASS")
        else:
            testsFailed += 1
            print("rock blunts scissors (Rock, Scissors): FAIL - expected 1 but was %d" % result)

        result = Round().play("Scissors", "Rock")

        if result == 2:
            testsPassed += 1
            print("rock blunts scissors (Scissors, Rock): PASS")
        else:
            testsFailed += 1
            print("rock blunts scissors (Scissors, Rock): FAIL - expected 2 but was %d" % result)

        # scissors cut paper
        result = Round().play("Scissors", "Paper")

        if result == 1:
            testsPassed += 1
            print("scissors cut paper (Scissors, Paper): PASS")
        else:
            testsFailed += 1
            print("scissors cut paper (Scissors, Paper): FAIL - expected 1 but was %d" % result)

        result = Round().play("Paper", "Scissors")

        if result == 2:
            testsPassed += 1
            print("scissors cut paper (Paper, Scissors): PASS")
        else:
            testsFailed += 1
            print("scissors cut paper (Paper, Scissors): FAIL - expected 2 but was %d" % result)

        # paper wraps rock
        result = Round().play("Paper", "Rock")

        if result == 1:
            testsPassed += 1
            print("paper wraps rock (Paper, Rock): PASS")
        else:
            testsFailed += 1
            print("paper wraps rock (Paper, Rock): FAIL - expected 1 but was %d" % result)

        result = Round().play("Rock", "Paper")

        if result == 2:
            testsPassed += 1
            print("paper wraps rock (Rock, Paper): PASS")
        else:
            testsFailed += 1
            print("paper wraps rock (Rock, Paper): FAIL - expected 2 but was %d" % result)

        # round is a draw
        result = Round().play("Rock", "Rock")

        if result == 0:
            testsPassed += 1
            print("round is a draw (Rock, Rock): PASS")
        else:
            testsFailed += 1
            print("round is a draw (Rock, Rock): FAIL - expected 0 but was %d" % result)

        result = Round().play("Scissors", "Scissors")

        if result == 0:
            testsPassed += 1
            print("round is a draw (Scissors, Scissors): PASS")
        else:
            testsFailed += 1
            print("round is a draw (Scissors, Scissors): FAIL - expected 0 but was %d" % result)

        result = Round().play("Paper", "Paper")

        if result == 0:
            testsPassed += 1
            print("round is a draw (Paper, Paper): PASS")
        else:
            testsFailed += 1
            print("round is a draw (Paper, Paper): FAIL - expected 0 but was %d" % result)

        # invalid inputs not allowed
        exception_raised = False

        try:
            Round().play("Blah", "Foo")
        except InvalidMoveException:
            exception_raised = True

        if exception_raised:
            testsPassed += 1
            print("invalid inputs not allowed: PASS")
        else:
            testsFailed += 1
            print("invalid inputs not allowed: FAIL - expected InvalidMoveException")

        # Game tests
        print("Game tests...")

        # player 1 wins game
        listener = SpyGameListener()
        game = Game(listener)

        game.play_round("Rock", "Scissors")
        game.play_round("Rock", "Scissors")

        result = listener.winner

        if result == 1:
            testsPassed += 1
            print("player 1 wins game: PASS")
        else:
            testsFailed += 1
            print("player 1 wins game: FAIL - expected 1 but was %d" % result)

        # player 2 wins game
        listener = SpyGameListener()
        game = Game(listener)
        game.play_round("Rock", "Paper")
        game.play_round("Rock", "Paper")

        result = listener.winner

        if result == 2:
            testsPassed += 1
            print("player 2 wins game: PASS")
        else:
            testsFailed += 1
            print("player 2 wins game: FAIL - expected 2 but was %d" % result)

        # drawers not counted
        listener = SpyGameListener()
        game = Game(listener)
        game.play_round("Rock", "Rock")
        game.play_round("Rock", "Rock")

        result = listener.winner

        if result == 0:
            testsPassed += 1
            print("drawers not counted: PASS")
        else:
            testsFailed += 1
            print("drawers not counted: FAIL - expected 0 but was %d" % result)

        # invalid moves not counted
        listener = SpyGameListener()
        game = Game(listener)
        try:
            game.play_round("Blah", "Foo")
            game.play_round("Rock", "Scissors")
        except:
            pass

        result = listener.winner

        if result == 0:
            testsPassed += 1
            print("invalid moves not counted: PASS")
        else:
            testsFailed += 1
            print("invalid moves not counted: FAIL - expected 0 but was %d" % result)

        print("Tests run: %d  Passed: %d  Failed: %d" % (testsPassed + testsFailed, testsPassed, testsFailed))


class SpyGameListener(GameListener):
    winner = 0

    def game_over(self, winner):
        self.winner = winner


if __name__ == "__main__":
    Program().main()
