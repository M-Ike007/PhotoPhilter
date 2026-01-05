import tkinter as tk
from PIL import Image, ImageTk, ImageFilter


class ButtonImage(tk.Button):
    def __init__(self, master, image_path, parent_panel_name):
        self.image_path = image_path
        self.state = False
        # load image
        self.image = ImageTk.PhotoImage(Image.open(self.image_path).resize((100, 100)))

        super().__init__(master,
                         image=self.image,
                         height=100,
                         width=100,
                         padx=0,
                         pady=0,
                         state='normal',
                         command=self.clicked)

    def clicked(self):
        self.state = not self.state
        if self.state:
            print('-', self.image_path)
        else:
            print('+', self.image_path)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Custom button Example")
    label = tk.Label(root, text="click me")
    label.pack()
    button = ButtonImage(root, image_path='Media/004.JPG', parent_panel_name='discard')
    button.pack()
    # custom_checkbox = CheckBoxImage(root)
    # custom_checkbox.pack(padx=20, pady=20)

    root.mainloop()