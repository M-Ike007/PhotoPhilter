from tkinter import *
from CheckBoxImage import CheckBoxImage as CBI


class Panel(Frame):
    def __init__(self):
        super().__init__()

        self.grid()

        self.checkboximage = CBI(self, image_path='Media/004.JPG')
        self.checkboximage.grid()

    def show_images_from_list(self, list_name: str):
        # unpack decisions.json information
        # TODO show images from list
        # get list of list_name
        mylist = ...
        # unpack settings.json and get directory

        for name in list_name:  # list_name should be "keep" or "discard"
            print(name)

    # we need the following:
    # - data structure that lets us visualize an image over and over
    # - figure out best tk datatype for a highlightable image

    # constraints
    # - everything selected and moved to another "panel" has
    #   consequences for the decisions.json. so at the end the json
    #   should be modified, after which the images are deleted
