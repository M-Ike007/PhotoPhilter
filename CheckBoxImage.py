import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk, ImageFilter
# source: https://www.w3resource.com/python-exercises/tkinter/python-tkinter-custom-widgets-and-themes-exercise-2.php
# source used but adjusted to handle more image data types

# https://medium.com/@revelyuution/image-manipulation-in-python-using-pillow-62eb68aa8f93
# for image filter

class CheckBoxImage(tk.Checkbutton):
    def __init__(self, master, image_path=None):
        super().__init__(master)

        # Load image using PIL
        image = Image.open(image_path)
        image = image.resize((100, 100))

        # Load custom images for checked and unchecked states
        self.checked_icon = ImageTk.PhotoImage(image.filter(ImageFilter.GaussianBlur(radius=3)))  # Replace with your checked image
        self.unchecked_icon = ImageTk.PhotoImage(image)  # Replace with your unchecked image
        # TODO this is an error, I don't know how to fix it yet...
        self.config(
            image=self.unchecked_icon,
            selectimage=self.checked_icon,
            indicatoron=False,
            padx=0,
            pady=0,
            borderwidth=0,
            highlightthickness=0,
            relief=tk.FLAT,
        )

    # chatgpt said to use this but i don't think its necessary, but keeping it here just in case...
        # Keep a reference to prevent garbage collection
        # self.image_refs = [self.checked_icon, self.unchecked_icon]


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Custom Checkbox Example")
    label = tk.Label(root, text="Click to check/uncheck checkbox:")
    label.pack()
    custom_checkbox = CheckBoxImage(root)
    custom_checkbox.pack(padx=20, pady=20)

    root.mainloop()
