import tkinter as tk


class TicTacToe:
    __BoardState = [0, 0, 0,
                    0, 0, 0,
                    0, 0, 0]
    __CurrentPlayer = 1
    __Symbols = ['', 'X', 'O']
    __Winner = None

    def __init__(self):
        self.root = tk.Tk()

        self.root.geometry("320x360")
        self.root.resizable(False, False)
        self.root.title("Tic-Tac-Toe")

        self.topFrame = tk.Frame(self.root)
        self.topFrame.columnconfigure(0, weight=1)
        self.topFrame.columnconfigure(1, weight=1)
        self.topFrame.columnconfigure(2, weight=1)

        self.btnX = tk.Label(self.topFrame, text='X', font=('Arial', 30), fg='darkred')
        self.btnX.grid(row=0, column=0, padx=10)
        self.label = tk.Label(self.topFrame, text='Player ' + str(self.__CurrentPlayer) + ' turn',
                              font=('Arial', 22))  # font=('Arial', 22, 'underline')
        self.label.grid(row=0, column=1)
        self.btnO = tk.Label(self.topFrame, text='O', font=('Arial', 30), fg=self.root['background'])
        self.btnO.grid(row=0, column=2, padx=10)

        self.topFrame.pack(pady=5)

        self.btnFrame = tk.Frame(self.root)
        self.btnFrame.columnconfigure(0, weight=1)
        self.btnFrame.columnconfigure(1, weight=1)
        self.btnFrame.columnconfigure(2, weight=1)

        # this results in bnt1 = btn2 = ... = btn8 -> one play, player 1 won
        # for i in range(9):
        #     btn = tk.Button(self.btnFrame, text=self.__BoardState[i], height=4, width=1, command=lambda: self.play(i))
        #     btn.grid(row=int(i / 3), column=i % 3, sticky='swen')

        self.btn1 = tk.Button(self.btnFrame, text='', height=1, width=1, command=lambda: self.play(0), font=('Arial', 24))
        self.btn1.grid(row=0, column=0, sticky='swen')
        self.btn2 = tk.Button(self.btnFrame, text='', height=1, width=1, command=lambda: self.play(1), font=('Arial', 24))
        self.btn2.grid(row=0, column=1, sticky='swen')
        self.btn3 = tk.Button(self.btnFrame, text='', height=1, width=1, command=lambda: self.play(2), font=('Arial', 24))
        self.btn3.grid(row=0, column=2, sticky='swen')

        self.btn4 = tk.Button(self.btnFrame, text='', height=1, width=1, command=lambda: self.play(3), font=('Arial', 24))
        self.btn4.grid(row=1, column=0, sticky='swen')
        self.btn5 = tk.Button(self.btnFrame, text='', height=1, width=1, command=lambda: self.play(4), font=('Arial', 24))
        self.btn5.grid(row=1, column=1, sticky='swen')
        self.btn6 = tk.Button(self.btnFrame, text='', height=1, width=1, command=lambda: self.play(5), font=('Arial', 24))
        self.btn6.grid(row=1, column=2, sticky='swen')

        self.btn7 = tk.Button(self.btnFrame, text='', height=1, width=1, command=lambda: self.play(6), font=('Arial', 24))
        self.btn7.grid(row=2, column=0, sticky='swen')
        self.btn8 = tk.Button(self.btnFrame, text='', height=1, width=1, command=lambda: self.play(7), font=('Arial', 24))
        self.btn8.grid(row=2, column=1, sticky='swen')
        self.btn9 = tk.Button(self.btnFrame, text='', height=1, width=1, command=lambda: self.play(8), font=('Arial', 24))
        self.btn9.grid(row=2, column=2, sticky='swen')

        self.btnFrame.pack(fill='both', padx=20, pady=10)

        self._Buttons = [self.btn1, self.btn2, self.btn3,
                         self.btn4, self.btn5, self.btn6,
                         self.btn7, self.btn8, self.btn9]

        self.btn = tk.Button(self.root, text='Restart', height=2, width=100, command=self.restart, font=('Arial', 22),
                             borderwidth=4)
        self.btn.pack(padx=1, pady=3)

        self.root.mainloop()

    def play(self, position):
        if self.__BoardState[position] == 0 and self.__Winner is None:
            self.__BoardState[position] = self.__CurrentPlayer
            self.update_window()

    def next_player(self):
        if self.__CurrentPlayer == 2:
            self.__CurrentPlayer = 1
            self.btnX.config(fg='darkred')
            self.btnO.config(fg=self.root['background'])
        else:
            self.__CurrentPlayer = 2
            self.btnX.config(fg=self.root['background'])
            self.btnO.config(fg='darkblue')

    def update_window(self):
        for position, player in enumerate(self.__BoardState):
            self._Buttons[position].config(text=self.__Symbols[player])
            if player == 1:
                self._Buttons[position].config(fg='darkred')

            if player == 2:
                self._Buttons[position].config(fg='darkblue')

        self.check_winner()
        if self.__Winner is None:
            self.next_player()
            self.label.config(text='Player ' + str(self.__CurrentPlayer) + ' turn')

    def check_winner(self):
        if (len(set(self.__BoardState[:3])) == 1 and self.__BoardState[0] != 0) or \
           (len(set(self.__BoardState[3:6])) == 1 and self.__BoardState[3] != 0) or \
           (len(set(self.__BoardState[6:])) == 1 and self.__BoardState[6] != 0):
            self.__Winner = self.__CurrentPlayer

        elif (len(set(self.__BoardState[::3])) == 1 and self.__BoardState[0] != 0) or \
             (len(set(self.__BoardState[1::3])) == 1 and self.__BoardState[1] != 0) or \
             (len(set(self.__BoardState[2::3])) == 1 and self.__BoardState[2] != 0):
            self.__Winner = self.__CurrentPlayer

        elif (len(set(self.__BoardState[::4])) == 1 and self.__BoardState[0] != 0) or \
             (len(set(self.__BoardState[2:-2:2])) == 1 and self.__BoardState[2] != 0):
            self.__Winner = self.__CurrentPlayer

        elif 0 not in self.__BoardState:
            self.__Winner = 3

        if self.__Winner is not None:
            self.btnX.config(fg=self.root['background'])
            self.btnO.config(fg=self.root['background'])

            if self.__Winner in [1, 2]:
                colors = ['darkred', 'darkblue']
                self.label.config(text='Player ' + str(self.__Winner) + ' won', fg=colors[self.__Winner - 1])

            if self.__Winner == 3:
                self.label.config(text='Tie', fg="darkgreen")

    def restart(self):
        self.__BoardState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.__Winner = None
        self.__CurrentPlayer = 2
        self.label.config(fg='black')
        self.update_window()


if __name__ == '__main__':
    TicTacToe()
