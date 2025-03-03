import tkinter as tk


class AddGUI(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.master.title('calculate roots')

        # add my variables
        self.a = tk.IntVar()
        self.b = tk.IntVar()
        self.c = tk.IntVar()

        self.output = tk.StringVar()

        # define widgets and grid
        self.define_widgets()
        self.grid()

    def define_widgets(self):
        # title
        lbl_title = tk.Label(self)
        lbl_title['text'] = "Calculate roots, give ABC"
        lbl_title.grid(row=0, column=0, columnspan=2)
        # label a, b, c
        lbl_a = tk.Label(self)
        lbl_a['text'] = 'a = '
        lbl_a.grid(row=1, column=0)
        lbl_b = tk.Label(self)
        lbl_b['text'] = 'b = '
        lbl_b.grid(row=2, column=0)
        lbl_c = tk.Label(self)
        lbl_c['text'] = 'c = '
        lbl_c.grid(row=3, column=0)

        # entry boxes
        entry_a = tk.Entry(self)
        entry_a['textvariable'] = self.a
        entry_a.grid(row=1, column=1)
        entry_b = tk.Entry(self)
        entry_b['textvariable'] = self.b
        entry_b.grid(row=2, column=1)
        entry_c = tk.Entry(self)
        entry_c['textvariable'] = self.c
        entry_c.grid(row=3, column=1)

        btn_solve = tk.Button(self)
        btn_solve['text'] = "Solve"
        btn_solve['command'] = self.roots
        btn_solve.grid(row=0, column=2)

        lbl_output = tk.Label(self)
        lbl_output['textvariable'] = self.output
        lbl_output.grid(row=2, column=2)

    def roots(self):
        try:
            a = self.a.get()
            b = self.b.get()
            c = self.c.get()
        except Exception as e:
            self.output.set(e)
        else:
            d = b**2 -4*a*c
            if d > 0:
                x1 = (((-b)+d**0.5)/(2*a))
                x2 = (((-b)-d**0.5)/(2*a))
                output = str(x1) + str(x2)
            elif d == 0:
                x = (-b)/(2*a)
                output = str(x)
            else:
                output = 'no solution'

        return self.output.set(output)


my_GUI = AddGUI()
my_GUI.mainloop()







