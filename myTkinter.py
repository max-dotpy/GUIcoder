from tkinter import Label
from PIL import Image, ImageTk


class myButton(Label):
    def __init__(self, master, **kw):
        """
        :param kw: [command, text, theme, font, img, img_bg]
        """
        self.kw = kw
        self.command = lambda *args: print("Working")
        label_kw, my_kw = self.parse_kw()
        self.dark, self.normal, self.light = my_kw["theme"]

        super().__init__(master, **label_kw)
        self.configure(relief="raised")

        if "img" in my_kw:
            image = Image.open(my_kw["img"])
            photo = ImageTk.PhotoImage(image)
            if "img_bg" in my_kw:
                self.configure(image=photo, bg=my_kw["bg"])
            else:
                self.configure(image=photo)
            self.image = photo
        else:
            self.configure(bg=self.normal, fg=self.light)

        self.bind('<Button-1>', lambda *args: self.clicked())
        self.bind('<ButtonRelease-1>', lambda *args: self.unclicked())

    def parse_kw(self):
        my_kw = {}
        for key, value in self.kw.items():
            if key in ["bg", "background", "fg", "foreground", "relief"]:
                del self.kw[key]

        if "command" in self.kw:
            self.command = self.kw["command"]
            del self.kw["command"]

        if "img" in self.kw:
            my_kw["img"] = self.kw["img"]
            del self.kw["img"]
            if "img_bg" in self.kw:
                my_kw["img_bg"] = self.kw["img_bg"]
                del self.kw["img_bg"]

        if "theme" in self.kw:
            my_kw["theme"] = self.kw["theme"]
            del self.kw["theme"]
        else:
            my_kw["theme"] = ('#435661', '#557282', '#defffc')

        return self.kw, my_kw

    def clicked(self):
        self.configure(relief="sunken")

    def unclicked(self):
        self.configure(relief="raised")
        self.command()

    def trigger(self):
        root = self.winfo_toplevel()
        self.configure(relief="sunken")
        root.update()
        root.after(100, self.unclicked())
