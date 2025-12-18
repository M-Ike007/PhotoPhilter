# TODO this file will have a class that is a tkinter window that lets the user finetune their photo sorting.
# important is the amount of photos. If it is generally small, we can use some type of interface.
# if it is a lot, maybe a different type of interface is required?
# lets start with an interface for generally normal/small sized assorted photos
# there should be an execute button that deletes the actual photos and keeps the rest.
# there should be something done with the decide later as well...
from tkinter import *
from PIL import Image, ImageTk
import json

import PhotoPanel as PPan


class App(Tk):
    def __init__(self):
        super().__init__()

        self.title("Final Sort")
        self.iconbitmap('Media/favicon.ico')

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # define shrink margins
        margin_x = 100
        margin_y = 100

        # Define window size
        window_width = screen_width - margin_x
        window_height = screen_height - margin_y

        # Set window size dynamically
        self.geometry(f"{window_width}x{window_height}+{int(margin_x / 2)}+{int(margin_y / 4)}")
        self.grid()

        self.leftpanel = PPan.Panel()
        self.rightpanel = PPan.Panel()
        self.left_panel = PPan.Panel('keep')
        self.right_panel = PPan.Panel('discard')

        self.left_panel.grid(row=1, column=0)
        self.right_panel.grid(row=1, column=2)

        self.title_left = Label(self, text='Keep', font=('Helvetica', 12))
        self.title_right = Label(self, text='Discard', font=('Helvetica', 12))

        self.title_left.grid(row=0, column=0)
        self.title_right.grid(row=0, column=2)

        self.button_switch = Button(self, text='Move', bg='gray')
        self.button_switch.grid(row=1, column=1, padx=10, pady=15)


        self.leftpanel.grid(row=0, column=0)
        self.rightpanel.grid(row=0, column=2)

        self.button_later = Button(self, text='Later', bg='orange')
        self.button_later.grid(row=1, column=1, padx=10, pady=15)


if __name__ == '__main__':
    final_sort = App()
    final_sort.mainloop()
