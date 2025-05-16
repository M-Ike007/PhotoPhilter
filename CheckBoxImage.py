import tkinter as tk
from tkinter import PhotoImage

# source: https://www.w3resource.com/python-exercises/tkinter/python-tkinter-custom-widgets-and-themes-exercise-2.php


class CheckBoxImage(tk.Checkbutton):
    def __init__(self, master=None, ** kwargs):
        super().__init__(master, ** kwargs)

        # Load custom images for checked and unchecked states
        self.checked_icon = PhotoImage(file='kaas.png')  # Replace with your checked image
        self.unchecked_icon = PhotoImage(file="kaas.png")  # Replace with your unchecked image

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


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Custom Checkbox Example")
    label = tk.Label(root, text="Click to check/uncheck checkbox:")
    label.pack()
    custom_checkbox = CheckBoxImage(root)
    custom_checkbox.pack(padx=20, pady=20)

    root.mainloop()
