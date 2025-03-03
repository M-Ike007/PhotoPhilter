from tkinter import *
from tkinter import messagebox


class App(Tk):
    def __init__(self):
        super().__init__()

        # Title, icon, size
        self.title("tkinter.com - OOP Popup Boxes")
        # icon
        self.iconbitmap('favicon.ico')
        # size window
        self.geometry('700x450')

        # create widgets
        self.my_label = Label(self, text='enter your name:', font=('Helvetica', 24))
        self.my_label.pack(pady=20)

        self.my_entry = Entry(self, width=30, font=('Helvetica', 30))
        self.my_entry.pack(pady=20)

        self.my_button = Button(self, text='Popup', command=self.popup)
        self.my_button.pack(pady=20)

    # create popup function
    def popup(self):
        if self.my_entry.get(): # if there is something in there, print it out, else dont
            messagebox.showinfo('hello', f"hello {self.my_entry.get()}")
        else:
            messagebox.showerror('error', 'you forgot to type, dumbass')


# define and instantiate our app
app = App()
app.mainloop()