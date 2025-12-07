from tkinter import *
from CheckBoxImage import CheckBoxImage as CBI
import json


class Panel(Frame):
    def __init__(self):
        super().__init__()

        self.grid()

        self.checkboximage = CBI(self, image_path=self.set_checkbox_image('discard'))
        self.checkboximage.grid()

    def set_checkbox_image(self, list_name: str):
        # unpack decisions.json information
        file = open("decisions.json")
        decisions = file.read()
        file.close()

        # get list of list_name
        imagenames = json.loads(decisions)[list_name]

        # unpack settings.json and get directory
        file = open('settings.json')
        settings = file.read()
        file.close()
        directory = json.loads(settings)['directory']

        # create image path
        image_path = str(directory) + '/' + str(imagenames[0])

        return image_path

if __name__ == '__main__':
    panel = Panel()
    panel.set_checkbox_image('discard')
