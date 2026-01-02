import tkinter as tk

window = tk.Tk()
button1 = tk.Button(text="B1", width=50)
button2 = tk.Button(text="B2", width=20)
button3 = tk.Button(text="B3", width=50)
button1.grid(column=0, row=0)
button2.grid(column=0, row=1, sticky="W")
button3.grid(column=0, row=2)
window.mainloop()