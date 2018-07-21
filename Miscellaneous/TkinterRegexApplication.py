import tkinter as tk
from tkinter import messagebox
import re
from random import choice


class RegularExpressionGame(tk.Frame):

    def __init__(self, master=None):
        # "super" basically replaces the call to the superclass method, or, in other words, the "tk.Frame" class,
        # which "RegularExpressionGame" is a subclass of. A superclass is a class from which another class inherits.
        # A subclass is the class that inherits from that superclass. Now, instead of having to do
        # "tk.Frame.__init__(self, master)", we can instead do "super().__init__(master)", at the advantage of not
        # having to use self in the call.
        super().__init__(master)
        self.pack()
        self.Create_Widgets()

    def Create_Widgets(self):
        self.TextBox = tk.Entry(self)
        self.Text = self.Randomness()
        self.RandomWords1 = tk.Label(self, text="Match These: \n\n"+self.Text)
        self.Text2 = self.Randomness()
        self.RandomWords2 = tk.Label(self, text = "Don't Match These: \n\n"+self.Text2)
        self.TextBox.bind('<KeyRelease>', self.Match)
        self.TextBox.pack()
        self.RandomWords1.pack(side = tk.LEFT, fill=tk.X)
        self.RandomWords2.pack(side = 'right', fill='x')

    def Match(self, event):
        print(self.TextBox.get())
        if all(re.fullmatch(self.TextBox.get(), i) for i in self.Text.split('\n')) and not all(re.fullmatch(self.TextBox.get(), i)for i in self.Text2.split('\n')):
            messagebox.showinfo('Good Job! Press "Okay" to move on!')
            self.RandomWords1['text'] = self.Randomness()
            self.RandomWords2['text'] = self.Randomness()
        else:
            print('Wrong!')

    def Randomness(self):
        y = []
        CharList = [*map(chr, range(97, 123)), ' ',]+[*map(chr, range(48,58))]
        for i in range(10):
            for u in range(20):
                y.append(choice(CharList))
            y.append('\n'*2)
        return ''.join(y)


root = tk.Tk(screenName='Game')
app = RegularExpressionGame(root)

if __name__ == '__main__':
    app.mainloop()

