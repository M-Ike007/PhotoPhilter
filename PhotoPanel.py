from tkinter import *
from CheckBoxImage import CheckBoxImage as CBI
import json


class Panel(Frame):
    def __init__(self, image_list: str):
        super().__init__()

        self.grid()

        self.checkboxes = self.create_checkbox_list(image_list)
        self.place_checkboxes()


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

    def create_checkbox_list(self, list_name: str):
        # unpack decisions.json information
        file = open(self.decisions)
        decisions = file.read()
        file.close()

        # get list of list_name
        imagenames = json.loads(decisions)[list_name]

        # unpack settings.json and get directory
        file = open('settings.json')
        settings = file.read()
        file.close()
        directory = json.loads(settings)['directory']

        checkboxes = []
        for i in range(len(imagenames)):
            image_path = str(directory) + '/' + str(imagenames[i])
            checkboxes.append(CBI(self, image_path=image_path))
        return checkboxes

    def place_checkboxes(self):
        for i in range(len(self.checkboxes)):
            self.checkbox = self.checkboxes[i]
            self.checkbox.grid(row=(1 + (i%7)), column=(i//7 +1))
            # the number 7 is based on my personal laptop screen size and might be different elsewhere
            self.checkbox.grid(row=(1 + (i%6)), column=(i//6 +1))
            #TODO the number 6 is based on my personal laptop screen size and might be different elsewhere


if __name__ == '__main__':
    panel = Panel('keep')
    panel.place_checkboxes()


