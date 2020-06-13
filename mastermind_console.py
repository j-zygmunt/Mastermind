"""
This module contains the console version of the mastermind game.
It allows you or computer to play the game.

CLasses:
InappropriateCodeException(Exception)
    Guess/code validation failed.
InappropriateModeException(Exception)
    Mode validation failed.
BasePlayer
    Represents the base player of the mastermind game.
HumanPlayer(BasePlayer)
    Class that contains human game logic.
ComputerPlayer(BasePlayer)
    Class that contains computer game logic based on Five guess algorithm.

Functions:
choose_game_mode()
    Here you can choose the game mode.
appropriate_mode(mode)
    Check if the given mode is valid.
play_again()
    Here you can decide if you want to play again.
"""

import copy
import random
import sys
from itertools import product

NUMBER_OF_PINS = 6
CODE_LENGTH = 4
MAX_GUESSES = 12
ANSWER_LENGTH = 2


class InappropriateCodeException(Exception):
    """Guess/code validation failed."""

    def __init__(self, message):
        Exception.__init__(self)
        self.message = message

    def __str__(self):
        return self.message


class InappropriateModeException(Exception):
    """Mode validation failed."""

    def __init__(self, message):
        Exception.__init__(self)
        self.message = message

    def __str__(self):
        return self.message


class BasePlayer:
    """
    Represents the base player of the mastermind game.

    Attributes:
    number_of_pins : int
        Number of the possible digits(1,2,3,4,5,6) used during the game.
    count_guesses : int
        Represents the current number of guesses.
    code_length : int
        The length of code.
    max_guesses : int
        The maximum number of guesses after which the game will end.

    Methods:
    appropriate_code(code)
        Check if the given code or guess is valid.
    check(guess,code)
        Check if the given guess fits the code.
    game_over(result)
        Print endgame information
    get_random_code()
        Return randomly generated code.
    get_code_length()
        Return the code length.
    get_number_of_pins()
        Return the number of possible digits.
    get_max_guesses()
        Return the maximum number of guesses.
    get_count_guesses()
        Return the number of the current guess.
    increment_count_guesses()
        Increment the value of tried codes.
    """

    def __init__(self):
        """
        Construct all the necessary attributes for the BasePlayer object.
        """

        self.__number_of_pins = NUMBER_OF_PINS
        self.__count_guesses = 0
        self.__code_length = CODE_LENGTH
        self.__max_guesses = MAX_GUESSES

    def appropriate_code(self, code):
        """
        Check if the given code or guess is valid.

        :param code: the code to be checked
        :return code: the checked code
        :raises InappropriateCodeException: if code is invalid
        """

        try:
            code = [int(pin) for pin in code]
        except InappropriateCodeException:
            raise InappropriateCodeException("Kod musi składać się z samych cyfr.")
        for pin in code:
            if pin < 1 or pin > self.__number_of_pins:
                raise InappropriateCodeException("Dozwolone tylko cyfry od 1 do 6.")
        if len(code) != self.__code_length:
            raise InappropriateCodeException("Kod musi mieć długość = 4.")
        return code

    def check(self, guess, code):
        """
        Check if the given guess fits the code.

        :param guess: the guess to be checked
        :param code: the actual code
        :return black_dot: number of digits on the correct position
        :return white_dot: number of digits that are in the guess and in the code
                           but in the wrong position
        """

        black_dot = 0
        white_dot = 0
        temp_code = copy.copy(code)
        temp_guess = copy.copy(guess)
        for i in range(self.__code_length):
            if temp_guess[i] == code[i]:
                black_dot += 1
                temp_code.remove(guess[i])
                temp_guess[i] = None
        for i in range(self.__code_length):
            if temp_guess[i] in temp_code:
                white_dot += 1
                temp_code.remove(guess[i])
                temp_guess[i] = None
        return black_dot, white_dot

    def game_over(self, result):
        """
        Print endgame information.

        :param result : win/lose
        """

        if isinstance(self, HumanPlayer):
            if result:
                print("Gratulacje!\nwygrałeś za {} razem!".format(self.__count_guesses))
            else:
                print("Nie tym razem, pzdr poćwicz.")
        else:
            if result:
                print("Komputer wygrał za {} razem".format(self.__count_guesses))
            else:
                print("Nie tym razem, pzdr poćwicz.")

    def get_random_code(self):
        """Return randomly generated code."""

        return [random.randint(1, self.__number_of_pins) for _ in range(self.__code_length)]

    def get_code_length(self):
        """Return the code length."""

        return self.__code_length

    def get_number_of_pins(self):
        """Return the number of possible digits."""

        return self.__number_of_pins

    def get_max_guesses(self):
        """Return the maximum number of guesses."""

        return self.__max_guesses

    def get_count_guesses(self):
        """Return the number of the current guess."""

        return self.__count_guesses

    def increment_count_guesses(self):
        """Increment the value of tried codes."""

        self.__count_guesses += 1


