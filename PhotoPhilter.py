from tkinter import *
from PIL import Image, ImageTk


from tkinter import PhotoImage
import customtkinter as ctk
import tkinter.ttk as ttk
import re

import PicSelect as Ps

huge_font = ('Helvetica', 20)
large_font = ('Helvetica', 12)
small_font = ('Helvetica', 8)
tiny_font = ('helvetica', 4)


# class that creates the app
class App(Tk):
    def __init__(self):
        super().__init__()

        # Define styles
        self.title("PhotoPhilter")
        self.iconbitmap('favicon.ico')

        # Define screen dimensions
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Define shrink margins
        margin_x = 100
        margin_y = 100

        # Define window size
        window_width = screen_width - margin_x
        window_height = screen_height - margin_y

        # Set window size dynamically
        self.geometry(f"{window_width}x{window_height}+{int(margin_x/2)}+{int(margin_y/4)}")
        self.grid()

        self.canvas_width = window_width - 200
        self.canvas_height = window_height - 200

        # Define photo sorter button frame
        self.sorter = Sorter(self)
        self.sorter.grid(row=3, column=1, sticky='s',)

        # Define photo list
        self.photo_list = Ps.Pictures()

        # Define sort lists
        self.keeplist = []
        self.discardlist = []
        self.laterlist = []

        # Define photo in frame
        self.resized_image = Image.Image
        self.resized_image_tk = ImageTk
        self.image_ratio = 0.5
        self.set_photo()

        # Define Metadata TODO

    def set_photo(self):
        if len(self.photo_list) > 0:
            # Define image
            self.image_original = Image.open(self.photo_list.get_image(fullpath=True))
            self.resized_image = self.image_original
            self.resized_image_tk = ImageTk.PhotoImage(self.resized_image)
            # get image ratio (from original image) # TODO
            self.image_ratio = self.image_original.size[0] / self.image_original.size[1]
            # Define canvas
            self.pic_canvas = Canvas(bd=0, highlightthickness=0, relief='ridge',
                                     width=self.canvas_width,
                                     height=self.canvas_height)
            self.pic_canvas.grid(row=1, column=1, sticky='n', padx=100)
            self.pic_canvas.bind('<Configure>', self.show_full_image)
        else:
            print('no more Photo\'s to sort')
            # close the app
            # store all data in JSON files
            # Main.py will open new window that shows overview and Execute button.

    def report(self, button: str):
        print('put', self.photo_list.get_image(fullpath=False), 'into', button, 'list')

    def keep(self):
        self.report('keep')

        # store name in keeplist
        self.keeplist.append(self.photo_list.get_image())
        # remove name from photo_list
        self.photo_list.remove(self.photo_list.get_image())
        # show next photo
        self.set_photo()

        print('keeplist contains: ', len(self.keeplist))
        print('images list contains: ', len(self.photo_list))

    def discard(self):
        self.report('discard')
        # store name in discardlist
        self.discardlist.append(self.photo_list.get_image())
        # remove name from photo_list
        self.photo_list.remove(self.photo_list.get_image())
        # show next photo
        self.set_photo()

        print('discard list contains: ', len(self.discardlist))
        print('images list contains: ', len(self.photo_list))

    def decide_later(self):
        self.report('later')
        # store name in laterlist
        self.laterlist.append(self.photo_list.get_image())
        # remove name from photolist
        self.photo_list.remove(self.photo_list.get_image())
        # show next photo
        self.set_photo()

        print('later list contains: ', len(self.laterlist))
        print('images list contains: ', len(self.photo_list))

    def analyze(self):
        # analyze current photo TODO
        pass

    def show_full_image(self, event):
        # current ratio
        canvas_ratio = self.canvas_width / self.canvas_height

        # this canvas_ratio is really important, needed for canvas and image

        # get coordinates
        if canvas_ratio > self.image_ratio:         # canvas is wider than the image
            height = int(event.height)
            width = int(height * self.image_ratio)
        else:                                       # canvas is narrower than the image
            width = int(event.width)
            height = int(width / self.image_ratio)

        resized_image = self.image_original.resize((width, height))
        self.resized_image_tk = ImageTk.PhotoImage(resized_image)
        self.pic_canvas.create_image(
            int(event.width / 2),
            int(event.height / 2),
            anchor='center',
            image=self.resized_image_tk)

    def store(self):
        pass
        # TODO method that stores the keep, discard and later lists somewhere somehow


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

        # TODO button for going into next folder, go inside, go outside


if __name__ == '__main__':
    # Define and instantiate app

    app = App()
    # app.mainloop()

    md = MyMetadata(app)
    md.get_metdat('004.JPG')


