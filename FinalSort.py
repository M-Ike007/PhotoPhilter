import os
from tkinter import *
from PIL import Image, ImageTk
import json

import PhotoPanel as PPan
import PopUpWindow as Popup

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

        self.left_panel = PPan.Panel('keep')
        self.right_panel = PPan.Panel('discard')

        self.left_panel.grid(row=1, column=0)
        self.right_panel.grid(row=1, column=2)

        self.title_left = Label(self, text='Keep', font=('Helvetica', 12))
        self.title_right = Label(self, text='Discard', font=('Helvetica', 12))

        self.title_left.grid(row=0, column=0)
        self.title_right.grid(row=0, column=2)

        self.button_switch = Button(self, text='Move', bg='orange')
        self.button_switch.grid(row=1, column=1, padx=10, pady=15)

        self.button_done = Button(self, text='Done', bg='green', command=self.done)
        self.button_done.grid(row=2, column=1, padx=10, pady=15)

    def get_move_imgs(self):
        # get state of every checkbox
        print('hi')
        self.left_panel.get_checkbox_states()
        self.right_panel.get_checkbox_states()

    def move_imgs(self):
        self.get_move_imgs()

        self.left_panel.refresh()
        self.right_panel.refresh()

    def done(self):
        popup = Popup.Popup()
        popup.mainloop()
        delete = popup.get_delete()
        if delete:
            print('photos will be deleted')
            # get directory
            file = open('settings.json')
            settings = file.read()
            file.close()
            directory = json.loads(settings)['directory']

            # get discard photo names and remove them
            file = open(directory + '/decisions.json')
            decisions = file.read()
            file.close()
            discard = json.loads(decisions)['discard']

            self.quit()
            self.destroy()
            for i in range(len(discard)):
                # keeping below line deactivated during development/testing
                # os.remove(directory + '/' + discard[i])
                print(discard[i], ' removed')
            print('done')
            os.remove(directory + '/decisions.json')
        else:
            print('photos stay')
        popup.destroy()




if __name__ == '__main__':
    final_sort = App()
    final_sort.mainloop()
    final_sort.get_move_imgs()
