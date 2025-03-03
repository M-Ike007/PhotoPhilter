from tkinter import *


class App(Tk):
    def __init__(self):
        super().__init__()

        # Title, icon, size
        self.title("tkinter.com - OOP Popup Boxes")
        # icon
        self.iconbitmap('favicon.ico')
        # size window
        self.geometry('500x800')

        # create widgets
        self.my_entry = Entry(self, width=25, font=('Helvetia', 24))
        self.my_entry.pack(pady=20)

        # create a new frame to hold the buttons
        MyFrame(self)

    def clear(self):
        # clear the entry box
        self.my_entry.delete(0, END)


# Button Frame Class
class MyFrame(Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.pack()

        # define buttons
        self.button_1 = Button(self, text='1', font=('Helvetica', 24))
        self.button_2 = Button(self, text='2', font=('Helvetica', 24))
        self.button_3 = Button(self, text='3', font=('Helvetica', 24))

        self.button_4 = Button(self, text='4', font=('Helvetica', 24))
        self.button_5 = Button(self, text='5', font=('Helvetica', 24))
        self.button_6 = Button(self, text='6', font=('Helvetica', 24))

        self.button_7 = Button(self, text='7', font=('Helvetica', 24))
        self.button_8 = Button(self, text='8', font=('Helvetica', 24))
        self.button_9 = Button(self, text='9', font=('Helvetica', 24))

        self.button_0 = Button(self, text='0', font=('Helvetica', 24))
        self.button_negative = Button(self, text='+/-', font=('Helvetica', 24))
        self.button_equal = Button(self, text='=', font=('Helvetica', 24))

        self.button_plus = Button(self, text='+', font=('Helvetica', 24))
        self.button_minus = Button(self, text='-', font=('Helvetica', 24))
        self.button_multiply = Button(self, text='*', font=('Helvetica', 24))

        self.button_divide = Button(self, text='/', font=('Helvetica', 24))
        self.button_clear = Button(self, text='clear', font=('Helvetica', 24), command=parent.clear)

        # grid the buttons to the screen
        self.button_1.grid(row=0, column=0, ipadx=40, ipady=20, padx=(0, 10))
        self.button_2.grid(row=0, column=1, ipadx=40, ipady=20)
        self.button_3.grid(row=0, column=2, ipadx=40, ipady=20, padx=(10, 0))

        self.button_4.grid(row=1, column=0, ipadx=40, ipady=20, padx=(0, 10), pady=10)
        self.button_5.grid(row=1, column=1, ipadx=40, ipady=20, pady=10)
        self.button_6.grid(row=1, column=2, ipadx=40, ipady=20, padx=(10, 0), pady=10)

        self.button_7.grid(row=2, column=0, ipadx=40, ipady=20, padx=(0, 10), pady=10)
        self.button_8.grid(row=2, column=1, ipadx=40, ipady=20, pady=10)
        self.button_9.grid(row=2, column=2, ipadx=40, ipady=20, padx=(10, 0), pady=10)

        self.button_0.grid(row=3, column=0, ipadx=40, ipady=20, padx=(0, 10), pady=10)
        self.button_negative.grid(row=3, column=1, ipadx=30, ipady=20, pady=10)
        self.button_equal.grid(row=3, column=2, ipadx=40, ipady=20, padx=(10, 0), pady=10)

        self.button_plus.grid(row=4, column=0, ipadx=40, ipady=20, padx=(0, 10), pady=10)
        self.button_minus.grid(row=4, column=1, ipadx=40, ipady=20, pady=10)
        self.button_multiply.grid(row=4, column=2, ipadx=40, ipady=20, padx=(10, 0), pady=10)

        self.button_divide.grid(row=5, column=0, ipadx=40, ipady=20, padx=(0, 10))
        self.button_clear.grid(row=5, column=1, columnspan=2, ipadx=88, ipady=20, padx=(10, 0))




# Define and instantiate our app
app = App()
app.mainloop()