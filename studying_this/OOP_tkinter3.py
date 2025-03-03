from tkinter import *
from tkinter import filedialog


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
        self.my_text = Text(self, width=80, height=20)
        self.my_text.pack(pady=20)

        self.my_button = Button(self, text='Open File', command=self.file)
        self.my_button.pack(pady=20)

    # create popup function
    def file(self):
        self.my_file = filedialog.askopenfilename(initialdir='',
                                                  title="Select a File",
                                                  filetypes=(("txt files", "*.txt"), ("All Files", "*.*")))
        if self.my_file:
            # open and read the file
            get_contents = open(self.my_file, 'r')
            self.my_text.insert(END, get_contents.read())

# Define and instantiate our app
app = App()
app.mainloop()