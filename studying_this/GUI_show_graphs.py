import tkinter as tk
from PIL import Image, ImageTk
import pandas as pd


def custom_button(text: str, grid: tuple, col_span=None):
    my_label = tk.Label()
    my_label['text'] = text
    my_label.grid(row=grid[0], column=grid[1], columnspan=col_span)
    return my_label

class Figure(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.master.title("I graph, you graphed, we have griphed ")
        self.data = tk.StringVar()
        self.axes = tuple

        # the basics
        self.define_widgets()
        self.grid()

    def define_widgets(self):
        # label title
        lbl_title = tk.Label()
        lbl_title['text'] = 'import data (.csv):'
        lbl_title.grid(row=0, column=0)

        # entry for csv
        entry_csv = tk.Entry()
        entry_csv['textvariable'] = self.data
        entry_csv.grid(row=0, column=1, columnspan=2)

        # knop add data
        btn_add_data = tk.Button()
        btn_add_data['text'] = 'Add Data'
        btn_add_data['command'] = self.add_data
        btn_add_data.grid(row=0, column=3)

        lbl_1 = custom_button('X-variable',(1, 0))
        lbl_2 = custom_button('Y-variable 1', (2, 0))
        lbl_2 = custom_button('Y-variable 2', (3, 0))
        lbl_plot_type = custom_button('select plot type:', (1, 2), 2)

        options_X_var = tk.OptionMenu(self, self.X_var_options)



    def add_data(self):
        self.X_var_options = ... # should be a list of strings, take out of csv with pandas
        pass


my_gui = Figure()
my_gui.mainloop()


