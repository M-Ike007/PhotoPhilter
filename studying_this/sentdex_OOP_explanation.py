import tkinter as tk


LARGE_FONT = ('Verdana', 12)


class SeaofBTCapp(tk.Tk):
    def __init__(self, *args, **kwargs):        # things you always want to be run when starting up this class. initialising!
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side='top', fill='both', expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        frame = StartPage(container, self)

        self.frames[StartPage] = frame

        frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()         #raises frame to the front


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Start Page', font=LARGE_FONT) # we just created a tk.Label object but we're not doing anything with it yet
        label.pack(pady=10, padx=10)


app = SeaofBTCapp()
app.mainloop()



