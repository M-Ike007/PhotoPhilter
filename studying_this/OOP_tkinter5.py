from tkinter import *

root = Tk()
root.title('lalal')
root.iconbitmap('favicon.ico')
root.geometry('700x450')

class My_widget(Frame):
    def __init__(self, parent, label_text, button_text):
        super().__init__(master = parent)

        # set up our grid
        self.rowconfigure(0, weight=1)
        self.columnconfigure((0,1), weight=1, uniform='z')

        # create our widgets
        Label(self, text=label_text, font=('Helvetica', 18)).grid(row=0, column=0)
        Button(self, text=button_text).grid(row=0, column=1)

        self.pack()


My_widget(root, 'Text 1', 'Button 1')


root.mainloop()


# source: https://www.youtube.com/watch?v=zstcMt9_80w&list=PLfZw_tZWahjzv9-aBt_lvcmIlCtlqaFge