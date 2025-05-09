from tkinter import *
from CheckBoxImage import CheckBoxImage as CBI


class Panel(Frame):
    def __init__(self):
        super().__init__()

        self.grid()

        self.checkboximage = CBI(self)
        self.checkboximage.grid()

        # lets try to build this panel with pack() instead of grid()
        # grid gives more freedom, but since we have such a specific
        # environment, pack might work really well here and save us
        # a lot of time!

        # just figured out that its not allowed to have a child use pack() when parent uses grid()
        # which is really fucking annoying but also understanding :(

        # we need the following:
        # - data structure that lets us visualize an image over and over
        # - figure out best tk datatype for a highlightable image

        # constraints
        # - everything selected and moved to another "panel" has
        #   consequences for the decisions.json. so at the end the json
        #   should be modified, after which the images are deleted
