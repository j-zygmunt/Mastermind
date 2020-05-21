import copy
import random
import sys
from itertools import product


class BasePlayer:

    def __init__(self):
        self.__number_of_pins = 6
        self.__count_guesses = 0
        self.__code_length = 4
        self.__max_guesses = 12

    def appropriate_code(self, code):
        try:
            code = [int(pin) for pin in code]
        except Exception:
            raise Exception("kod musi składać się z samych cyfr")
        for pin in code:
            if pin < 1 or pin > self.__number_of_pins:
                raise Exception("Dozwolone tylko cyfry od 1 do 6")
        if len(code) != self.__code_length:
            raise Exception("Kod musi mieć długość = 4")
        return code

    def check(self, guess, code):
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
        if isinstance(self, HumanPlayer):
            if result:
                print("Gratulacje!\nwygrałeś za {} razem!".format(self.__count_guesses + 1))
            else:
                print("nie tym razem, pzdr poćwicz")
        else:
            if result:
                print("Komputer wygrał za {} razem".format(self.__count_guesses + 1))
            else:
                print("nie tym razem, pzdr poćwicz")

    def get_random_code(self):
        return [random.randint(1, self.__number_of_pins) for _ in range(self.__code_length)]

    def get_code_length(self):
        return self.__code_length

    def get_number_of_pins(self):
        return self.__number_of_pins

    def get_max_guesses(self):
        return self.__max_guesses

    def get_count_guesses(self):
        return self.__count_guesses

    def increment_count_guesses(self):
        self.__count_guesses += 1


class HumanPlayer(BasePlayer):
    def __init__(self):
        super().__init__()
        self.__code = None

    def get_guess(self):
        while True:
            try:
                user_input = input("Twoja próba: ")
                return self.appropriate_code(user_input)
            except Exception as error:
                print("Kod w nieprawidłowej formie: ", error)

    @staticmethod
    def get_answer(black_dot, white_dot):
        print("black {} white {}".format(black_dot, white_dot))

    def play_mastermind(self):
        self.__code = self.get_random_code()
        while self.get_count_guesses() < self.get_max_guesses():
            self.increment_count_guesses()
            guess = self.get_guess()
            black_dot, white_dot = self.check(guess, self.__code)
            if black_dot == self.get_code_length():
                return self.game_over(True)
            self.get_answer(black_dot, white_dot)
        return self.game_over(False)


class ComputerPlayer(BasePlayer):
    __initial_guess = [1, 1, 2, 2]

    def __init__(self):
        super().__init__()
        self.__code = None
        self.__unseen_codes = set(product(tuple(range(1, self.get_number_of_pins()+1)),
                                          repeat=self.get_code_length()))
        self.__possible_codes = set(product(tuple(range(1, self.get_number_of_pins()+1)),
                                            repeat=self.get_code_length()))
        self.__response = None
        self.__current_guess = self.__initial_guess

    def get_code(self):
        while True:
            if self.__code is None:
                try:
                    user_input = input("Podaj kod: ")
                    self.__code = self.appropriate_code(user_input)
                except Exception as error:
                    print("Błędny kod: ", error)
            else:
                break

    def remove_unlike_response(self):
        self.__possible_codes.difference_update(set(p for p in self.__possible_codes
                                                    if self.check(list(self.__current_guess),
                                                                  list(p)) != self.__response))

    def remove_guess(self):
        self.__unseen_codes.difference_update(self.__current_guess)
        self.__possible_codes.difference_update(self.__current_guess)

    def minmax(self):
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

    def play_mastermind(self, who):
        if who:
            self.get_code()
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
    game_m = None
    while True:
        if game_m is None:
            try:
                user_input = input("Wybierz tryb gry:\n"
                                   "-Komputer zgaduje losowy kod - 1\n"
                                   "-Komputer zgaduje zadany kod - 2\n"
                                   "-Komputer zgaduje zadany kod, ty odpowiadzasz - 3\n"
                                   "-Ty zgadujesz - 4\n"
                                   "Tryb: ")
                game_m = appropriate_mode(user_input)
            except Exception as error:
                print("Nie ma takiego trybu: ", error)
        else:
            break
    return game_m


def appropriate_mode(user_mode):
    try:
        mode = int(user_mode)
    except Exception:
        raise Exception("Aby wybrać tryb wpisz cyfrę")
    if mode < 1 or mode > 4:
        raise Exception("Aby wybrać tryb wpisz cyfrę od 1 do 4")
    return mode


def play_again():
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
        print("to implement")
    if game_mode == 4:
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
            print("to implement")
        if game_mode == 4:
            game = HumanPlayer()
            game.play_mastermind()
