import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk


# setup
window = tk.Tk()
window.geometry('600x400')
window.title('Images')

# import image
image_original = Image.open('foto.jpg').resize((600, 400))
image_tk = ImageTk.PhotoImage(image_original)

# widget
label = ttk.Label(window, text='raccoon', image=image_tk)
label.pack()

# run
window.mainloop()
