from tkinter import Frame, Label, Entry, Canvas
from GUIcoder.myTkinter import myButton
from PIL import Image, ImageTk


def rgb2hex(rgb):
    digits = "0123456789abcdef"
    _hex = "#"
    for value in rgb:
        x = value // 16
        _hex += digits[x]
        _hex += digits[value - x * 16]
    return _hex


class Selector(Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.master = master
        self.bg = self["bg"]
        self.pack_propagate(0)

        root_button = myButton(self, text="SET ROOT",
                               command=lambda *args: self.event_generate("<<SETROOT>>"))
        root_button.place(relx=0.1, rely=0.031, relwidth=0.8, relheight=0.0775, anchor='nw')

        frame_button = myButton(self, text="FRAME",
                                command=lambda *args: self.event_generate("<<FRAME>>"))
        frame_button.place(relx=0.101, rely=0.1395, relwidth=0.363, relheight=0.1, anchor='nw')

        label_button = myButton(self, text="LABEL",
                                command=lambda *args: self.event_generate("<<LABEL>>"))
        label_button.place(relx=0.1005, rely=0.2662, relwidth=0.364, relheight=0.1, anchor='nw')

        button_button = myButton(self, text="BUTTON",
                                 command=lambda *args: self.event_generate("<<BUTTON>>"))
        button_button.place(relx=0.536, rely=0.14, relwidth=0.365, relheight=0.1, anchor='nw')

        radio_button = myButton(self, text="RADIOBUTTON",
                                command=lambda *args: self.event_generate("<<RADIOBUTTON>>"))
        radio_button.place(relx=0.5335, rely=0.2657, relwidth=0.365, relheight=0.1, anchor='nw')

        check_button = myButton(self, text="CHECKBUTTON",
                                command=lambda *args: self.event_generate("<<CHECKBUTTON>>"))
        check_button.place(relx=0.1005, rely=0.391, relwidth=0.364, relheight=0.1, anchor='nw')

        combobox_button = myButton(self, text="COMBOBOX",
                                   command=lambda *args: self.event_generate("<<COMBOBOX>>"))
        combobox_button.place(relx=0.1005, rely=0.516, relwidth=0.364, relheight=0.1, anchor='nw')

        entry_button = myButton(self, text="ENTRY",
                                command=lambda *args: self.event_generate("<<ENTRY>>"))
        entry_button.place(relx=0.536, rely=0.3907, relwidth=0.363, relheight=0.1, anchor='nw')

        text_button = myButton(self, text="TEXT",
                               command=lambda *args: self.event_generate("<<TEXT>>"))
        text_button.place(relx=0.536, rely=0.5158, relwidth=0.363, relheight=0.1, anchor='nw')

        spinbox_button = myButton(self, text="SPINBOX",
                                  command=lambda *args: self.event_generate("<<SPINBOX>>"))
        spinbox_button.place(relx=0.1005, rely=0.642, relwidth=0.364, relheight=0.1, anchor='nw')

        listbox_button = myButton(self, text="LISTBOX",
                                  command=lambda *args: self.event_generate("<<LISTBOX>>"))
        listbox_button.place(relx=0.536, rely=0.6428, relwidth=0.365, relheight=0.1, anchor='nw')

        self.save_button = myButton(self, text="SAVE", command=self.save)
        self.save_button.place(relx=0.22, rely=0.8125, relwidth=0.56, relheight=0.1225, anchor='nw')

    def save(self):
        self.master.writer.write_py()
        self.save_button.configure(text="SAVED IT!")
        self.master.root.after(3000, lambda *args: self.save_button.configure(text="SAVE"))


class ColorSelector(Frame):
    def __init__(self, master, index, color=False):
        super().__init__(master, bg='#435661')
        self.master = master
        self.index = index
        self.color = color if color else "#557282"
        self.all_colors_img = None
        self.color_picked = None
        self.pix = None
        self.all_colors = None
        self.quad = None
        self.circle = None
        self.entry = None
        self.ok = None
        self.remove = None

        self.set_everything()

    def set_everything(self):
        self.create_all_colors_img()

        self.all_colors = Label(self, image=self.all_colors_img, bg="#435661")
        self.all_colors.place(relx=0.025, rely=0.012, relwidth=0.95, relheight=0.07, anchor='nw')

        self.quad = Label(self, bg="#557282")
        self.quad.place(relx=0.025, rely=0.093, relwidth=0.95, relheight=0.475, anchor='nw')

        self.circle = Canvas(self, highlightthickness=0, bg="#435661")
        self.circle.place(relx=0.025, rely=0.582, relwidth=0.334, relheight=0.167, anchor='nw')

        self.circle.create_oval((0, 0, 66, 66), width=2, fill=self.color, outline="#435661")

        self.entry = Entry(self, bd=0, highlightthickness=0, bg="#557282", fg="#defffc", justify="center")
        self.entry.place(relx=0.4, rely=0.63, relwidth=0.57, relheight=0.08)

        if self.color != "#557282":
            self.entry.insert("end", self.color)

        self.ok = myButton(self, text="Confirm", font=("", 15), command=lambda *args: self.confirm())
        self.ok.place(relx=0.21, rely=0.784, relwidth=0.58, relheight=0.08, anchor='nw')

        self.remove = myButton(self, text="Remove this color", font=("", 12), command=lambda *args: self.remove_())
        self.remove.place(relx=0.21, rely=0.891, relwidth=0.58, relheight=0.08, anchor='nw')

        self.all_colors.bind("<Button-1>", lambda event: self.set_color_picked(event.x))
        self.all_colors.bind("<ButtonRelease-1>", lambda event: self.show_gradient())
        self.all_colors.bind("<B1-Motion>", lambda event: self.set_color_picked(event.x))
        self.all_colors.bind("<B1-Motion>", lambda event: self.show_gradient(event.x))

        self.quad.bind("<Button-1>", lambda event: self.show_color(event.x, event.y))
        self.quad.bind("<B1-Motion>", lambda event: self.show_color(event.x, event.y))

        self.entry.bind("<Return>", lambda *args: self.entry_sets())

    def create_all_colors_img(self):
        img = Image.new("HSV", (255, 20))
        pix = img.load()
        for x in range(255):
            for y in range(20):
                pix[x, y] = (x, 255, 255)
        self.all_colors_img = ImageTk.PhotoImage(img.resize((190, 20), Image.ANTIALIAS))

    def set_color_picked(self, x):
        self.color_picked = x * 255 // 190

    def create_gradient(self):
        img = Image.new("HSV", (255, 255))
        pix = img.load()

        for x in range(255):
            for y in range(255):
                pix[x, 254 - y] = (self.color_picked, x, y)

        self.pix = img.convert("RGB").load()

        return ImageTk.PhotoImage(img.resize((190, 190), Image.ANTIALIAS))

    def show_gradient(self, X=False):
        if X:
            self.set_color_picked(X)
        img = self.create_gradient()
        self.quad.configure(image=img)
        self.quad.image = img

    def show_color(self, x, y):
        if self.pix:
            if 0 <= x < 190 and 0 <= y < 190:
                rgb = self.pix[int(x / 190 * 255), int(y / 190 * 255)]
                _hex = rgb2hex(rgb)
                self.circle.create_oval((0, 0, 66, 66), width=2, fill=_hex, outline="#435661")

                self.entry.delete(0, "end")
                self.entry.insert("end", _hex)

                self.color = _hex

    def entry_sets(self):
        _hex = self.entry.get()
        self.circle.create_oval((0, 0, 66, 66), width=2, fill=_hex, outline="#435661")

        self.quad.image = None
        self.color = _hex

    def confirm(self):
        self.master.destroy()

    def remove_(self):
        self.color = None
        self.master.destroy()