import tkinter as tk
from PIL import Image, ImageTk, ImageFilter


class ButtonImage(tk.Button):
    def __init__(self, master, image_path):
        self.image_path = image_path
        self.state = False
        # load image
        self.image = Image.open(self.image_path).resize((100, 100))
        # image normal
        self.image_unclicked = ImageTk.PhotoImage(self.image)
        # image clicked
        self.image_clicked = ImageTk.PhotoImage(self.image.filter(ImageFilter.GaussianBlur(radius=3)))

        super().__init__(master,
                         image=self.image_unclicked,
                         height=100,
                         width=100,
                         padx=0,
                         pady=0,
                         state='normal',
                         command=self.clicked)

    def clicked(self):
        self.state = not self.state
        if self.state:
            info = str('-'+ self.image_path)
            self.config(image=self.image_clicked)
        else:
            info = str('+'+ self.image_path)
            self.config(image=self.image_unclicked)
        print(info)
        return info


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Custom button Example")
    label = tk.Label(root, text="click me")
    label.pack()
    button = ButtonImage(root, image_path='Media/004.JPG')
    button.pack()
    # custom_checkbox = CheckBoxImage(root)
    # custom_checkbox.pack(padx=20, pady=20)

    root.mainloop()