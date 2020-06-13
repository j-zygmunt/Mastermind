"""Mastermind game assets"""

import tkinter


class Assets:
    """Stores assets"""
    # pylint: disable=too-few-public-methods

    @staticmethod
    def load():
        """Loads assets from disk"""
        Assets.WINDOW_BACKGROUND = tkinter.PhotoImage(file="graphics/bg/background.png")
        Assets.PLAY_BUTTON = tkinter.PhotoImage(file='graphics/buttons/play.png')
        Assets.COMPUTER_BUTTON = tkinter.PhotoImage(file='graphics/buttons/computer.png')
        Assets.HUMAN_BUTTON = tkinter.PhotoImage(file='graphics/buttons/human.png')
        Assets.CHECK_BUTTON = tkinter.PhotoImage(file='graphics/buttons/check.png')
        Assets.RESTART_BUTTON_END = tkinter.PhotoImage(file='graphics/buttons/restart.png')
        Assets.RESTART_BUTTON_WINDOW = tkinter.PhotoImage(file='graphics/buttons/restart2.png')
        Assets.CLOSE_BUTTON = tkinter.PhotoImage(file='graphics/buttons/close.png')
        Assets.MENU_BUTTON = tkinter.PhotoImage(file='graphics/buttons/menu.png')
        Assets.BACK_BUTTON = tkinter.PhotoImage(file='graphics/buttons/back.png')
        Assets.RANDOM_CODE_BUTTON = tkinter.PhotoImage(file='graphics/buttons/random.png')
        Assets.YOUR_CODE_BUTTON = tkinter.PhotoImage(file='graphics/buttons/your.png')
        Assets.ENTER_BUTTON = tkinter.PhotoImage(file='graphics/buttons/enter.png')
        Assets.NEXT_BUTTON = tkinter.PhotoImage(file="graphics/buttons/next.png")
        Assets.YOUR_GUESS = tkinter.PhotoImage(file='graphics/labels/your_guesses.png')
        Assets.COMPUTER_GUESS = tkinter.PhotoImage(file='graphics/labels/computer_guesses.png')
        Assets.ANSWERS = tkinter.PhotoImage(file='graphics/labels/answers.png')
        Assets.GUESS = tkinter.PhotoImage(file='graphics/labels/guess.png')
        Assets.CODE = tkinter.PhotoImage(file='graphics/labels/code.png')