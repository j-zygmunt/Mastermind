"""
This module contains mastermind game GUI.

CLasses:
Gui
"""

import tkinter
import mastermind


class Gui(tkinter.Frame): # pylint: disable=too-many-ancestors

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
        self.__your_answers_button_img = \
            tkinter.PhotoImage(file='graphics/buttons/your_answers.png')
        self.__enter_button_img = \
            tkinter.PhotoImage(file='graphics/buttons/enter.png')
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
        self.__window_background_label = None
        self.__var = tkinter.StringVar()
        self.__guess_frame = None
        self.__current_game = None
        self.__entry = None
        self.__guess = None
        self.__code = None
        self.__output_dots = None
        self.__remaining_attempts = None
        self.__play_button = None
        self.__check_button = None
        self.__computer_button = None
        self.__human_button = None
        self.__close_button = None
        self.__menu_button = None
        self.__restart_button_window = None
        self.__restart_button_end = None
        self.__random_code_button = None
        self.__your_code_button = None
        self.__back_button = None
        self.__your_answers_button = None
        self.__enter_button = None
        self.__error_popup = None
        self.__popup2 = None
        self.start()

    def clear_current_window(self):
        objects = self.__main_window.place_slaves()
        for obj in objects:
            obj.destroy()

    def restart(self, mode):
        if self.__popup2 is not None:
            self.__popup2.destroy()
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
        if self.__popup2 is not None:
            self.__popup2.destroy()
        if self.__error_popup is not None:
            self.__error_popup.destroy()
        self.__main_window.destroy()

    def menu(self):
        if self.__popup2 is not None:
            self.__popup2.destroy()
        if self.__error_popup is not None:
            self.__error_popup.destroy()
        self.choose_player()

    def back(self, where):
        if where == 0:
            self.__entry.delete(0, 'end')
            self.choose_player()

    def start(self):
        self.clear_current_window()
        window_background_label = tkinter.Label(self.__main_window)
        window_background_label.config(image=self.__window_background)
        window_background_label.place(relwidth=1, relheight=1)
        play_button = tkinter.Button(self.__main_window, command=self.choose_player)
        play_button.config(image=self.__play_button_img)
        play_button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    def choose_player(self):
        self.clear_current_window()
        self.__window_background_label = tkinter.Label(self.__main_window)
        self.__window_background_label.config(image=self.__window_background)
        self.__window_background_label.place(relwidth=1, relheight=1)
        self.__computer_button = tkinter.Button(self.__main_window, command=self.choose_computer_player_mode,
                                                image=self.__computer_button_img)
        self.__computer_button.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)
        self.__human_button = tkinter.Button(self.__main_window, command=self.play_as_human,
                                             image=self.__human_button_img)
        self.__human_button.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)
        self.__back_button = tkinter.Button(self.__main_window, command=self.start, image=self.__back_button_img)
        self.__back_button.place(relx=0.98, rely=0.02, anchor=tkinter.NE)

    def play_as_human(self):
        self.clear_current_window()
        self.__window_background_label = tkinter.Label(self.__main_window)
        self.__window_background_label.config(image=self.__window_background)
        self.__window_background_label.place(relwidth=1, relheight=1)
        self.__current_game = mastermind.HumanPlayer()
        self.__current_game.set_random_code()
        remaining = mastermind.MAX_GUESSES - self.__current_game.get_count_guesses()
        self.__remaining_attempts = tkinter.Label(self.__main_window, bg='grey', font='Calibri 13 bold',
                                                  text=str(remaining))
        self.__remaining_attempts.config(width=2, borderwidth=2, relief="ridge")
        self.__remaining_attempts.place(relx=0.05, rely=0.05)
        guesses_label = tkinter.Label(self.__main_window, image=self.__your_guesses_img)
        guesses_label.place(relx=0.3, rely=0.15, anchor=tkinter.CENTER)
        answers_label = tkinter.Label(self.__main_window, image=self.__answers_img)
        answers_label.place(relx=0.7, rely=0.15, anchor=tkinter.CENTER)
        self.__guess_frame = tkinter.Frame(self.__main_window, height=10, width=15, bg='#707271')
        self.__entry = tkinter.Entry(self.__guess_frame, textvariable=self.__var)
        self.__entry.config(width=7, font="Calibri 13 bold", justify='center')
        here_label = tkinter.Label(self.__guess_frame, image=self.__guess_here_img, bg='#707271')
        here_label.grid(row=0, column=0)
        self.__entry.grid(row=0, column=1)
        self.__guess_frame.place(relx=0.5, rely=0.98, anchor=tkinter.S)
        self.__check_button = tkinter.Button(self.__main_window, command=self.get_guess, image=self.__check_button_img)
        self.__main_window.bind('<Return>', lambda event=None: self.get_guess())
        self.__check_button.place(relx=0.85, rely=0.98, anchor=tkinter.S)
        self.__restart_button_window = tkinter.Button(self.__main_window, command=lambda: self.restart(0),
                                                      image=self.__restart_button_window_img)
        self.__restart_button_window.place(relx=0.15, rely=0.98, anchor=tkinter.S)
        self.__back_button = tkinter.Button(self.__main_window, command=lambda: self.back(0),
                                            image=self.__back_button_img)
        self.__back_button.place(relx=0.98, rely=0.02, anchor=tkinter.NE)

    def choose_computer_player_mode(self):
        self.clear_current_window()
        self.__window_background_label = tkinter.Label(self.__main_window)
        self.__window_background_label.config(image=self.__window_background)
        self.__window_background_label.place(relwidth=1, relheight=1)
        self.__current_game = mastermind.ComputerPlayer()
        self.__random_code_button = tkinter.Button(self.__main_window, image=self.__random_code_button_img, command=self.play_as_computer_m1)
        self.__random_code_button.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)
        self.__your_code_button = tkinter.Button(self.__main_window, image=self.__your_code_button_img, command=self.play_as_computer_m2)
        self.__your_code_button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        self.__your_answers_button = tkinter.Button(self.__main_window, image=self.__your_answers_button_img, command=lambda: self.play_as_computer(3))
        self.__your_answers_button.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)
        self.__back_button = tkinter.Button(self.__main_window, command=self.choose_player, image=self.__back_button_img)
        self.__back_button.place(relx=0.98, rely=0.02, anchor=tkinter.NE)

    def play_as_computer_m1(self):
        self.clear_current_window()
        self.__window_background_label = tkinter.Label(self.__main_window)
        self.__window_background_label.config(image=self.__window_background)
        self.__window_background_label.place(relwidth=1, relheight=1)
        self.__current_game = mastermind.ComputerPlayer()
        remaining = mastermind.MAX_GUESSES - self.__current_game.get_count_guesses()
        self.__remaining_attempts = tkinter.Label(self.__main_window, bg='grey', font='Calibri 13 bold',
                                                  text=str(remaining))
        self.__remaining_attempts.config(width=2, borderwidth=2, relief="ridge")
        self.__remaining_attempts.place(relx=0.05, rely=0.05)
        code_label = tkinter.Label(self.__main_window, image=self.__computer_guesses_img)
        code_label.place(relx=0.3, rely=0.15, anchor=tkinter.CENTER)
        answers_label = tkinter.Label(self.__main_window, image=self.__answers_img)
        answers_label.place(relx=0.7, rely=0.15, anchor=tkinter.CENTER)
        self.__current_game.set_random_code()
        current_frame = tkinter.Frame(self.__main_window, height=10, width=15, bg='#707271')
        here_label = tkinter.Label(current_frame, image=self.__code_here_img, bg='#707271')
        here_label.grid(row=0, column=0)
        self.__code = ""
        for element in self.__current_game.get_code():
            self.__code += str(element)
        current_code = tkinter.Label(current_frame, text=self.__code, bg='#707271', font='Calibri 13 bold', justify='center')
        current_code.grid(row=0, column=1)
        current_frame.place(relx=0.5, rely=0.98, anchor=tkinter.S)
        self.__check_button = tkinter.Button(self.__main_window, command=lambda: self.get_computer_guess(1), image=self.__check_button_img)
        self.__main_window.bind('<Return>', lambda event=None: self.get_computer_guess(1))
        self.__check_button.place(relx=0.85, rely=0.98, anchor=tkinter.S)
        self.__restart_button_window = tkinter.Button(self.__main_window, command=lambda: self.restart(1),
                                                      image=self.__restart_button_window_img)
        self.__restart_button_window.place(relx=0.15, rely=0.98, anchor=tkinter.S)
        self.__back_button = tkinter.Button(self.__main_window, command=self.choose_computer_player_mode, image=self.__back_button_img)
        self.__back_button.place(relx=0.98, rely=0.02, anchor=tkinter.NE)

    def play_as_computer_m2(self):
        self.clear_current_window()
        self.__window_background_label = tkinter.Label(self.__main_window)
        self.__window_background_label.config(image=self.__window_background)
        self.__window_background_label.place(relwidth=1, relheight=1)
        self.__current_game = mastermind.ComputerPlayer()
        remaining = mastermind.MAX_GUESSES - self.__current_game.get_count_guesses()
        self.__remaining_attempts = tkinter.Label(self.__main_window, bg='grey', font='Calibri 13 bold',
                                                  text=str(remaining))
        self.__remaining_attempts.config(width=2, borderwidth=2, relief="ridge")
        self.__remaining_attempts.place(relx=0.05, rely=0.05)
        code_label = tkinter.Label(self.__main_window, image=self.__computer_guesses_img)
        code_label.place(relx=0.3, rely=0.15, anchor=tkinter.CENTER)
        answers_label = tkinter.Label(self.__main_window, image=self.__answers_img)
        answers_label.place(relx=0.7, rely=0.15, anchor=tkinter.CENTER)
        self.__guess_frame = tkinter.Frame(self.__main_window, height=10, width=15, bg='#707271')
        self.__entry = tkinter.Entry(self.__guess_frame, textvariable=self.__var, width=7, font="Calibri 13 bold", justify='center')
        self.__enter_button = tkinter.Button(self.__guess_frame, image=self.__enter_button_img, command=self.get_code)
        self.__enter_button.grid(row=0, column=0)
        self.__entry.grid(row=0, column=1)
        self.__guess_frame.place(relx=0.5, rely=0.98, anchor=tkinter.S)
        self.__check_button = tkinter.Button(self.__main_window, command=lambda: self.get_computer_guess(2), image=self.__check_button_img)
        self.__check_button.place(relx=0.85, rely=0.98, anchor=tkinter.S)
        self.__check_button.config(state='disable')
        self.__restart_button_window = tkinter.Button(self.__main_window, command=lambda: self.restart(2),
                                                      image=self.__restart_button_window_img)
        self.__restart_button_window.place(relx=0.15, rely=0.98, anchor=tkinter.S)
        self.__back_button = tkinter.Button(self.__main_window, command=self.choose_computer_player_mode, image=self.__back_button_img)
        self.__back_button.place(relx=0.98, rely=0.02, anchor=tkinter.NE)

    def get_computer_guess(self, mode):
        self.__current_game.increment_count_guesses()
        self.__guess = ""
        for element in self.__current_game.get_current_guess():
            self.__guess += str(element)
        self.__current_game.remove_guess()
        self.__remaining_attempts.destroy()
        remaining = mastermind.MAX_GUESSES - self.__current_game.get_count_guesses()
        self.__remaining_attempts = tkinter.Label(self.__main_window, bg='#707271', font='Calibri 13 bold',
                                                  text=str(remaining))
        self.__remaining_attempts.config(width=2, borderwidth=2, relief="ridge")
        self.__remaining_attempts.place(relx=0.05, rely=0.05)
        current_guess = self.__current_game.get_current_guess()
        current_code = self.__current_game.get_code()
        self.__output_dots = self.__current_game.check(current_guess, current_code)
        self.__current_game.set_response(self.__output_dots)
        self.add_guess(self.__current_game.get_count_guesses(), 1)
        if self.__output_dots[0] == 4 or self.__current_game.get_count_guesses() > mastermind.MAX_GUESSES - 1:
            self.__check_button.config(state='disable')
            self.__main_window.unbind('<Return>')
            self.__popup2 = tkinter.Toplevel()
            self.__popup2.config(bg='#707271')
            self.__popup2.geometry('200x80')
            self.__popup2.resizable(0, 0)
            self.__popup2.bind('<Return>', lambda event=None: self.__popup2.destroy())
            if self.__output_dots[0] == 4:
                self.__popup2.title(":)")
                label = tkinter.Label(self.__popup2, bg='#707271', text='Congratulations\nComputer have won in ' + str(
                    self.__current_game.get_count_guesses()) + 'th attempt')
                label.pack(pady=10)
            else:
                self.__popup2.title(":(")
                label = tkinter.Label(self.__popup2, bg='#707271', text='Not this time\nThe code was: ' + self.__code)
                label.pack(pady=10)
            self.__close_button = tkinter.Button(self.__popup2, command=self.quit, image=self.__close_button_img)
            self.__close_button.place(x=8.75, y=45)
            self.__menu_button = tkinter.Button(self.__popup2, command=self.menu, image=self.__menu_button_img)
            self.__menu_button.place(x=72.5, y=45)
            self.__restart_button_end = tkinter.Button(self.__popup2, command=lambda: self.restart(mode),
                                                       image=self.__restart_button_end_img)
            self.__restart_button_end.place(x=136.25, y=45)
            self.__popup2.mainloop()

        self.__current_game.remove_unlike_response()
        if len(self.__current_game.get_possible_codes()) == 1:
            last = self.__current_game.get_last_guess()
            self.__current_game.set_current_guess(last)
        else:
            self.__current_game.minimax()

    def get_code(self):
        try:
            user_input = self.__var.get()
            self.__code = self.__current_game.appropriate_code(user_input)
            self.__current_game.set_code(self.__code)
            self.__main_window.bind('<Return>', lambda event=None: self.get_computer_guess(2))
            self.__check_button.config(state='active')
        except mastermind.InappropriateCodeException as error:
            self.__error_popup = tkinter.Toplevel()
            self.__error_popup.title("Error")
            self.__error_popup.config(bg='#707271')
            self.__error_popup.geometry('200x80')
            self.__error_popup.resizable(0, 0)
            label = tkinter.Label(self.__error_popup, text=error, bg='#707271')
            label.pack(pady=10)
            self.__close_button = tkinter.Button(self.__error_popup, command=self.__error_popup.destroy,
                                                 image=self.__close_button_img)
            self.__error_popup.bind('<Return>', lambda event=None: self.__error_popup.destroy())
            self.__close_button.place(x=72.5, y=45)
            self.__error_popup.mainloop()
            return
        self.__enter_button.config(state='disable')
        self.__entry.config(state='disabled')

    def get_guess(self):
        try:
            user_input = self.__var.get()
            self.__guess = self.__current_game.appropriate_code(user_input)
        except mastermind.InappropriateCodeException as error:
            self.__error_popup = tkinter.Toplevel()
            self.__error_popup.title("Error")
            self.__error_popup.config(bg='#707271')
            self.__error_popup.geometry('200x80')
            self.__error_popup.resizable(0, 0)
            label = tkinter.Label(self.__error_popup, text=error, bg='#707271')
            label.pack(pady=10)
            self.__close_button = tkinter.Button(self.__error_popup, command=self.__error_popup.destroy,
                                                 image=self.__close_button_img)
            self.__error_popup.bind('<Return>', lambda event=None: self.__error_popup.destroy())
            self.__close_button.place(x=72.5, y=45)
            self.__error_popup.mainloop()
            return
        self.__current_game.increment_count_guesses()
        self.__remaining_attempts.destroy()
        remaining = mastermind.MAX_GUESSES - self.__current_game.get_count_guesses()
        self.__remaining_attempts = tkinter.Label(self.__main_window, bg='#707271', font='Calibri 13 bold',
                                                  text=str(remaining))
        self.__remaining_attempts.config(width=2, borderwidth=2, relief="ridge")
        self.__remaining_attempts.place(relx=0.05, rely=0.05)
        self.__output_dots = self.__current_game.check(self.__guess, self.__current_game.get_code())
        self.add_guess(self.__current_game.get_count_guesses(), 0)
        if self.__output_dots[0] == 4 or self.__current_game.get_count_guesses() > mastermind.MAX_GUESSES - 1:
            self.__entry.config(state='disabled')
            self.__check_button.config(state='disabled')
            self.__main_window.unbind('<Return>')
            self.__popup2 = tkinter.Toplevel()
            self.__popup2.config(bg='#707271')
            self.__popup2.geometry('200x80')
            self.__popup2.resizable(0, 0)
            self.__popup2.bind('<Return>', lambda event=None: self.__popup2.destroy())
            if self.__current_game.get_count_guesses() > self.__current_game.get_max_guesses() - 1:
                self.__popup2.title(":(")
                code = ""
                for element in self.__current_game.get_code():
                    code += str(element)
                label = tkinter.Label(self.__popup2, bg='#707271', text='Not this time\nThe code was: ' + code)
                label.pack(pady=10)
            else:
                self.__popup2.title(":)")
                label = tkinter.Label(self.__popup2, bg='#707271', text='Congratulations\nYou have won in '
                                                                        + str(self.__current_game.get_count_guesses())
                                                                        + 'th attempt')
                label.pack(pady=10)
            self.__close_button = tkinter.Button(self.__popup2, command=self.quit, image=self.__close_button_img)
            self.__close_button.place(x=8.75, y=45)
            self.__menu_button = tkinter.Button(self.__popup2, command=self.menu, image=self.__menu_button_img)
            self.__menu_button.place(x=72.5, y=45)
            self.__restart_button_end = tkinter.Button(self.__popup2, command=lambda: self.restart(0))
            self.__restart_button_end.config(image=self.__restart_button_end_img)
            self.__restart_button_end.place(x=136.25, y=45)
            self.__popup2.mainloop()

    def add_guess(self, iteration, mode):
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


if __name__ == "__main__":
    root = tkinter.Tk()
    Gui(root)
    root.mainloop()
