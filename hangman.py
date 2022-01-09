from random import randint

class Game:
    """
    Hangman Game
    """

    # Dictionary of lowercase english words I got online
    FILE = "words.txt"

    BORDER_LEN = 50
    GAME_OPTIONS = [10, 8, 6]
    HANGMAN_STATES = [
        """
                    -----
                    |   |
                        |
                        |
                        |
                        |
                    ---------
        """,
        """
                    -----
                    |   |
                    O   |
                        |
                        |
                        |
                    ---------
        """,
        """
                    -----
                    |   |
                    O   |
                    |   |
                        |
                        |
                    ---------
        """,
        """
                    -----
                    |   |
                    O   |
                   /|   |
                        |
                        |
                    ---------
        """,
        """
                    -----
                    |   |
                    O   |
                   /|\  |
                        |
                        |
                    ---------
        """,
        """
                    -----
                    |   |
                    O   |
                   /|\  |
                   /    |
                        |
                    ---------
        """,
        """
                    -----
                    |   |
                    O   |
                   /|\  |
                   / \  |
                        |
                    ---------
        """,
        """
                    -----
                    |   |
                    O   |
                   /|\  |
                  _/ \  |
                        |
                    ---------
        """,
        """
                    -----
                    |   |
                    O   |
                   /|\  |
                  _/ \_ |
                        |
                    ---------
        """,
        """
                    -----
                    |   |   
                    O   |
                  ./|\  |
                  _/ \_ |
                        |
                    ---------
        """,
        """
                    -----
                    |   |   
                    O   |
                  ./|\. |
                  _/ \_ |
                        |
                    ---------
        """]

    def __init__(self, game_option=0):
        """ Intialize the game
        :param game_option: is either 0, 1, 2
        :type game_option: int
        """
        self.word = self.random_word()
        self.incorrect = []
        self.correct = []
        self.guess_limit = Game.GAME_OPTIONS[game_option]
        self.gameover = False

    def random_word(self):
        """ Return a random word for hangman game
        :rtype: str
        """
        dictionary = open(Game.FILE, 'r').readlines()
        rand_index = randint(0, len(dictionary))
        word = dictionary[rand_index].strip()
        return word

    def get_correct_guesses(self, with_underlines):
        """ Return the correct guessed letters with
        underlines if with_underlines is True
        :type with_underlines: bool
        :rtype: str
        """
        ret_str = ""
        for letter in self.word:
            if letter in self.correct:
                if with_underlines:
                    ret_str += " %s " % letter
                else:
                    ret_str += letter
            elif with_underlines:
                ret_str += " _ "
        return ret_str

    def already_guessed(self, guess):
        """ Return True if the guess is already guessed
        :type guess: str
        :rtype: bool
        """
        return guess in (self.correct + self.incorrect)

    def guess_letter(self, guess):
        """ Checks if the guess is correct
        :type guess: str
        :rtype: None
        """
        if guess in self.word:
            self.correct.append(guess)
        else:
            self.incorrect.append(guess)

    def check_gameover(self):
        """ Return if the game is over
        :rtype: str
        """
        ret_str = ""
        if len(self.incorrect) >= self.guess_limit:
            ret_str = "\nYou lose. The word was %r." % self.word
            self.gameover = True
        elif self.get_correct_guesses(False) == self.word:
            ret_str = "\nYou won the game!"
            self.gameover = True
        return ret_str

    def __str__(self):
        """ Return the string of the current
         state of the hangman game
        :rtype: str
        """
        return ("\n" + "-" * Game.BORDER_LEN +
                "\n" + Game.HANGMAN_STATES[len(self.incorrect)] +
                "\n" + "Incorrect guesses: %s" % ", ".join(self.incorrect) +
                "\n" + "Correct guesses: %s" % self.get_correct_guesses(True) +
                self.check_gameover())


def check_guess(game):
    """ Return the string prompt for the hangman game
    :type game: Game
    :rtype: str
    """
    while True:
        guess = input("Guess a letter: ").lower()
        if not guess.isalpha() or len(guess) > 1:
            print("Please guess a letter.")
        elif game.already_guessed(guess):
            print("You've already guessed %r." % guess)
        else:
            return guess


def main():
    """ Main I/O for the Hangman Game
    :rtype: str
    """
    play_game = True
    while play_game:
        print("\n------- WELCOME TO KIRANJIT's HANGMAN GAME -------")
        settings_menu = True
        difficulty_level = 0
        print("\nThere are multiple difficulty settings:")
        print("\t(b) Beginner     (10 lives)")
        print("\t(i) Intermediate (8 lives)")
        print("\t(e) Expert       (6 lives)")
        while settings_menu:
            user_setting = input("\nPlease choose a difficulty option (b,i,e): ")
            if user_setting in "bie":
                if user_setting == "b":
                    difficulty_level = 0
                elif user_setting == "i":
                    difficulty_level = 1
                elif user_setting == "e":
                    difficulty_level = 2
                settings_menu = False
        game = Game(difficulty_level)
        print(game)
        while not game.gameover:
            guess = check_guess(game)
            game.guess_letter(guess)
            print(game)
        play_again = input("Want to play again? (y/n): ").lower()
        if play_again == "n":
            play_game = False
    print("\nThanks for playing for Kiranjit's Hangman Game!")


if __name__ == "__main__":
    main()
