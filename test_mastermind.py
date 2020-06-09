"""This module contains unittests of some mastermind game logic functions."""

import unittest
import mastermind


class TestMastermind(unittest.TestCase):

    def test_completely_wrong_code_human(self):
        """
        Test if method gives correct answers (human)
            completely wrong code
        """

        game = mastermind.HumanPlayer()
        game.set_code([1, 1, 1, 1])
        black, white = game.check([2, 2, 2, 2], game.get_code())
        self.assertEqual(black, 0)
        self.assertEqual(white, 0)

        black, white = game.check([4, 5, 4, 5], game.get_code())
        self.assertEqual(black, 0)
        self.assertEqual(white, 0)

    def test_completely_wrong_code_computer(self):
        """
        Test if method gives correct answers (computer)
            completely wrong code
        """

        game = mastermind.ComputerPlayer()
        game.set_code([1, 1, 1, 1])
        black, white = game.check([2, 2, 2, 2], game.get_code())
        self.assertEqual(black, 0)
        self.assertEqual(white, 0)

        black, white = game.check([4, 5, 4, 5], game.get_code())
        self.assertEqual(black, 0)
        self.assertEqual(white, 0)

    def test_wrong_positions_human(self):
        """
        Test if method gives correct answers (human)
            digits on wrong positions
        """

        game = mastermind.HumanPlayer()
        game.set_code([6, 3, 6, 1])
        black, white = game.check([3, 6, 1, 6], game.get_code())
        self.assertEqual(black, 0)
        self.assertEqual(white, 4)

        black, white = game.check([1, 6, 3, 6], game.get_code())
        self.assertEqual(black, 0)
        self.assertEqual(white, 4)

        black, white = game.check([1, 1, 1, 3], game.get_code())
        self.assertEqual(black, 0)
        self.assertEqual(white, 2)

    def test_wrong_positions_computer(self):
        """
        Test if method gives correct answers (computer)
            digits on wrong positions
        """

        game = mastermind.ComputerPlayer()
        game.set_code([6, 3, 6, 1])
        black, white = game.check([3, 6, 1, 6], game.get_code())
        self.assertEqual(black, 0)
        self.assertEqual(white, 4)

        black, white = game.check([1, 6, 3, 6], game.get_code())
        self.assertEqual(black, 0)
        self.assertEqual(white, 4)

        black, white = game.check([1, 1, 1, 3], game.get_code())
        self.assertEqual(black, 0)
        self.assertEqual(white, 2)

    def test_correct_digits_and_wrong_positions_human(self):
        """
        Test if method gives correct answers (human)
            digits on correct positions and on wrong positions
        """

        game = mastermind.HumanPlayer()
        game.set_code([1, 2, 3, 4])
        black, white = game.check([2, 1, 3, 4], game.get_code())
        self.assertEqual(black, 2)
        self.assertEqual(white, 2)

        black, white = game.check([4, 2, 3, 1], game.get_code())
        self.assertEqual(black, 2)
        self.assertEqual(white, 2)

        black, white = game.check([4, 4, 4, 4], game.get_code())
        self.assertEqual(black, 1)
        self.assertEqual(white, 0)

    def test_correct_digits_and_wrong_positions_computer(self):
        """
        Test if method gives correct answers (computer)
            digits on correct positions and on wrong positions
        """

        game = mastermind.HumanPlayer()
        game.set_code([6, 4, 2, 5])
        black, white = game.check([2, 4, 3, 4], game.get_code())
        self.assertEqual(black, 1)
        self.assertEqual(white, 1)

        black, white = game.check([2, 4, 6, 5], game.get_code())
        self.assertEqual(black, 2)
        self.assertEqual(white, 2)

        black, white = game.check([5, 4, 2, 5], game.get_code())
        self.assertEqual(black, 3)
        self.assertEqual(white, 0)

    def test_appropriate_code(self):
        """Test user input guess"""

        game = mastermind.HumanPlayer()
        game2 = mastermind.ComputerPlayer()

        'too long'
        myinput = '12345'

        with self.assertRaises(mastermind.InappropriateCodeException) as context:
            game.appropriate_code(myinput)
            game2.appropriate_code(myinput)

        self.assertTrue('Kod musi mieć długość = 4.' in str(context.exception))

        'too short'
        myinput = '123'

        with self.assertRaises(mastermind.InappropriateCodeException) as context:
            game.appropriate_code(myinput)
            game2.appropriate_code(myinput)

        self.assertTrue('Kod musi mieć długość = 4.' in str(context.exception))

        'not digits'
        myinput = 'asdas'

        with self.assertRaises(mastermind.InappropriateCodeException) as context:
            game.appropriate_code(myinput)
            game2.appropriate_code(myinput)

        self.assertTrue('Kod musi składać się z samych cyfr.' in str(context.exception))

        'special chars'
        myinput = ' $@_+'

        with self.assertRaises(mastermind.InappropriateCodeException) as context:
            game.appropriate_code(myinput)
            game2.appropriate_code(myinput)

        self.assertTrue('Kod musi składać się z samych cyfr.' in str(context.exception))

        'digit out of range'
        myinput = '1228'

        with self.assertRaises(mastermind.InappropriateCodeException) as context:
            game.appropriate_code(myinput)
            game2.appropriate_code(myinput)

        self.assertTrue('Dozwolone tylko cyfry od 1 do 6.' in str(context.exception))

    def test_computer_loop(self):
        """
        Test if computer game loop works correctly.
        """

        s = 0
        for i in range(100):
            game = mastermind.ComputerPlayer()
            self.assertEqual(game.play_mastermind(), True)
            s += game.get_count_guesses()
        print("Średnia ilość strzałów potrzebnych od odgadnięcia kodu\n Sprawność: ", s/100)