class HumanPlayer(BasePlayer):
    """
    Class that contains human game logic.

    Attributes:
    code : list
        4-digit code

    Methods:
    get_guess()
        Get the user guess.
    get_answer()
        Print the answer.
    get_code()
        Return the actual code.
    play_mastermind()
        Game loop.
    set_code()
        Set code.
    """

    def __init__(self):
        """Construct all the necessary attributes for the HumanPlayer object."""

        super().__init__()
        self.__code = None

    def get_guess(self):
        """
        Get user guess.

        :return : valid guess
        """

        while True:
            try:
                user_input = input("Twoja próba: ")
                return self.appropriate_code(user_input)
            except InappropriateCodeException as error:
                print("Kod w nieprawidłowej formie: ", error)

    @staticmethod
    def get_answer(black_dot, white_dot):
        """Print the answer."""

        print("black {} white {}".format(black_dot, white_dot))

    def get_code(self):
        """Return the actual code"""

        return self.__code

    def play_mastermind(self):
        """
        Game loop.

        :return : True if you win, False if you lose
        """

        self.__code = self.get_random_code()
        while self.get_count_guesses() < self.get_max_guesses():
            self.increment_count_guesses()
            guess = self.get_guess()
            black_dot, white_dot = self.check(guess, self.__code)
            if black_dot == self.get_code_length():
                return self.game_over(True)
            self.get_answer(black_dot, white_dot)
        return self.game_over(False)

    def set_code(self, code):
        """Set_code."""

        self.__code = code


