import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk


def stretch_image(event):
    global resized_image_tk
    # size
    width = event.width
    height = event.height

    # create an image                   we dont want to import the image here because it would be imported many times
    resized_image = image_original.resize((width, height))
    resized_image_tk = ImageTk.PhotoImage(resized_image)

    # place on canvas
    canvas.create_image(0,0, image = resized_image_tk, anchor='nw')


# setup
window = tk.Tk()
window.geometry('600x400')
window.title('Images')

# grid layout

window.columnconfigure((0, 1, 2, 3), weight=1, uniform='a')
window.rowconfigure(0, weight=1)

# import image
image_original = Image.open('foto.jpg')
image_tk = ImageTk.PhotoImage(image_original)

python_dark = Image.open('foto2.png').resize((30, 30))
python_dark_tk = ImageTk.PhotoImage(python_dark)

image_ctk = ctk.CTkImage(light_image=Image.open('logo_dark.png'), dark_image=Image.open('logo_light.png'))

# widget
# label = ttk.Label(window, text='raccoon', image=image_tk)
# label.pack()

button_frame = ttk.Frame(window)

button = ttk.Button(button_frame, text='a button', image=python_dark_tk, compound='right')
button.pack(pady=10)

button_ctk = ctk.CTkButton(button_frame, text='a button', image=image_ctk, compound='right')
button_ctk.pack(pady=10)

button_frame.grid(column=0, row=0, sticky='NSEW')

# canvas -> image
canvas = tk.Canvas(window, bg='black', bd=0, highlightthickness=0, relief='ridge')
canvas.grid(column=1, columnspan=3, row = 0, sticky='NSEW')
# canvas.create_image(0,0, image = image_tk, anchor='nw')         # this needs to be a tk image

canvas.bind('<Configure>', stretch_image)

# run
window.mainloop()
