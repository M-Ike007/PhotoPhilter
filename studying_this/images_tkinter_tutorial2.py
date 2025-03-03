import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk


# setup
window = tk.Tk()
window.geometry('600x400')
window.title('Images')

# import image
image_original = Image.open('foto.jpg')
image_tk = ImageTk.PhotoImage(image_original)

python_dark = Image.open('foto2.png').resize((30, 30))
python_dark_tk = ImageTk.PhotoImage(python_dark)

image_ctk = ctk.CTkImage(light_image=Image.open('logo_dark.png'), dark_image=Image.open('logo_light.png'))

# widget
# label = ttk.Label(window, text='raccoon', image=image_tk)
# label.pack()

button = ttk.Button(window, text='a button', image=python_dark_tk, compound='right')
button.pack()

button_ctk = ctk.CTkButton(window, text='a button', image=image_ctk, compound='right')
button_ctk.pack()

# run
window.mainloop()
