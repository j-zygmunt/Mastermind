"""
This module contains the mastermind game logic.
It allows you or computer to play the game.

CLasses:
InappropriateCodeException(Exception)
    Guess/code validation failed.
BasePlayer
    Represents the base player of the mastermind game.
HumanPlayer(BasePlayer)
    Class that contains human game logic.
ComputerPlayer(BasePlayer)
    Class that contains computer game logic based on Five guess algorithm.
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
        except ValueError:
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
    set_random_code()
        Set randomly generated code.
    get_code()
        Return the actual code.
    set_code()
        Set code.
    """

    def __init__(self):
        """Construct all the necessary attributes for the HumanPlayer object."""

        super().__init__()
        self.__code = None

    def set_random_code(self):
        """Set Randomly generated code."""

        self.__code = [random.randint(1, self.get_number_of_pins())
                       for _ in range(self.get_code_length())]

    def get_code(self):
        """Return the actual code"""
        return self.__code

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
    set_random_code()
        Set randomly generated code.
    remove_unlike_response()
        Remove from possible_codes any code that would not give the same response
        if it (the guess) were the code.
    remove_guess()
        Remove from possible_codes and unseen_codes the current guess if it's not the solution.
    minimax()
        Minimax technique to find the next guess.
    play_mastermind()
        Game loop for tests only.
    set_code(code)
        Set the actual code.
    get_code()
        Return the actual code.
    set_current_guess(guess)
        Set the current guess.
    get_current_guess()
        Return the current guess.
    get_possible_codes()
        Return the set of the possible guesses.
    set_response(response)
        Set the guess response.
    get_last_guess()
        Return the last element of possible guesses.
    """

    __initial_guess = [1, 1, 2, 2]

    def __init__(self):
        """Construct all the necessary attributes for the HumanPlayer object."""

        super().__init__()
        self.__code = None
        self.__unseen_codes = set(product(tuple(range(1, self.get_number_of_pins() + 1)),
                                          repeat=self.get_code_length()))
        self.__possible_codes = set(product(tuple(range(1, self.get_number_of_pins() + 1)),
                                            repeat=self.get_code_length()))
        self.__response = None
        self.__current_guess = self.__initial_guess

    def set_random_code(self):
        """Set randomly generated code."""

        self.__code = [random.randint(1, self.get_number_of_pins())
                       for _ in range(self.get_code_length())]

    def remove_unlike_response(self):
        """
        Remove from possible_codes any code that would not give the same response
        if it (the guess) were the code.
        """

        self.__possible_codes.difference_update(set(
            poss for poss in self.__possible_codes
            if self.check(list(self.__current_guess), list(poss)) != self.__response))

    def remove_guess(self):
        """
        Remove from possible_codes and unseen_codes the current guess if it's not the solution.
        """

        self.__unseen_codes.difference_update(self.__current_guess)
        self.__possible_codes.difference_update(self.__current_guess)

    def minimax(self):
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

    def play_mastermind(self):
        """
        Game loop for tests only.

        :return : True if you win, False if you lose
        """

        self.set_random_code()
        while self.get_count_guesses() < self.get_max_guesses():
            self.increment_count_guesses()
            self.remove_guess()
            self.__response = self.check(self.__current_guess, self.__code)
            if self.__response[0] == self.get_code_length():
                return True
            self.remove_unlike_response()
            if len(self.__possible_codes) == 1:
                self.__current_guess = list(self.__possible_codes.pop())
            else:
                self.minimax()
        return False

    def set_code(self, code):
        """Set the actual code."""

        self.__code = code

    def get_code(self):
        """Return the actual code."""

        return self.__code

    def set_current_guess(self, guess):
        """Set the current guess."""

        self.__current_guess = guess

    def get_current_guess(self):
        """Return the current guess."""

        return self.__current_guess

    def get_possible_codes(self):
        """Return the set of the possible guesses."""

        return self.__possible_codes

    def set_response(self, response):
        """Set the guess response."""

        self.__response = response

    def get_last_guess(self):
        """Return the last element of possible guesses."""

        return list(self.__possible_codes.pop())
