
### apparently this tutorial was done 1- years ago and some things are depracated :( ###

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

import tkinter as tk
from tkinter import ttk

import matplotlib
matplotlib.use("TkAgg")


LARGE_FONT = ('Verdana', 12)


class SeaofBTCapp(tk.Tk):
    def __init__(self, *args, **kwargs):        # things you always want to be run when starting up this class. initialising!
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.iconbitmap(self, default='favicon.ico')
        tk.Tk.wm_title(self, 'Sea of BTC client')

        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo, PageThree):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()         #raises frame to the front


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text='Start Page', font=LARGE_FONT) # we just created a tk.Label object but we're not doing anything with it yet
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text='Visit Page 1', command=lambda: controller.show_frame(PageOne))
        button1.pack()

        button2 = ttk.Button(self, text='to page 2', command=lambda: controller.show_frame(PageTwo))
        button2.pack()

        button3 = ttk.Button(self, text='graph page', command=lambda: controller.show_frame(PageTwo))
        button3.pack()


class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Page One!', font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text='Back to Home', command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text='to page 2', command=lambda: controller.show_frame(PageTwo))
        button2.pack()


class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Page two', font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text='Back to Home', command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text='Back to page one', command=lambda: controller.show_frame(PageOne))
        button2.pack()


class PageThree(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='graph page', font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text='Back to Home', command=lambda: controller.show_frame(StartPage))
        button1.pack()

        # plot
        f = Figure(figusize=(5, 5), dpi=100)
        a = f.add_subplot(111)
        a.plot([1,2,3,4,5,6,7,8], [5,6,1,3,8,9,3,5])
        # add canvas
        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand = True)

        # # navigation bar
        # toolbar = NavigationToolbar2Tk(canvas, self)
        # toolbar.update()
        # canvas.tkcanvas().pack(side=tk.TOP, fill=tk.BOTH, expand = True)


app = SeaofBTCapp()
app.mainloop()



