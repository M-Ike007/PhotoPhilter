from tkinter import *


class App(Tk):
    def __init__(self):
        super().__init__()
        # title
        self.title("tkinter lol - go crazy!!!")
        # icon
        self.iconbitmap('favicon.ico')
        # size window
        self.geometry('700x450')

        self.status = True

        # create widgets
        self.my_label = Label(self, text='Hello gurls', font=('Helvetica', 24))
        self.my_label.pack(pady=20)

        self.mybutton = Button(self, text='change text', command=self.change)
        self.mybutton.pack(pady=20)

        # create a frame outside this function
        My_frame(self)

    def change(self):
        if self.status == True:
            self.my_label.config(text='you thought you ate')
            self.status = False
        else:
            self.my_label.config(text='Hello gurls')
            self.status = True


class My_frame(Frame):
    def __init__(self, parent, ):
        super().__init__(parent)

        # put on screen
        self.pack(pady=20)
        # create a few buttons
        self.my_button1 = Button(self, text='Change', command=parent.change)
        self.my_button2 = Button(self, text='Change', command=parent.change)
        self.my_button3 = Button(self, text='Change', command=parent.change)

        self.my_button1.grid(row=0, column=0, padx=10)
        self.my_button2.grid(row=0, column=1, padx=10)
        self.my_button3.grid(row=0, column=2, padx=10)





app = App()

app.mainloop()