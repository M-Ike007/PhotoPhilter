import tkinter as tk
from PIL import Image, ImageTk


class Figure(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.master.title("Images")

        self.images = ['foto.jpg', 'hoi.jpg']
        self.fieldvalue = tk.StringVar()
        self.fieldvalue.set(self.images[0])
        self.img = ImageTk.PhotoImage(Image.open("foto.jpg"))
        self.nf = tk.StringVar()

        self.define_widgets()
        self.grid()

    def define_widgets(self):
        # label wat the dropdown does
        self.lbl_dropdown = tk.Label(self)
        self.lbl_dropdown['text'] = "choose"
        self.lbl_dropdown.grid(row=0, column=0)

        # dropdown menu
        self.dd_images = tk.OptionMenu(self, self.fieldvalue, *self.images, command=self.display_image)
        self.dd_images.grid(column=1, row=0)

        # label to show the image in
        self.lbl_image = tk.Label(self)
        self.lbl_image['image'] = self.img
        self.lbl_image.grid(column=0, row=1, columnspan=3)

        # label for entry box
        self.lbl_entry = tk.Label(self)
        self.lbl_entry['text'] = 'enter filename (only png)'
        self.lbl_entry.grid(row=2, column=0)

        # entry box for the new image name
        self.ent_new_image = tk.Entry(self)
        self. ent_new_image["textvariable"] = self.nf
        self.ent_new_image.grid(column=1, row=2)

        # button to add new image to the dropdown menu
        self.btn_new_image = tk.Button(self)
        self.btn_new_image['text'] = "get"
        self.btn_new_image['command'] = self.add_image
        self.btn_new_image.grid(row=2, column=2)

    def display_image(self, choice=None):
        if choice == None:
            image = self.fieldvalue.get()
        else:
            image = self.fieldvalue.get()
        im = Image.open(image)
        if im.width > 704:
            if im.height > 396:
                im = im.resize((704, 396))
            else:
                im = im.resize((704, im.height))
        else:
            if im.height > 396:
                im = im.resize((im.width, 396))
        self.img = ImageTk.PhotoImage(im)
        self.lbl_image.configure(image=self.img)

    def add_image(self):
        if self.ent_new_image.get() not in self.images:
            self.images.append(self.nf.get())
        self.dd_images = tk.OptionMenu(self, self.fieldvalue, *self.images, command=self.display_image)
        self.dd_images.grid(column=1, row=0)
        self.lbl_image.configure(image = self.display_image(self.images[-1]))

my_gui = Figure()
my_gui.mainloop()








