import tkinter as tk
import flying_distance as fd


class Gui_fly(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.master.title('Flying distances GUI')
        self.departure = tk.StringVar()
        self.destination = tk.StringVar()
        self.coordinates = tk.StringVar()
        self.distance = tk.StringVar()

        #functies
        self.define_widget()
        self.grid()

    def define_widget(self):
        lbl_dep = tk.Label(self)
        lbl_dep['text'] = "Departure city"
        lbl_dep.grid(row=0, column=0)

        lbl_des = tk.Label(self)
        lbl_des['text'] = "Destination city"
        lbl_des.grid(row=0, column=3)

        self.ent_dep = tk.Listbox(self)
        self.ent_dep.grid(row=1, column=0)

        self.ent_des = tk.Listbox(self)
        self.ent_des.grid(row=1, column=3)

        self.btn_calc = tk.Button(self)
        self.btn_calc['text'] = "Calculate"

        #self.btn_calc['command'] = self.add_image
        self.btn_calc.grid(row=1, column=1, columnspan=2)

        lbl_dep_ch = tk.Label(self)
        lbl_dep_ch['text'] = "Dep. city:"
        lbl_dep_ch.grid(row=2, column=1)

        lbl_des_ch = tk.Label(self)
        lbl_des_ch['text'] = "Des. city:"
        lbl_des_ch.grid(row=2, column=2)

        self.lbl_output_dep = tk.Label(self)
        self.lbl_output_dep['textvariable'] = self.departure
        self.lbl_output_dep.grid(row=3, column=1)

        self.lbl_output_des = tk.Label(self)
        self.lbl_output_des['textvariable'] = self.destination
        self.lbl_output_des.grid(row=3, column=2)

        lbl_dep_cor = tk.Label(self)
        lbl_dep_cor['text'] = "Coordinates"
        lbl_dep_cor.grid(row=4, column=1)

        lbl_des_cor = tk.Label(self)
        lbl_des_cor['text'] = "Coordinates"
        lbl_des_cor.grid(row=4, column=2)

        self.lbl_output_dep_cor = tk.Label(self)
        self.lbl_output_dep_cor['textvariable'] = self.coordinates
        self.lbl_output_dep_cor.grid(row=5, column=1)

        self.lbl_output_des_cor = tk.Label(self)
        self.lbl_output_des_cor['textvariable'] = self.coordinates
        self.lbl_output_des_cor.grid(row=5, column=2)

        lbl_flyingdistance = tk.Label(self)
        lbl_flyingdistance['text'] = "Flying distance:"
        lbl_flyingdistance.grid(row=6, column=1, columnspan=2)

        self.distance = tk.Label(self)
        lbl_flyingdistance['text'] = self.distance

    def load_data(self, **dict):
        pass

    def calculate(self, my_dict):
        cities = fd.reader('more_city_data', my_dict)
        tuple_depart = cities[self.departure]
        tuple_destin = cities[self.destination]

        self.distance = fd.fly_dist(tuple_depart, tuple_destin)
        self.lbl_distance = tk.Label(self)
        self.lbl_distance['text'] = self.distance
        self.lbl_distance.grid(...)


city_dict = {'Amsterdam': ('Amsterdam', (52, 22, 'N'), (4, 32, 'E')),
             'Montreal': ('Montreal', (45, 30, 'N'), (73, 35, 'W')),
             'Auckland': ('Auckland', (36, 52, 'S'), (174, 45, 'E'))}

hello = Gui_fly()
hello.mainloop()