class ComputerPlayer(BasePlayer):
    """
        Class that contains computer game logic based on the Five guess algorithm.

        Attributes:
        initial_guess : list
            computers first guess, why is it 1122, ask the author of the Five guess algorithm
        code : list
            4-digit code
        unseen_codes : set
            set of all the unseen codes (that weren't computer guesses)
        possible_codes : set
            set of all the possible codes (6^4)
        response : tuple
            guess response
        current_guess : list
            actual guess

        Methods:
        set_code()
            Set code entered by user.
        remove_unlike_response()
            Remove from possible_codes any code that would not give the same response
            if it (the guess) were the code.
        remove_guess()
            Remove from possible_codes and unseen_codes the current guess if it's not the solution.
        minimax()
            Minimax technique to find the next guess.
        play_mastermind()
            Game loop.
        """

    __initial_guess = [1, 1, 2, 2]

    def __init__(self):
        """Construct all the necessary attributes for the HumanPlayer object."""

        super().__init__()
        self.__code = None
        self.__unseen_codes = set(product(tuple(range(1, self.get_number_of_pins()+1)),
                                          repeat=self.get_code_length()))
        self.__possible_codes = set(product(tuple(range(1, self.get_number_of_pins()+1)),
                                            repeat=self.get_code_length()))
        self.__response = None
        self.__current_guess = self.__initial_guess

    def set_user_code(self):
        """Set code entered by user."""

        while True:
            if self.__code is None:
                try:
                    user_input = input("Podaj kod: ")
                    self.__code = self.appropriate_code(user_input)
                except InappropriateCodeException as error:
                    print("Błędny kod: ", error)
            else:
                break

    def remove_unlike_response(self):
        """
        Remove from possible_codes any code that would not give the same response
        if it (the guess) were the code.
        """

        self.__possible_codes.difference_update(set(p for p in self.__possible_codes
                                                    if self.check(list(self.__current_guess),
                                                                  list(p)) != self.__response))

    def remove_guess(self):
        """
        Remove from possible_codes and unseen_codes the current guess if it's not the solution.
        """

        self.__unseen_codes.difference_update(self.__current_guess)
        self.__possible_codes.difference_update(self.__current_guess)

    def minmax(self):
        """Minimax technique to find the next guess."""

        minim = sys.maxsize
        results = {(black, white): 0 for black in range(self.get_code_length() + 1)
                   for white in range(self.get_code_length() + 1 - black)
                   if not (black == self.get_code_length() - 1 and white == 1)}
        for unseen in self.__unseen_codes:
            for possible in self.__possible_codes:
                ret = self.check(list(possible), list(unseen))
                results[ret] += 1
            maxim = max(results.values())
            results = {x: 0 for x in results}
            if maxim < minim:
                minim = maxim
                self.__current_guess = list(unseen)

    def play_mastermind(self, mode):
        """
        Game loop.

        :param : mode - game mode(random code, user code)
        :return : True if you win, False if you lose
        """

        if mode:
            self.set_user_code()
        else:
            self.__code = self.get_random_code()
            print("wyosowany kod", self.__code)
        while self.get_count_guesses() < self.get_max_guesses():
            self.increment_count_guesses()
            self.remove_guess()
            print("Strzał: {}".format(self.__current_guess))
            self.__response = self.check(self.__current_guess, self.__code)
            if self.__response[0] == self.get_code_length():
                return self.game_over(True)
            self.remove_unlike_response()
            if len(self.__possible_codes) == 1:
                self.__current_guess = list(self.__possible_codes.pop())
            else:
                self.minmax()
        return self.game_over(False)


def chose_game_mode():
    """
    Here you can choose the game mode.

    :return game_m : checked game mode
    """

    game_m = None
    while True:
        if game_m is None:
            try:
                user_input = input("Wybierz tryb gry:\n"
                                   "-Komputer zgaduje losowy kod - 1\n"
                                   "-Komputer zgaduje zadany kod - 2\n"
                                   "-Ty zgadujesz - 3\n"
                                   "Tryb: ")
                game_m = appropriate_mode(user_input)
            except InappropriateModeException as error:
                print("Nie ma takiego trybu: ", error)
        else:
            break
    return game_m


def appropriate_mode(mode):
    """
    Check if the given mode is valid.

    :param mode : game mode to be checked
    :return mode : checked game mode
    """

    try:
        mode = int(mode)
    except ValueError:
        raise InappropriateModeException("Aby wybrać tryb wpisz cyfrę.")
    if mode < 1 or mode > 3:
        raise InappropriateModeException("Aby wybrać tryb wpisz cyfrę od 1 do 3.")
    return mode


def play_again():
    """
    Here you can decide if you want to play again.

    :return True : play again
    :return False : terminate application
    """

    user_answer = input("żeby zakończyć wpisz stop: ")
    if user_answer.lower() != 'stop':
        return True
    return False


if __name__ == "__main__":
    game_mode = chose_game_mode()
    if game_mode == 1:
        game = ComputerPlayer()
        game.play_mastermind(False)
    if game_mode == 2:
        game = ComputerPlayer()
        game.play_mastermind(True)
    if game_mode == 3:
        game = HumanPlayer()
        game.play_mastermind()
    while play_again():
        game_mode = chose_game_mode()
        if game_mode == 1:
            game = ComputerPlayer()
            game.play_mastermind(False)
        if game_mode == 2:
            game = ComputerPlayer()
            game.play_mastermind(True)
        if game_mode == 3:
            game = HumanPlayer()
            game.play_mastermind()
