import copy as cp
import random


class GameRules(object):

    def __init__(self, code_length=4, number_of_pins=6):
        self.number_of_pins = number_of_pins
        self.countGuesses = 0
        self.code_length = code_length

    def appropriate_code(self, code):
        try:
            code = [int(pin) for pin in code]
        except Exception:
            raise Exception("kod musi składać się z samych cyfr")
        for pin in code:
            if pin < 1 or pin > 6:
                raise Exception("Dozwolone tylko cyfry od 1 do 6")
        if len(code) != self.code_length:
            raise Exception("Kod musi mieć długość = 4")
        return code

    @staticmethod
    def check(guess, code):
        black_dot = 0
        white_dot = 0
        temp = cp.copy(code)
        for i in range(4):
            if guess[i] == code[i]:
                black_dot += 1
                temp.remove(guess[i])
                guess[i] = None
        for i in range(4):
            if guess[i] in temp:
                white_dot += 1
                temp.remove(guess[i])
                guess[i] = None
        return black_dot, white_dot

    def game_over(self, result):
        if type(self) is HumanPlayer:
            if result:
                print("Gratulacje!\nwygrałeś za {} razem!".format(self.countGuesses + 1))
            else:
                print("nie tym razem, pzdr poćwicz")
        else:
            print("Komputer wygrał za %s razem", self.countGuesses + 1)

    def get_code(self):
        return [random.randint(1, self.number_of_pins) for _ in range(self.code_length)]


class HumanPlayer(GameRules):
    def __init__(self):
        super().__init__()
        self.code = None

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
        self.code = self.get_code()
        print(self.code)
        while self.countGuesses < 12:
            guess = self.get_guess()
            print(guess)
            print(self.code)
            black_dot, white_dot = self.check(guess, self.code)
            if black_dot == 4:
                return self.game_over(True)
            else:
                self.get_answer(black_dot, white_dot)
            self.countGuesses +=1
        return self.game_over(False)


class ComputerPlayer(GameRules):
    def __init__(self):
        super().__init__()
        self.code = None


    def get_code(self):
        while True:
            if self.code is None:
                try:
                    user_input = input("Podaj kod: ")
                    self.game_rules.appropriate_code(user_input)
                except Exception as error:
                    print("Błędny kod: ", error)
                    user_input = None
                self.code = user_input
            else:
                break

    def get_answer(self, black_dot, white_dot):
        pass

    def play_mastermind(self, who):
        if who:
            self.get_code()
        else:
            self.code = super().get_code()
        while self.countGuesses < 12:
            black_dot, white_dot = self.check(self.get_guess(), self.code)
            if black_dot == 4:
                return self.winner()
            else:
                self.get_answer(black_dot, white_dot)


def play_again():
    user_input = input("żeby zakończyć wpisz stop: ")
    if user_input.lower() != 'stop':
        return True
    return False


if __name__ == "__main__":
    game = HumanPlayer()
    game.play_mastermind()
    while play_again():
        new_game = HumanPlayer()
        new_game.play_mastermind()
