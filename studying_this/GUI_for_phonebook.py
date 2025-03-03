import tkinter as tk
import time as time


class AddGUI(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.master.title('crowd counter')

        # add my variables
        self.nameNum = {'Mees', '0657374225'}
        self.number = tk.StringVar()
        self.name = tk.StringVar()

        self.define_widgets()
        self.grid()

    def define_widgets(self):

        # labels
        lbl_name = tk.Label(self)
        lbl_name['text'] = 'Name: '
        lbl_name.grid(row=0, column=0)

        lbl_number = tk.Label(self)
        lbl_number['text'] = 'Number: '
        lbl_number.grid(row=1, column=0)

        # entries
        entry_number = tk.Entry()
        entry_number['textvariable'] = self.number
        entry_number.grid(row=0, column=1)

        entry_name = tk.Entry()
        entry_name['textvariable'] = self.name
        entry_name.grid(row=1, column=1)

        # buttons
        btn_lookup = tk.Button(self)
        btn_lookup['text'] = 'lookup'
        btn_lookup['command'] = self.lookup
        btn_lookup.grid(row=2, column=0 )

        btn_enter = tk.Button(self)
        btn_enter['text'] = 'enter'
        btn_enter['command'] = self.enter
        btn_enter.grid(row=2, column=1)

        btn_remove = tk.Button(self)
        btn_remove['text'] = 'remove'
        btn_remove['command'] = self.remove
        btn_remove.grid(row=2, column=2)

        btn_quit = tk.Button(self)
        btn_quit['text'] = 'quit'
        btn_quit['command'] = self.goodbye
        btn_quit.grid(row=2, column=3)

    def lookup(self):
        pass

    def enter(self):
        pass

    def remove(self):
        pass

    def goodbye(self):
        pass



y = AddGUI()
y.mainloop()
