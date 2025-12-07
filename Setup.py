import json
from tkinter import *
from tkinter import filedialog


huge_font = ('Helvetica', 20)
large_font = ('Helvetica', 12)
small_font = ('Helvetica', 8)
tiny_font = ('helvetica', 4)


class App(Tk):
    def __init__(self):
        super().__init__()

        # Define styles
        self.title("PhotoPhilter - Setup")
        self.iconbitmap('Media/favicon.ico')
        self.geometry('700x400')
        self.grid()

        # stored settings
        self.folder = StringVar()
        ...                         # define settings to be stored here

        # frames
        self.setup_frame = Setup(self)

    # functionalities
    def select_directory(self):
        selected_folder = filedialog.askdirectory(initialdir='', title='Select a folder', mustexist=True)
        if selected_folder:
            # store selected folder path
            self.setup_frame.insert_dir(selected_folder)

    def set_workflow(self):
        pass
        # TODO idea for the future: let user determine their own workflow, which
        # lets them specify which steps to take and in what order.
        # also lets user decide on what folders to go through. (i.e. all subfolders of folder x, or ... )

    def start(self):
        # get settings
        self.folder = self.setup_frame.get_dir()
        ...                                         # get all settings values from Setup here.

        # check if everything is present
        if self.folder:
            # TODO it would make more sense if json files are stored
            #  in the given directory of the folder. That way you can
            #  load them and continue from where you left off.
            self.setup_frame.quit()

            settings = {'directory': self.folder}  # store all settings values in this dictionary

            with open("settings.json", "w") as outfile:
                json.dump(settings, outfile)

            outfile.close()

        else:
            self.setup_frame.raise_missing('directory')

        self.destroy()


class Setup(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.grid()

        # define top label for directory
        self.label = Label(self, text='Select Folder:', font=large_font)
        self.label.grid(row=1, column=1)

        # Define entry box description label
        self.label2 = Label(self, text='Directory:', font=large_font)
        self.label2.grid(row=2, column=1)

        # define entry box
        self.directory = Entry(self, width=50, font=large_font)
        self.directory.grid(row=2, column=2)

        # define directory button
        self.dir_button = Button(self, text='Folder', font=small_font,
                                 command=parent.select_directory)
        self.dir_button.grid(row=2, column=3)

        # start button
        self.start = Button(self, text='Start', font=small_font, command=parent.start, bg='#BCBCBC', width=5)
        self.start.grid(row=4, column=4, sticky='SE', padx=50, pady=310)

        # missing settings label (can change, when pressing start)
        self.label_missing = Label(self, text='', fg='red', font=small_font)
        self.label_missing.grid(row=4, column=2)

    def insert_dir(self, text: str):
        self.directory.delete(0, 'end')     # clear previous text
        self.directory.insert(0, text)

    def get_dir(self):
        return self.directory.get()

    def raise_missing(self, missing_item: str = 'something'):
        txt = 'you forgot to fill in ' + missing_item
        self.label_missing.config(text=txt)

    # TODO add function for buttonmapping of the buttons where user input determines these.


if __name__ == '__main__':
    print('hi')
    # Define and instantiate app
    app = App()
    app.mainloop()

