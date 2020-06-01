import tkinter
import Mastermind


class GUI(tkinter.Frame):
    def __init__(self, root):
        tkinter.Frame.__init__(self, root)
        self.__main_window = root
        self.__main_window.geometry("250x500")
        self.__main_window.resizable(0, 0)
        self.__main_window.title("Mastermind")
        self.__current_frame = None
        self.__current_game = None
        self.__entry = None
        self.__code = None
        self.__var = tkinter.StringVar()
        self.__play_button = tkinter.Button(self.__main_window, text="Play Mastermind!", command=self.choose_player)
        self.__play_button.pack()

    def choose_player(self):
        self.__play_button.destroy()
        self.__current_frame = tkinter.Frame(self.__main_window)
        self.__current_frame.pack()
        computer_button = tkinter.Button(self.__current_frame, text="Computer", command=self.play_as_computer)
        human_button = tkinter.Button(self.__current_frame, text="Human", command=self.play_as_human)
        computer_button.pack()
        human_button.pack()

    def destroy_current_frame(self):
        self.__current_frame.destroy()
        self.__current_frame = None

    def play_as_human(self):
        self.destroy_current_frame()
        self.__current_frame = tkinter.Frame(self.__main_window).pack()
        self.__current_game = Mastermind.HumanPlayer()
        self.__current_game.set_random_code()
        label = tkinter.Label(self.__current_frame, text="Guess")
        label.pack()
        self.__entry = tkinter.Entry(self.__current_frame, textvariable=self.__var, width=35).pack()
        check_button = tkinter.Button(self.__current_frame, text="check", command=self.get_entry).pack()
        # while self.__current_game.get_count_guesses() < self.__current_game.get_max_guesses():
        # pass

    def get_entry(self):
        try:
            user_input = self.__var.get()
            self.__code = self.__current_game.appropriate_code(user_input)
        except Exception as error:
            popup = tkinter.Tk()
            popup.title("Error")
            label = tkinter.Label(popup, text=error)
            label.pack(side="top", fill="x", pady=20, padx=40)
            close_button = tkinter.Button(popup, text="Okay", command=popup.destroy)
            close_button.pack()
            popup.mainloop()

    def play_as_computer(self):
        self.destroy_current_frame()
        self.__current_frame = tkinter.Frame(self.__main_window).pack()


if __name__ == "__main__":
    root = tkinter.Tk()
    GUI(root)
    root.mainloop()
