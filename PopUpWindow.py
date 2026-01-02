import json
from tkinter import *
from tkinter import filedialog


huge_font = ('Helvetica', 20)
large_font = ('Helvetica', 12)
small_font = ('Helvetica', 8)
tiny_font = ('helvetica', 4)


class Popup(Tk):
    def __init__(self):
        super().__init__()

        # Define styles
        self.title("")
        self.iconbitmap('Media/favicon.ico')
        self.geometry('360x160')
        self.grid()

        self.delete_bool = False

        # define top label for directory
        self.label = Label(self, text='Are you sure you wish to \ndelete the disard pile?', font=large_font)
        self.label.grid(row=1, column=1, columnspan=3)

        # Define entry box description label
        self.label2 = Label(self, text='the corresponding photos \nwill be moved to trash', font=large_font)
        self.label2.grid(row=2, column=1, columnspan=3)

        # define directory button
        self.yes_button = Button(self, text='Yes', foreground='green',  font=small_font, command=self.click_yes)
        self.yes_button.grid(row=3, column=3, sticky='NESW', padx= 30, pady=20, ipadx=50)

        self.no_button = Button(self, text='No', foreground='red', font=small_font, command=self.click_no)
        self.no_button.grid(row=3, column=1, sticky='NESW', padx= 30, pady=20, ipadx=50)

    def click_yes(self):
            print('yes pressed')
            self.delete_bool = True
            self.quit()

    def click_no(self):
            print('no pressed')
            self.quit()

    def get_delete(self):
        return self.delete_bool


if __name__ == '__main__':
    # Define and instantiate app
    app = Popup()
    app.mainloop()

