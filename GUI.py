"""
This module contains the mastermind game interface.

CLasses:
MastermindInterface
    This class allows you to play in 3 ways:
        human - you have to break the randomly generated code.
        computer mode1 - computer have to break the randomly generated code.
        computer mode2 - computer have to break your code.
"""

import tkinter
import mastermind


class MastermindInterface(tkinter.Frame):   # pylint: disable=too-many-ancestors, disable=too-many-instance-attributes
    """
    This class allows you to play in 3 ways:

        human - you have to break the randomly generated code.
        computer mode1 - computer have to break the randomly generated code.
        computer mode2 - computer have to break your code.

    Parameters:
    main : Tk
        main window

    Attributes:
    main_window
        main application window
    current_game
        actual game mode
    entry
        guess and code entry box
    guess
        current guess
    code
        current code
    output_dots
        current code answer
    remaining_attempts
        label that displays how many attempts left
    check_button
        guess check button
    enter_button
        code enter button
    back_button
        back button
    error_popup = None
        popup window that appears when error occurs
    endgame_popup
        popup window that appears when the game ends
    var
        variable that stores user entry
    and a lot of graphics

    Methods:
    clear_current_window:
        clear window
    start:
        create start window


    """

    def __init__(self, main):
        tkinter.Frame.__init__(self, main)
        self.__main_window = main
        self.__main_window.geometry("412x520")
        self.__main_window.resizable(0, 0)
        self.__main_window.title("Mastermind")

        self.__window_background = \
            tkinter.PhotoImage(file='graphics/bg/background.png')
        self.__play_button_img = \
            tkinter.PhotoImage(file='graphics/buttons/play.png')
        self.__computer_button_img = \
            tkinter.PhotoImage(file='graphics/buttons/computer.png')
        self.__human_button_img = \
            tkinter.PhotoImage(file='graphics/buttons/human.png')
        self.__check_button_img = \
            tkinter.PhotoImage(file='graphics/buttons/check.png')
        self.__restart_button_end_img = \
            tkinter.PhotoImage(file='graphics/buttons/restart.png')
        self.__restart_button_window_img = \
            tkinter.PhotoImage(file='graphics/buttons/restart2.png')
        self.__close_button_img = \
            tkinter.PhotoImage(file='graphics/buttons/close.png')
        self.__menu_button_img = \
            tkinter.PhotoImage(file='graphics/buttons/menu.png')
        self.__back_button_img = \
            tkinter.PhotoImage(file='graphics/buttons/back.png')
        self.__random_code_button_img = \
            tkinter.PhotoImage(file='graphics/buttons/random.png')
        self.__your_code_button_img = \
            tkinter.PhotoImage(file='graphics/buttons/your.png')
        self.__enter_button_img = \
            tkinter.PhotoImage(file='graphics/buttons/enter.png')
        self.__next_button_img = \
            tkinter.PhotoImage(file="graphics/buttons/next.png")
        self.__your_guesses_img = \
            tkinter.PhotoImage(file='graphics/labels/your_guesses.png')
        self.__computer_guesses_img = \
            tkinter.PhotoImage(file='graphics/labels/computer_guesses.png')
        self.__answers_img = \
            tkinter.PhotoImage(file='graphics/labels/answers.png')
        self.__guess_here_img = \
            tkinter.PhotoImage(file='graphics/labels/guess.png')
        self.__code_here_img = \
            tkinter.PhotoImage(file='graphics/labels/code.png')

        self.__current_game = None
        self.__entry = None
        self.__guess = None
        self.__code = None
        self.__output_dots = None
        self.__remaining_attempts = None
        self.__check_button = None
        self.__enter_button = None
        self.__back_button = None
        self.__error_popup = None
        self.__endgame_popup = None
        self.__var = tkinter.StringVar()
        self.start()

    def clear_current_window(self):
        """Destroy all of the objects of the current window."""

        objects = self.__main_window.place_slaves()
        for obj in objects:
            obj.destroy()

    def start(self):
        """
        Create start window.

            play_button - go to choose_player window
        """

        self.clear_current_window()
        window_background_label = tkinter.Label(self.__main_window)
        window_background_label.config(image=self.__window_background)
        window_background_label.place(relwidth=1, relheight=1)
        play_button = tkinter.Button(self.__main_window,
                                     command=self.choose_player,
                                     image=self.__play_button_img)
        play_button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    def choose_player(self):
        """
        Here you can choose the game mode.

            computer_button - let computer play
            human_button - play by yourself
            back_button - back to start window
        """

        self.clear_current_window()
        window_background_label = tkinter.Label(self.__main_window)
        window_background_label.config(image=self.__window_background)
        window_background_label.place(relwidth=1, relheight=1)

        computer_button = tkinter.Button(self.__main_window,
                                         image=self.__computer_button_img,
                                         command=self.choose_computer_player_mode)
        computer_button.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)
        human_button = tkinter.Button(self.__main_window,
                                      command=self.play_as_human,
                                      image=self.__human_button_img)
        human_button.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)
        self.__back_button = tkinter.Button(self.__main_window,
                                            command=self.start,
                                            image=self.__back_button_img)
        self.__back_button.place(relx=0.98, rely=0.02, anchor=tkinter.NE)

    def play_as_human(self):
        """
        Here you can try to break the code by yourself.

            remaining_attempts - label that displays how many attempts left
            guess_frame - frame that contains text box where you enter your guess
            check_button - check if the guess is valid(get_guess method)
            restart_button - restart the game(restart method)
            back_button - back to choose_player window
        """

        self.clear_current_window()
        window_background_label = tkinter.Label(self.__main_window)
        window_background_label.config(image=self.__window_background)
        window_background_label.place(relwidth=1, relheight=1)

        self.__current_game = mastermind.HumanPlayer()
        self.__current_game.set_random_code()
        remaining = mastermind.MAX_GUESSES - self.__current_game.get_count_guesses()
        self.__remaining_attempts = tkinter.Label(self.__main_window, font='Calibri 13 bold',
                                                  text=str(remaining), bg='grey')
        self.__remaining_attempts.config(width=2, borderwidth=2, relief="ridge")
        self.__remaining_attempts.place(relx=0.05, rely=0.05)
        guesses_label = tkinter.Label(self.__main_window, image=self.__your_guesses_img)
        guesses_label.place(relx=0.3, rely=0.15, anchor=tkinter.CENTER)
        answers_label = tkinter.Label(self.__main_window, image=self.__answers_img)
        answers_label.place(relx=0.7, rely=0.15, anchor=tkinter.CENTER)
        guess_frame = tkinter.Frame(self.__main_window, height=10, width=15, bg='#707271')
        self.__entry = tkinter.Entry(guess_frame, textvariable=self.__var)
        self.__entry.config(width=7, font="Calibri 13 bold", justify='center')
        self.__entry.grid(row=0, column=1)
        here_label = tkinter.Label(guess_frame, image=self.__guess_here_img, bg='#707271')
        here_label.grid(row=0, column=0)
        guess_frame.place(relx=0.5, rely=0.98, anchor=tkinter.S)
        self.__check_button = tkinter.Button(self.__main_window,
                                             command=self.get_guess,
                                             image=self.__check_button_img)
        self.__check_button.place(relx=0.85, rely=0.98, anchor=tkinter.S)
        self.__main_window.bind('<Return>', lambda event=None: self.get_guess())
        restart_button_window = tkinter.Button(self.__main_window,
                                               command=lambda: self.restart(0),
                                               image=self.__restart_button_window_img)
        restart_button_window.place(relx=0.15, rely=0.98, anchor=tkinter.S)
        self.__back_button = tkinter.Button(self.__main_window,
                                            command=lambda: self.back(0),
                                            image=self.__back_button_img)
        self.__back_button.place(relx=0.98, rely=0.02, anchor=tkinter.NE)

    def get_guess(self):
        """
        Check if the guess is valid
            if not - error_popup occurs
                contains:
                close_button - close error_popup
            if it is - add_guess method displays current guess and answer

            endgame_popup - occurs when the game ends (win,lose)
                contains:
                menu_button - go to menu (menu method)
                close_button - terminate application (quit method)
                restart_button - restart the game (restart method)
        """

        try:
            self.__guess = self.__current_game.appropriate_code(self.__var.get())

        except mastermind.InappropriateCodeException as error:
            self.__error_popup = tkinter.Toplevel()
            self.__error_popup.title("Error")
            self.__error_popup.config(bg='#707271')
            self.__error_popup.geometry('200x80')
            self.__error_popup.resizable(0, 0)
            self.__error_popup.bind('<Return>', lambda event=None: self.__error_popup.destroy())
            label = tkinter.Label(self.__error_popup, text=error, bg='#707271')
            label.pack(pady=10)
            close_button = tkinter.Button(self.__error_popup,
                                          command=self.__error_popup.destroy,
                                          image=self.__close_button_img)
            close_button.place(x=72.5, y=45)
            self.__error_popup.mainloop()
            return

        self.__current_game.increment_count_guesses()
        self.__remaining_attempts.destroy()
        remaining = mastermind.MAX_GUESSES - self.__current_game.get_count_guesses()
        self.__remaining_attempts = tkinter.Label(self.__main_window, bg='#707271',
                                                  font='Calibri 13 bold', text=str(remaining))
        self.__remaining_attempts.config(width=2, borderwidth=2, relief="ridge")
        self.__remaining_attempts.place(relx=0.05, rely=0.05)
        self.__output_dots = self.__current_game.check(self.__guess, self.__current_game.get_code())
        self.add_guess(self.__current_game.get_count_guesses(), 0)

        if self.__output_dots[0] == 4 or remaining == 0:
            self.__entry.config(state='disabled')
            self.__check_button.config(state='disabled')
            self.__main_window.unbind('<Return>')
            self.__endgame_popup = tkinter.Toplevel()
            self.__endgame_popup.config(bg='#707271')
            self.__endgame_popup.geometry('200x80')
            self.__endgame_popup.resizable(0, 0)
            self.__endgame_popup.bind('<Return>', lambda event=None: self.__endgame_popup.destroy())

            if self.__output_dots[0] == 4:
                self.__endgame_popup.title(":)")
                text = 'Congratulations\nYou have won in ' + \
                       str(self.__current_game.get_count_guesses()) + 'th attempt'
                label = tkinter.Label(self.__endgame_popup, bg='#707271', text=text)
                label.pack(pady=10)

            else:
                self.__endgame_popup.title(":(")
                code = (''.join('%s' % char for char in self.__current_game.get_code()))
                text = 'Not this time\nThe code was: ' + code
                label = tkinter.Label(self.__endgame_popup, bg='#707271', text=text)
                label.pack(pady=10)

            close_button = tkinter.Button(self.__endgame_popup,
                                          command=self.quit,
                                          image=self.__close_button_img)
            close_button.place(x=8.75, y=45)
            menu_button = tkinter.Button(self.__endgame_popup,
                                         command=lambda: self.menu(0),
                                         image=self.__menu_button_img)
            menu_button.place(x=72.5, y=45)
            restart_button_end = tkinter.Button(self.__endgame_popup,
                                                command=lambda: self.restart(0),
                                                image=self.__restart_button_end_img)
            restart_button_end.place(x=136.25, y=45)
            self.__endgame_popup.mainloop()

    def choose_computer_player_mode(self):
        """
        Here you can choose if the code will be generated randomly or entered by you.

            random_code_button - random code
            your_code_button - your code
            back_button - back to choose_player window
        """

        self.clear_current_window()
        window_background_label = tkinter.Label(self.__main_window)
        window_background_label.config(image=self.__window_background)
        window_background_label.place(relwidth=1, relheight=1)

        self.__current_game = mastermind.ComputerPlayer()
        random_code_button = tkinter.Button(self.__main_window,
                                            image=self.__random_code_button_img,
                                            command=self.play_as_computer_m1)
        random_code_button.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)
        your_code_button = tkinter.Button(self.__main_window,
                                          image=self.__your_code_button_img,
                                          command=self.play_as_computer_m2)
        your_code_button.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)
        self.__back_button = tkinter.Button(self.__main_window,
                                            command=self.choose_player,
                                            image=self.__back_button_img)
        self.__back_button.place(relx=0.98, rely=0.02, anchor=tkinter.NE)

    def play_as_computer_m1(self):
        """
        Here computer tries to break the random code.

            remaining_attempts - label that displays how many attempts left
            code_frame - frame that contains label with current code
            check_button - check the next computer guess(get_computer_guess)
            restart_button - restart the game(restart method)
            back_button - back to choose_computer_player_mode window
        """

        self.clear_current_window()
        window_background_label = tkinter.Label(self.__main_window)
        window_background_label.config(image=self.__window_background)
        window_background_label.place(relwidth=1, relheight=1)

        self.__current_game = mastermind.ComputerPlayer()
        remaining = mastermind.MAX_GUESSES - self.__current_game.get_count_guesses()
        self.__remaining_attempts = tkinter.Label(self.__main_window, font='Calibri 13 bold',
                                                  text=str(remaining), bg='grey')
        self.__remaining_attempts.config(width=2, borderwidth=2, relief="ridge")
        self.__remaining_attempts.place(relx=0.05, rely=0.05)
        code_label = tkinter.Label(self.__main_window, image=self.__computer_guesses_img)
        code_label.place(relx=0.3, rely=0.15, anchor=tkinter.CENTER)
        answers_label = tkinter.Label(self.__main_window, image=self.__answers_img)
        answers_label.place(relx=0.7, rely=0.15, anchor=tkinter.CENTER)
        self.__current_game.set_random_code()
        code_frame = tkinter.Frame(self.__main_window, height=10, width=15, bg='#707271')
        here_label = tkinter.Label(code_frame, image=self.__code_here_img, bg='#707271')
        here_label.grid(row=0, column=0)
        self.__code = (''.join('%s' % char for char in self.__current_game.get_code()))
        current_code = tkinter.Label(code_frame, text=self.__code, bg='#707271',
                                     font='Calibri 13 bold', justify='center')
        current_code.grid(row=0, column=1)
        code_frame.place(relx=0.5, rely=0.98, anchor=tkinter.S)
        self.__check_button = tkinter.Button(self.__main_window,
                                             image=self.__next_button_img,
                                             command=lambda: self.get_computer_guess(1))
        self.__check_button.place(relx=0.85, rely=0.98, anchor=tkinter.S)
        self.__main_window.bind('<Return>', lambda event=None: self.get_computer_guess(1))
        restart_button_window = tkinter.Button(self.__main_window,
                                               command=lambda: self.restart(1),
                                               image=self.__restart_button_window_img)
        restart_button_window.place(relx=0.15, rely=0.98, anchor=tkinter.S)
        self.__back_button = tkinter.Button(self.__main_window,
                                            image=self.__back_button_img,
                                            command=self.choose_computer_player_mode)
        self.__back_button.place(relx=0.98, rely=0.02, anchor=tkinter.NE)

    def play_as_computer_m2(self):
        """
        Here computer tries to break your code.

            remaining_attempts - label that displays how many attempts left
            code_frame - frame that contains text box where you enter your code
            check_button - check the next computer guess(get_computer_guess)
            restart_button - restart the game(restart method)
            back_button - back to choose_computer_player_mode window
        """

        self.clear_current_window()
        window_background_label = tkinter.Label(self.__main_window)
        window_background_label.config(image=self.__window_background)
        window_background_label.place(relwidth=1, relheight=1)

        self.__current_game = mastermind.ComputerPlayer()
        remaining = mastermind.MAX_GUESSES - self.__current_game.get_count_guesses()
        self.__remaining_attempts = tkinter.Label(self.__main_window, bg='grey',
                                                  font='Calibri 13 bold', text=str(remaining))
        self.__remaining_attempts.config(width=2, borderwidth=2, relief="ridge")
        self.__remaining_attempts.place(relx=0.05, rely=0.05)
        code_label = tkinter.Label(self.__main_window, image=self.__computer_guesses_img)
        code_label.place(relx=0.3, rely=0.15, anchor=tkinter.CENTER)
        answers_label = tkinter.Label(self.__main_window, image=self.__answers_img)
        answers_label.place(relx=0.7, rely=0.15, anchor=tkinter.CENTER)
        code_frame = tkinter.Frame(self.__main_window, height=10, width=15, bg='#707271')
        self.__enter_button = tkinter.Button(code_frame, command=self.get_code,
                                             image=self.__enter_button_img)
        self.__enter_button.grid(row=0, column=0)
        self.__entry = tkinter.Entry(code_frame, textvariable=self.__var, width=7,
                                     font="Calibri 13 bold", justify='center')
        self.__entry.grid(row=0, column=1)
        code_frame.place(relx=0.5, rely=0.98, anchor=tkinter.S)
        self.__check_button = tkinter.Button(self.__main_window,
                                             image=self.__next_button_img,
                                             command=lambda: self.get_computer_guess(2))
        self.__check_button.place(relx=0.85, rely=0.98, anchor=tkinter.S)
        self.__check_button.config(state='disable')
        restart_button_window = tkinter.Button(self.__main_window,
                                               command=lambda: self.restart(2),
                                               image=self.__restart_button_window_img)
        restart_button_window.place(relx=0.15, rely=0.98, anchor=tkinter.S)
        self.__back_button = tkinter.Button(self.__main_window,
                                            image=self.__back_button_img,
                                            command=lambda: self.back(1))
        self.__back_button.place(relx=0.98, rely=0.02, anchor=tkinter.NE)

    def get_computer_guess(self, mode):
        """
        Get the next computer guess using the five guess algorithm.

            endgame_popup - occurs when the game ends (always win)
                contains:
                menu_button - go to menu (menu method)
                close_button - terminate application (quit method)
                restart_button - restart the game (restart method)
        :param mode : computer game mode
        """

        self.__current_game.increment_count_guesses()
        self.__guess = (''.join('%s' % char for char in self.__current_game.get_current_guess()))
        self.__current_game.remove_guess()
        self.__remaining_attempts.destroy()
        remaining = mastermind.MAX_GUESSES - self.__current_game.get_count_guesses()
        self.__remaining_attempts = tkinter.Label(self.__main_window, bg='#707271',
                                                  font='Calibri 13 bold', text=str(remaining))
        self.__remaining_attempts.config(width=2, borderwidth=2, relief="ridge")
        self.__remaining_attempts.place(relx=0.05, rely=0.05)
        current_guess = self.__current_game.get_current_guess()
        current_code = self.__current_game.get_code()
        self.__output_dots = self.__current_game.check(current_guess, current_code)
        self.__current_game.set_response(self.__output_dots)
        self.add_guess(self.__current_game.get_count_guesses(), 1)

        if self.__output_dots[0] == 4 or remaining == 0:
            self.__check_button.config(state='disable')
            self.__main_window.unbind('<Return>')
            self.__endgame_popup = tkinter.Toplevel()
            self.__endgame_popup.config(bg='#707271')
            self.__endgame_popup.geometry('200x80')
            self.__endgame_popup.resizable(0, 0)
            self.__endgame_popup.bind('<Return>', lambda event=None: self.__endgame_popup.destroy())

            if self.__output_dots[0] == 4:
                self.__endgame_popup.title(":)")
                text = 'Congratulations\nComputer have won in ' +\
                       str(self.__current_game.get_count_guesses()) + 'th attempt'
                label = tkinter.Label(self.__endgame_popup, bg='#707271', text=text)
                label.pack(pady=10)

            else:
                self.__endgame_popup.title(":(")
                text = 'Not this time\nThe code was: ' + self.__code
                label = tkinter.Label(self.__endgame_popup, bg='#707271', text=text)
                label.pack(pady=10)
            close_button = tkinter.Button(self.__endgame_popup,
                                          command=self.quit,
                                          image=self.__close_button_img)
            close_button.place(x=8.75, y=45)
            menu_button = tkinter.Button(self.__endgame_popup,
                                         command=lambda: self.menu(mode),
                                         image=self.__menu_button_img)
            menu_button.place(x=72.5, y=45)
            restart_button_end = tkinter.Button(self.__endgame_popup,
                                                command=lambda: self.restart(mode),
                                                image=self.__restart_button_end_img)
            restart_button_end.place(x=136.25, y=45)
            self.__endgame_popup.mainloop()

        self.__current_game.remove_unlike_response()
        if len(self.__current_game.get_possible_codes()) == 1:
            last = self.__current_game.get_last_guess()
            self.__current_game.set_current_guess(last)
        else:
            self.__current_game.minimax()

    def get_code(self):
        """
        Check if the entered code is valid.
            if not - error_popup occurs
                contains:
                close_button - close error_popup
            if it is - set code
        """

        try:
            self.__code = self.__current_game.appropriate_code(self.__var.get())
            self.__current_game.set_code(self.__code)
            self.__main_window.bind('<Return>', lambda event=None: self.get_computer_guess(2))
            self.__check_button.config(state='active')

        except mastermind.InappropriateCodeException as error:
            self.__error_popup = tkinter.Toplevel()
            self.__error_popup.title("Error")
            self.__error_popup.config(bg='#707271')
            self.__error_popup.geometry('200x80')
            self.__error_popup.resizable(0, 0)
            self.__error_popup.bind('<Return>', lambda event=None: self.__error_popup.destroy())

            label = tkinter.Label(self.__error_popup, text=error, bg='#707271')
            label.pack(pady=10)

            close_button = tkinter.Button(self.__error_popup,
                                          command=self.__error_popup.destroy,
                                          image=self.__close_button_img)
            close_button.place(x=72.5, y=45)
            self.__error_popup.mainloop()
            return

        self.__enter_button.config(state='disable')
        self.__entry.config(state='disabled')

    def add_guess(self, iteration, mode):
        """
        Display the current guess and answers.

        :param iteration : current attempt
        :param mode : game mode
        """

        guess_frame = tkinter.Frame(self.__main_window, bg='grey')
        answer_frame = tkinter.Frame(self.__main_window, bg='grey')

        if mode == 0:
            guess_label = tkinter.Label(guess_frame, text=self.__var.get())
            guess_label.config(font='Calibri 12 bold', background='grey')
            guess_label.grid(row=0, column=0, padx=10, pady=0)

        if mode == 1:
            guess_label = tkinter.Label(guess_frame, text=self.__guess)
            guess_label.config(font='Calibri 12 bold', background='grey')
            guess_label.grid(row=0, column=0, padx=10, pady=0)

        for i in range(self.__output_dots[0]):
            canvas = tkinter.Canvas(answer_frame, width=7, height=7, bg='black', bd=0)
            canvas.grid(row=0, column=i + 1, padx=4, pady=4)

        for i in range(self.__output_dots[1]):
            canvas = tkinter.Canvas(answer_frame, width=7, height=7, bg='white', bd=0)
            canvas.grid(row=0, column=i + 1 + self.__output_dots[0], padx=4, pady=4)

        guess_frame.place(relx=0.3, rely=0.17 + iteration * 0.055, anchor=tkinter.CENTER)
        answer_frame.place(relx=0.7, rely=0.17 + iteration * 0.055, anchor=tkinter.CENTER)

    def restart(self, mode):
        """
        Restart current game.

        :param mode : game mode
        """

        if self.__endgame_popup is not None:
            self.__endgame_popup.destroy()

        if self.__error_popup is not None:
            self.__error_popup.destroy()

        if mode == 0:
            self.__entry.config(state='normal')
            self.__entry.delete(0, 'end')
            self.play_as_human()

        if mode == 1:
            self.play_as_computer_m1()

        if mode == 2:
            self.__entry.config(state='normal')
            self.__entry.delete(0, 'end')
            self.play_as_computer_m2()

    def quit(self):
        """Terminate application."""

        if self.__endgame_popup is not None:
            self.__endgame_popup.destroy()

        if self.__error_popup is not None:
            self.__error_popup.destroy()

        self.__main_window.destroy()

    def menu(self, mode):
        """Go to choose player window."""

        if mode in (0, 2):
            self.__entry.config(state='normal')
            self.__entry.delete(0, 'end')

        if self.__endgame_popup is not None:
            self.__endgame_popup.destroy()

        if self.__error_popup is not None:
            self.__error_popup.destroy()

        self.choose_player()

    def back(self, where):
        """Back to previous window."""

        if where == 0:
            self.__entry.config(state='normal')
            self.__entry.delete(0, 'end')
            self.choose_player()

        if where == 1:
            self.__entry.config(state='normal')
            self.__entry.delete(0, 'end')
            self.choose_computer_player_mode()


if __name__ == "__main__":
    root = tkinter.Tk()
    MastermindInterface(root)
    root.mainloop()
