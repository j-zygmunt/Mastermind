import tkinter
import Mastermind


class GUI(tkinter.Frame):

    def __init__(self, root):
        tkinter.Frame.__init__(self, root)
        self.__main_window = root
        self.__main_window.geometry("412x520")
        self.__main_window.resizable(0, 0)
        self.__main_window.title("Mastermind")
        self.__window_background = tkinter.PhotoImage(file='graphics/background.png')
        self.__play_button_img = tkinter.PhotoImage(file='graphics/play.png')
        self.__computer_button_img = tkinter.PhotoImage(file='graphics/computer.png')
        self.__human_button_img = tkinter.PhotoImage(file='graphics/human.png')
        self.__check_button_img = tkinter.PhotoImage(file='graphics/check.png')
        self.__ok_button_img = tkinter.PhotoImage(file='graphics/ok.png')
        self.__your_guesses_img = tkinter.PhotoImage(file='graphics/your_guesses.png')
        self.__answers_img = tkinter.PhotoImage(file='graphics/answers.png')
        self.__guess_here_img = tkinter.PhotoImage(file='graphics/guess.png')
        self.__restart_button_end_img = tkinter.PhotoImage(file='graphics/restart.png')
        self.__restart_button_window_img = tkinter.PhotoImage(file='graphics/restart2.png')
        self.__close_button_img = tkinter.PhotoImage(file='graphics/close.png')
        self.__menu_button_img = tkinter.PhotoImage(file='graphics/menu.png')
        self.__window_background_label = None
        self.__current_game = None
        self.__var = tkinter.StringVar()
        self.__entry = None
        self.__guess = None
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
        self.__popup1 = None
        self.__popup2 = None
        self.start()

    def start(self):
        self.__window_background_label = tkinter.Label(self.__main_window, image=self.__window_background)
        self.__window_background_label.place(relwidth=1, relheight=1)
        self.__play_button = tkinter.Button(self.__main_window, text="Play Mastermind!", command=self.choose_player,
                                            image=self.__play_button_img)
        self.__play_button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    def choose_player(self):
        self.clear_current_window()
        self.__window_background_label = tkinter.Label(self.__main_window, image=self.__window_background)
        self.__window_background_label.place(relwidth=1, relheight=1)
        self.__computer_button = tkinter.Button(self.__main_window, command=self.play_as_computer,
                                                image=self.__computer_button_img)
        self.__human_button = tkinter.Button(self.__main_window, command=self.play_as_human,
                                             image=self.__human_button_img)
        self.__computer_button.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)
        self.__human_button.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

    def clear_current_window(self):
        objects = self.__main_window.place_slaves()
        for o in objects:
            o.destroy()

    def restart(self):
        pass

    def menu(self):
        pass

    def play_as_human(self):
        self.clear_current_window()
        self.__window_background_label = tkinter.Label(self.__main_window, image=self.__window_background)
        self.__window_background_label.place(relwidth=1, relheight=1)
        self.__current_game = Mastermind.HumanPlayer()
        self.__current_game.set_random_code()
        self.__remaining_attempts = tkinter.Label(self.__main_window, bg='grey', font='Calibri 13', text=str(self.__current_game.get_max_guesses() - self.__current_game.get_count_guesses()))
        self.__remaining_attempts.config(width=2, borderwidth=2, relief="ridge")
        self.__remaining_attempts.place(relx=0.05, rely=0.05)
        guesses_label = tkinter.Label(self.__main_window, image=self.__your_guesses_img)
        guesses_label.place(relx=0.3, rely=0.15, anchor=tkinter.CENTER)
        answers_label = tkinter.Label(self.__main_window, image=self.__answers_img)
        answers_label.place(relx=0.7, rely=0.15, anchor=tkinter.CENTER)
        current_frame = tkinter.Frame(self.__main_window, height=10, width=15, bg='grey')
        self.__entry = tkinter.Entry(current_frame, textvariable=self.__var, width=7, font="Calibri 13")
        here_label = tkinter.Label(current_frame, image=self.__guess_here_img, bg='grey')
        here_label.grid(row=0, column=0)
        self.__entry.grid(row=0, column=1)
        current_frame.place(relx=0.5, rely=0.98, anchor=tkinter.S)
        self.__check_button = tkinter.Button(self.__main_window, command=self.get_guess, image=self.__check_button_img)
        self.__main_window.bind('<Return>', lambda event=None: self.get_guess())
        self.__check_button.place(relx=0.85, rely=0.98, anchor=tkinter.S)
        self.__restart_button_window = tkinter.Button(self.__main_window, command=self.restart, image=self.__restart_button_window_img)
        self.__restart_button_window.place(relx=0.15, rely=0.98, anchor=tkinter.S)

    def quit(self):
        if self.__popup2 is not None:
            self.__popup2.destroy()
        if self.__popup1 is not None:
            self.__popup1.destroy()
        self.__main_window.destroy()

    def get_guess(self):
        try:
            user_input = self.__var.get()
            self.__guess = self.__current_game.appropriate_code(user_input)
        except Exception as error:
            self.__popup1 = tkinter.Toplevel()
            self.__popup1.title("Error")
            self.__popup1.config(bg='grey')
            self.__popup1.geometry('200x80')
            self.__popup1.resizable(0, 0)
            label = tkinter.Label(self.__popup1, text=error, bg='grey')
            label.pack(pady=10)
            self.__close_button = tkinter.Button(self.__popup1, command=self.__popup1.destroy, image=self.__close_button_img)
            self.__popup1.bind('<Return>', lambda event=None: self.__popup1.destroy())
            self.__close_button.place(x=72.5, y=45)
            self.__popup1.mainloop()
            return
        self.__current_game.increment_count_guesses()
        self.__remaining_attempts.destroy()
        self.__remaining_attempts = tkinter.Label(self.__main_window, bg='grey', font='Calibri 13', text=str(self.__current_game.get_max_guesses() - self.__current_game.get_count_guesses()))
        self.__remaining_attempts.config(width=2, borderwidth=2, relief="ridge")
        self.__remaining_attempts.place(relx=0.05, rely=0.05)
        self.__output_dots = self.__current_game.check(self.__guess, self.__current_game.get_code())
        self.add_guess(self.__current_game.get_count_guesses())
        if self.__output_dots[0] == 4:
            self.__popup2 = tkinter.Toplevel()
            self.__popup2.title("Congratulations!")
            self.__popup2.config(bg='grey')
            self.__popup2.geometry('200x80')
            self.__popup2.resizable(0, 0)
            label = tkinter.Label(self.__popup2, bg='grey', text='Congratulations\nYou have won in ' + str(self.__current_game.get_count_guesses()) + 'th attempt')
            label.pack(pady=10)
            self.__close_button = tkinter.Button(self.__popup2, command=self.quit, image=self.__close_button_img)
            self.__popup2.bind('<Return>', lambda event=None: self.__popup2.destroy())
            self.__close_button.place(x=8.75, y=45)
            self.__menu_button = tkinter.Button(self.__popup2, command=self.menu, image=self.__menu_button_img)
            self.__menu_button.place(x=72.5, y=45)
            self.__restart_button_end = tkinter.Button(self.__popup2, command=self.restart, image=self.__restart_button_end_img)
            self.__restart_button_end.place(x=136.25, y=45)
            self.__popup2.mainloop()
        if self.__current_game.get_count_guesses() > self.__current_game.get_max_guesses() - 1:
            self.__entry.config(state='disabled')
            self.__check_button.config(state='disable')
            self.__main_window.unbind('<Return>')
            self.__popup2 = tkinter.Toplevel()
            tkinter.Frame.__init__(self, self.__popup2)
            self.__popup2.title(":(")
            self.__popup2.config(bg='grey')
            self.__popup2.geometry('200x80')
            self.__popup2.resizable(0, 0)
            code = ""
            for element in self.__current_game.get_code():
                code += str(element)
            label = tkinter.Label(self.__popup2, bg='grey', text='Not this time\nThe code was: ' + code)
            label.pack()
            self.__close_button = tkinter.Button(self.__popup2, command=self.quit, image=self.__close_button_img)
            self.__popup2.bind('<Return>', lambda event=None: self.__popup2.destroy())
            self.__close_button.place(x=8.75, y=45)
            self.__menu_button = tkinter.Button(self.__popup2, command=self.menu, image=self.__menu_button_img)
            self.__menu_button.place(x=72.5, y=45)
            self.__restart_button_end = tkinter.Button(self.__popup2, command=self.restart, image=self.__restart_button_end_img)
            self.__restart_button_end.place(x=136.25, y=45)
            self.__popup2.mainloop()

    def add_guess(self, iter):
        guess_frame = tkinter.Frame(self.__main_window, bg='grey')
        answer_frame = tkinter.Frame(self.__main_window, bg='grey')
        guess_label = tkinter.Label(guess_frame, text=self.__var.get(), font='Calibri 12', background='grey')
        guess_label.grid(row=0, column=0, padx=10, pady=0)
        for i in range(self.__output_dots[0]):
            c = tkinter.Canvas(answer_frame, width=7, height=7, bg='black', bd=0)
            c.grid(row=0, column=i + 1, padx=4, pady=4)
        for i in range(self.__output_dots[1]):
            c = tkinter.Canvas(answer_frame, width=7, height=7, bg='white', bd=0)
            c.grid(row=0, column=i + 1 + self.__output_dots[0], padx=4, pady=4)
        guess_frame.place(relx=0.3, rely=0.17+iter*0.055, anchor=tkinter.CENTER)
        answer_frame.place(relx=0.7, rely=0.17+iter*0.055, anchor=tkinter.CENTER)

    def play_as_computer(self):
        self.destroy_current_frame()
        self.__current_frame = tkinter.Frame(self.__main_window).pack()

if __name__ == "__main__":
    root = tkinter.Tk()
    GUI(root)
    root.mainloop()
