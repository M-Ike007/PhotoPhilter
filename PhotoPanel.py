from tkinter import *
from CheckBoxImage import CheckBoxImage as CBI
import json


class Panel(Frame):
    def __init__(self, image_list: str):
        super().__init__()

        self.decisions = self.get_decisions()

        self.grid()

        self.checkboxes = self.create_checkbox_list(image_list)
        self.checkbox = CBI
        self.place_checkboxes()

        self.states = []

    def get_decisions(self):
        with open('settings.json', 'r') as outfile:
            settings = json.load(outfile)
        outfile.close()
        return settings['directory'] + '/decisions.json'

    def set_checkbox_image(self, list_name: str):
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
            # checkboxVar = IntVar()
            image_path = str(directory) + '/' + str(imagenames[i])
            checkboxes.append(CBI(self, image_path=image_path))
            # self.states.append(checkboxVar)
        return checkboxes

    def place_checkboxes(self):
        for i in range(len(self.checkboxes)):
            self.checkbox = self.checkboxes[i]
            self.checkbox.grid(row=(1 + (i%6)), column=(i//6 +1))
            #TODO the number 6 is based on my personal laptop screen size and might be different elsewhere

    def refresh(self):
        # remove current checkboxes?
        ...
        # place new situation
        self.place_checkboxes()

    def get_checkbox_states(self):
        print(self.states)

if __name__ == '__main__':
    panel = Panel('keep')
    panel.place_checkboxes()


