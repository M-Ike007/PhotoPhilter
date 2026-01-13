from tkinter import *
from CheckBoxImage import CheckBoxImage as CBI
from ButtonImage import ButtonImage as BI
import json


class Panel(Frame):
    def __init__(self, image_list: str):
        super().__init__()
        self.image_list = image_list
        self.decisions = self.get_decisions()

        self.grid()



        # self.checkboxes = self.create_checkbox_list(self.image_list)
        # self.checkbox = CBI
        # self.place_checkboxes()
        # self.states = []

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

    # BI's

class Panel2(Frame):
    def __init__(self, image_list: str):
        super().__init__()
        self.image_list = image_list
        self.directory = self.get_dir()
        self.decisions = self.get_decisions(self.directory)

        self.BIs = []
        self.grid()

        self.place_BIs()

        # self.checkboxes = self.create_checkbox_list(self.image_list)
        # self.checkbox = CBI
        # self.place_checkboxes()
        # self.states = []

    def get_dir(self):
        with open('settings.json', 'r') as outfile:
            settings = json.load(outfile)
        outfile.close()
        decisions_dir = settings['directory'] + '/decisions.json'
        return decisions_dir

    def get_decisions(self, decisions_dir):
        with open(decisions_dir, 'r') as outfile:
            decisions = json.load(outfile)
        outfile.close()
        return decisions

    def get_decision_list(self, list_name):
        return self.decisions[list_name]

    def create_BIs(self):
        mylist = self.get_decision_list(self.image_list)
        for i in range(len(mylist)):
            image_path = str(self.directory) + '/' + str(mylist[i])
            self.BIs.append(BI(self, image_path=image_path, ))

    def send_clicked_buttons(self):
        for i in range(len(self.BIs)):
            if self.BIs[i].state == True:
                print('i am clicked')
            else:
                print('i am NOT clicked')

    def place_BIs(self):
        for i in range(len(self.BIs)):
            BI = self.BIs[i]
            BI.grid(row=(1 + (i%6)), column=(i//6 +1))



if __name__ == '__main__':
    panel = Panel2('keep')
    panel.create_BIs()


