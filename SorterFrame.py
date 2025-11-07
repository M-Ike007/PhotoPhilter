from tkinter import Frame
from tkinter import *


huge_font = ('Helvetica', 20)
large_font = ('Helvetica', 12)
small_font = ('Helvetica', 8)
tiny_font = ('helvetica', 4)


class Sorter(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.grid()

        # 4 buttons: Keep, Discard, decide Later, analyze
        self.button_keep = Button(self, text='Keep', font=large_font, command=parent.keep, bg='green')
        self.button_keep.grid(row=1, column=1, padx=10, pady=15)

        self.button_discard = Button(self, text='Discard', font=large_font, command=parent.discard, bg='red')
        self.button_discard.grid(row=1, column=2, padx=10, pady=15)

        self.button_later = Button(self, text='Later', font=large_font, command=parent.decide_later, bg='orange')
        self.button_later.grid(row=1, column=3, padx=10, pady=15)

        self.button_analyze = Button(self, text='Analyze', font=large_font, command=parent.analyze, bg='turquoise')
        self.button_analyze.grid(row=1, column=4, padx=10, pady=15)

        # TODO help button

        # TODO undo button

        # TODO rotate photo 90 degrees

        # TODO button that stars an image as to give user choice to look
        #  at them later (is this the same as later button?

        # TODO button for going into next folder, go inside, go outside. This could be an entire window tbh...

        # TODO button to show an overview of upcoming images

        # TODO compare button

        # TODO 'bank' button that lets users bank a certain image in a different folder. would be nice if users can make an unlimited amount of bank folders.
