from tkinter import *
from tkinter import ttk



def relx(widget, factor):
    info = widget.place_info()
    relx = float(info["relx"])
    rely = float(info["rely"])
    relwidth = float(info["relwidth"])
    relheight = float(info["relheight"])
    widget.place(relx=relx + factor * 0.001, rely=rely, relwidth=relwidth, relheight=relheight, anchor="nw")


def rely(widget, factor):
    info = widget.place_info()
    relx = float(info["relx"])
    rely = float(info["rely"])
    relwidth = float(info["relwidth"])
    relheight = float(info["relheight"])
    widget.place(relx=relx, rely=rely + factor * 0.001, relwidth=relwidth, relheight=relheight, anchor="nw")


def relwidth(widget, factor):
    info = widget.place_info()
    relx = float(info["relx"])
    rely = float(info["rely"])
    relwidth = float(info["relwidth"])
    relheight = float(info["relheight"])
    widget.place(relx=relx, rely=rely, relwidth=relwidth + factor * 0.001, relheight=relheight, anchor="nw")


def relheight(widget, factor):
    info = widget.place_info()
    relx = float(info["relx"])
    rely = float(info["rely"])
    relwidth = float(info["relwidth"])
    relheight = float(info["relheight"])
    widget.place(relx=relx, rely=rely, relwidth=relwidth, relheight=relheight + factor * 0.001, anchor="nw")


class myButton:
    def __init__(self, master, **kwargs):
        """
        :param kwargs: [command, text, theme, font, img]
        """
        self.master = master
        self.command = kwargs["command"] if "command" in kwargs else lambda *args: print("Working")
        self.text = kwargs["text"] if "text" in kwargs else "Button"
        self.dark, self.normal, self.light = kwargs["theme"] if "theme" in kwargs else ('#435661', '#557282', '#defffc')
        self.font = kwargs["font"] if "font" in kwargs else "TkDefaultFont"

        if "img" in kwargs:
            image = Image.open(kwargs["img"])
            photo = ImageTk.PhotoImage(image)
            if "bg" in kwargs:
                self.button = Label(self.master, image=photo, bg=kwargs["bg"], relief=RAISED)
            else:
                self.button = Label(self.master, image=photo, relief=RAISED)
            self.button.image = photo
        else:
            self.button = Label(self.master, bg=self.normal, fg=self.light,
                                text=self.text, font=self.font, relief=RAISED)

        self.button.bind('<Button-1>', lambda *args: self.clicked())
        self.button.bind('<ButtonRelease-1>', lambda *args: self.unclicked())

    def clicked(self):
        self.button.configure(relief=SUNKEN)

    def unclicked(self):
        self.button.configure(relief=RAISED)
        self.command()

    def pack(self, **kwargs):
        self.button.pack(**kwargs)

    def pack_forget(self):
        self.button.pack_forget()

    def trigger(self):
        root = self.button.winfo_toplevel()
        self.button.configure(relief=SUNKEN)
        root.update()
        root.after(100, self.unclicked())

        
class Writer:
    def __init__(self):
        self.background = "white"
        self.geometry = "1000x600+0+0"
        self.record = {}

        self.text = [
            "from tkinter import *\nfrom tkinter import ttk\nfrom tkinter.ttk import Combobox\n\n\nclass App(Frame):\n\tdef __init__(self, master):\n" +
            "\t\tsuper().__init__(master, bg='{}')\n\t\tmaster.geometry('{}')\n\n"
        ]

    def write_widget(self, widget_name, place_info):
        if widget_name in self.record:
            j = self.record[widget_name] + 1
            self.record[widget_name] += 1
        else:
            j = 0
            self.record[widget_name] = 0

        text = f"\t\tself.{widget_name.lower()}{j} = {widget_name}(self)\n\t\tself.{widget_name.lower()}{j}.place("
        if widget_name == "Button":
            text = f"\t\tself.{widget_name.lower()}{j} = ttk.{widget_name}(self)" \
                   f"\n\t\tself.{widget_name.lower()}{j}.place("

        for key, value in place_info.items():
            if key in ["relx", "rely", "relwidth", "relheight", "anchor"]:
                if type(value) == str:
                    value = f"'{value}'"
                text += f"{key}={value}, "
        self.text.append(text[:-2] + ")\n")

    def begin_configure(self, widget_name):
        j = self.record[widget_name]
        self.text.append(f"\t\tself.{widget_name.lower()}{j}.configure(")

    def write_configure(self, key, value):
        try:
            value = int(value)
        except ValueError:
            value = f"'{value}'"

        self.text.append(f"{key}={value}, ")

    def end_configure(self):
        if self.text[-1][-2:] == "e(":
            self.text[-1] = "\n\n"
        else:
            self.text[-1] = self.text[-1][:-2] + ")\n\n"

    def write_py(self):
        self.text[0] = self.text[0].format(self.background, self.geometry)
        self.text.append("\n\nif __name__ == '__main__':\n\troot = Tk()\n\n\tApp(root).place(relx=0, "
                         "rely=0, relwidth=1, relheight=1)\n\n\troot.mainloop()\n\n")

        text = "".join(self.text)
        with open("Prototype.py", "w") as file:
            file.write(text)


# Frame, LEFT, myButton, CENTER, Label, Entry, Listbox, relx, rely, relwidth, relheight
class Settings(Frame):
    def __init__(self, master, widget, widget_name, writer, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        self.widget = widget
        self.widget_name = widget_name
        self.writer = writer
        self.theme = ("#808080", "#bdbdbd", "#000000")
        self.bg = self["bg"]
        self.frame_background = "red"

        self.set_labels_and_buttons()

        self.label = Label(self, bg="#bdbdbd", justify=CENTER)
        self.label.place(relx=0.125, relwidth=0.75, rely=0.21, relheight=0.07)

        self.entry = Entry(self, justify=CENTER)
        self.entry.place(relx=0.125, relwidth=0.575, rely=0.33, relheight=0.07)

        self.entry.bind("<Return>", lambda *event: self.set_value())

        self.ok_button = myButton(self, command=self.set_value, theme=self.theme, text="Ok")
        self.ok_button.button.place(relx=0.75, relwidth=0.125, rely=0.33, relheight=0.07)

        self.box = Listbox(self, bg="#bdbdbd")
        self.box.place(relx=0.08, relwidth=0.84, rely=0.45, relheight=0.35)

        self.box.bind("<ButtonRelease-1>", lambda *event: self.box_click())

        self.items = []
        self.values = []
        self.j = 0
        self.record = {"background": "red"}

        end_button = myButton(self, command=self.end, theme=self.theme, text="Finish")
        end_button.button.place(relx=0.33, relwidth=0.33, rely=0.85, relheight=0.1)

    def set_labels_and_buttons(self):
        frame_top_left = Frame(self, bg=self.bg)
        frame_top_left.place(relx=0, rely=0, relheight=0.1, relwidth=0.5)

        frame_top_right = Frame(self, bg=self.bg)
        frame_top_right.place(relx=0.5, rely=0, relheight=0.1, relwidth=0.5)

        frame_bottom_left = Frame(self, bg=self.bg)
        frame_bottom_left.place(relx=0, rely=0.1, relheight=0.1, relwidth=0.5)

        frame_bottom_right = Frame(self, bg=self.bg)
        frame_bottom_right.place(relx=0.5, rely=0.1, relheight=0.1, relwidth=0.5)

        Label(frame_top_left, bg=self.bg, fg="black", text="relx:").pack(side=LEFT, padx=10)
        myButton(frame_top_left, theme=self.theme, text=" - ",
                 command=lambda *args: relx(self.widget, -1)).pack(side=LEFT, padx=5)
        myButton(frame_top_left, theme=self.theme, text=" + ",
                 command=lambda *args: relx(self.widget, 1)).pack(side=LEFT, padx=5)

        Label(frame_top_right, bg=self.bg, fg="black", text="rely:").pack(side=LEFT, padx=10)
        myButton(frame_top_right, theme=self.theme, text=" - ",
                 command=lambda *args: rely(self.widget, -1)).pack(side=LEFT, padx=5)
        myButton(frame_top_right, theme=self.theme, text=" + ",
                 command=lambda *args: rely(self.widget, 1)).pack(side=LEFT, padx=5)

        Label(frame_bottom_left, bg=self.bg, fg="black", text="relwidth:").pack(side=LEFT, padx=10)
        myButton(frame_bottom_left, theme=self.theme, text=" - ",
                 command=lambda *args: relwidth(self.widget, -1)).pack(side=LEFT, padx=5)
        myButton(frame_bottom_left, theme=self.theme, text=" + ",
                 command=lambda *args: relwidth(self.widget, 1)).pack(side=LEFT, padx=5)

        Label(frame_bottom_right, bg=self.bg, fg="black", text="relheight:").pack(side=LEFT, padx=10)
        myButton(frame_bottom_right, theme=self.theme, text=" - ",
                 command=lambda *args: relheight(self.widget, -1)).pack(side=LEFT, padx=5)
        myButton(frame_bottom_right, theme=self.theme, text=" + ",
                 command=lambda *args: relheight(self.widget, 1)).pack(side=LEFT, padx=5)

    def set_listbox(self, items):
        self.items = items
        for item in items:
            self.box.insert(END, item)
            self.values.append("")

    def box_click(self):
        self.j = self.box.curselection()[0]
        self.entry.delete(0, END)
        text = f"{self.items[self.j]} : {self.values[self.j]}"
        self.label.configure(text=text)

    def set_value(self):
        value = self.entry.get()
        try:
            self.values[self.j] = int(value)
        except ValueError:
            self.values[self.j] = str(value)

        text = f"{self.items[self.j]} : {self.values[self.j]}"
        self.label.configure(text=text)

        couple = {self.items[self.j]: self.values[self.j]}
        if self.widget_name != "Frame":
            self.widget.configure(**couple)
        else:
            self.master.frame_background = self.values[self.j]
            self.event_generate("<<GenFrame>>")

        self.record[self.items[self.j]] = self.values[self.j]

    def end(self):
        if self.widget_name != "Frame":
            self.writer.write_widget(self.widget_name, self.widget.place_info())
        else:
            self.writer.write_widget(self.widget_name, self.master.fake_frame_place_info)

        if self.record:
            self.writer.begin_configure(self.widget_name)

            for key, value in self.record.items():
                if key == "background" and value == "red":
                    continue
                self.writer.write_configure(key, value)

            self.writer.end_configure()

        self.master.frame_background = self.frame_background

        self.destroy()


# Frame, myButton, TOP, LEFT, Entry, Label
class Settings_Root(Frame):
    def __init__(self, master, board, writer, **kwargs):
        super().__init__(master, **kwargs)
        self.root = board
        self.writer = writer
        self.theme = ("#808080", "#bdbdbd", "#000000")
        self.bg = self["bg"]
        self._background = "white"
        self._geometry = "1000x600+0+0"

        f1 = Frame(self, bg=self.bg)
        f1.pack(fill=BOTH, padx=15, pady=15)

        Label(f1, bg=self.bg, fg="black", text="background: ").pack(side=LEFT, fill=X)
        self.entry_background = Entry(f1, width=15, justify=CENTER)
        self.entry_background.pack(side=LEFT)
        myButton(f1, theme=self.theme, text="OK", command=self.set_background).pack(side=LEFT, fill=X, padx=10)
        self.entry_background.bind("<Return>", lambda event: self.set_background())

        f2 = Frame(self, bg=self.bg)
        f2.pack(fill=BOTH, padx=15, pady=15)

        Label(f2, bg=self.bg, fg="black", text="width: ").pack(side=LEFT, fill=X)
        self.entry_width = Entry(f2, width=10, justify=CENTER)
        self.entry_width.pack(side=LEFT)
        Label(f2, bg=self.bg, fg="black", text="height: ").pack(side=LEFT, fill=X)
        self.entry_height = Entry(f2, width=10, justify=CENTER)
        self.entry_height.pack(side=LEFT)

        f3 = Frame(self, bg=self.bg)
        f3.pack(fill=BOTH, padx=15, pady=15)

        Label(f3, bg=self.bg, fg="black", text="x offset: ").pack(side=LEFT, fill=X)
        self.entry_xoff = Entry(f3, width=10, justify=CENTER)
        self.entry_xoff.pack(side=LEFT)
        Label(f3, bg=self.bg, fg="black", text="y offset: ").pack(side=LEFT, fill=X)
        self.entry_yoff = Entry(f3, width=10, justify=CENTER)
        self.entry_yoff.pack(side=LEFT)

        myButton(self, theme=self.theme, text="OK", command=self.set_geometry).pack(pady=10)

        myButton(self, theme=self.theme, text="Finish", command=self.end).pack(pady=10)

    def set_background(self):
        self.root.configure(bg=self.entry_background.get())
        self._background = self.entry_background.get()

    def set_geometry(self):
        w, h = self.entry_width.get(), self.entry_height.get()
        x, y = self.entry_xoff.get(), self.entry_yoff.get()
        w = 0 if w == "" else int(w)
        h = 0 if h == "" else int(h)
        x = 0 if x == "" else int(x)
        y = 0 if y == "" else int(y)

        self.root.master.geometry(f"{w}x{h}+{x}+{y}")
        self._geometry = f"{w}x{h}+{x}+{y}"

    def end(self):
        self.writer.geometry = self._geometry
        self.writer.background = self._background

        self.destroy()


# Frame, LEFT, myButton, RIGHT, TOP, BOTH
class Selector(Frame):
    def __init__(self, master, writer, **kwargs):
        super().__init__(master, **kwargs)
        self.theme = ("#808080", "#bdbdbd", "#000000")
        self.bg = self["bg"]
        self.pack_propagate(0)

        root_button = myButton(self, theme=self.theme, text="SET ROOT",
                               command=lambda *args: self.event_generate("<<SETROOT>>"))
        root_button.pack(fill=X, padx=40, pady=15)

        frame_left = Frame(self, bg=self.bg)
        frame_left.pack(side=LEFT, fill=BOTH, expand=True, padx=15, pady=8)

        frame_right = Frame(self, bg=self.bg)
        frame_right.pack(side=RIGHT, fill=BOTH, expand=True, padx=15, pady=8)

        frame_button = myButton(frame_left, theme=self.theme, text="FRAME",
                                command=lambda *args: self.event_generate("<<FRAME>>"))
        frame_button.pack(fill=X, pady=5)

        label_button = myButton(frame_left, theme=self.theme, text="LABEL",
                                command=lambda *args: self.event_generate("<<LABEL>>"))
        label_button.pack(fill=X, pady=5)

        button_button = myButton(frame_right, theme=self.theme, text="BUTTON",
                                 command=lambda *args: self.event_generate("<<BUTTON>>"))
        button_button.pack(fill=X, pady=5)

        radio_button = myButton(frame_right, theme=self.theme, text="RADIOBUTTON",
                                command=lambda *args: self.event_generate("<<RADIOBUTTON>>"))
        radio_button.pack(fill=X, pady=5)

        check_button = myButton(frame_left, theme=self.theme, text="CHECKBUTTON",
                                command=lambda *args: self.event_generate("<<CHECKBUTTON>>"))
        check_button.pack(fill=X, pady=5)

        combobox_button = myButton(frame_left, theme=self.theme, text="COMBOBOX",
                                   command=lambda *args: self.event_generate("<<COMBOBOX>>"))
        combobox_button.pack(fill=X, pady=5)

        entry_button = myButton(frame_right, theme=self.theme, text="ENTRY",
                                command=lambda *args: self.event_generate("<<ENTRY>>"))
        entry_button.pack(fill=X, pady=5)

        text_button = myButton(frame_right, theme=self.theme, text="TEXT",
                               command=lambda *args: self.event_generate("<<TEXT>>"))
        text_button.pack(fill=X, pady=5)

        spinbox_button = myButton(frame_left, theme=self.theme, text="SPINBOX",
                                  command=lambda *args: self.event_generate("<<SPINBOX>>"))
        spinbox_button.pack(fill=X, pady=5)

        listbox_button = myButton(frame_right, theme=self.theme, text="LISTBOX",
                                  command=lambda *args: self.event_generate("<<LISTBOX>>"))
        listbox_button.pack(fill=X, pady=5)

        save_button = myButton(self, theme=self.theme, text="SAVE", command=writer.write_py)
        save_button.pack(side=BOTTOM, fill=X, padx=10, pady=15)


# Toplevel, Frame, Setting, Selector
class Manager(Toplevel):
    def __init__(self, master, writer, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        self.writer = writer
        self.selector = Selector(self, self.writer, bg=self["bg"])
        self.frame_background = "red"
        self.fake_frame_place_info = {}

        self.selector.place(relx=0, rely=0, relwidth=1, relheight=1)

    def switch(self, widget, widget_name, items):
        settings = Settings(self, widget, widget_name, self.writer, bg=self["bg"])
        settings.set_listbox(items)
        settings.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.wait_window(settings)

    def set_root(self, board):
        settings = Settings_Root(self, board, self.writer, bg=self["bg"])
        settings.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.wait_window(settings)


# Canvas
class Board(Canvas):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        self.x0, self.y0, self.x1, self.y1 = 0, 0, 0, 0
        self.configure(highlightthickness=0)
        self.set_bind()

    def draw(self, x, y):
        self.delete("line")
        self.x1, self.y1 = x, y

        self.create_line(self.x0, self.y0, self.x0, self.y1, tag="line", width=1)
        self.create_line(self.x0, self.y0, self.x1, self.y0, tag="line", width=1)
        self.create_line(self.x0, self.y1, self.x1, self.y1, tag="line", width=1)
        self.create_line(self.x1, self.y0, self.x1, self.y1, tag="line", width=1)

    def set_P0(self, x, y):
        self.x0, self.y0 = x, y

    def get_dims(self):
        return self.winfo_width(), self.winfo_height()

    def get_geometry(self):
        if self.x0 < self.x1 and self.y0 < self.y1:
            return (self.x0, self.y0), (self.x1 - self.x0, self.y1 - self.y0), self.get_dims()
        elif self.x0 < self.x1 and self.y1 < self.y0:
            return (self.x0, self.y1), (self.x1 - self.x0, self.y0 - self.y1), self.get_dims()
        elif self.x1 < self.x0 and self.y1 < self.y0:
            return (self.x1, self.y1), (self.x0 - self.x1, self.y0 - self.y1), self.get_dims()
        else:
            return (self.x1, self.y0), (self.x0 - self.x1, self.y1 - self.y0), self.get_dims()

    def set_bind(self):
        self.bind("<B1-Motion>", lambda event: self.draw(event.x, event.y))
        self.bind("<Button-1>", lambda event: self.set_P0(event.x, event.y))


# Manager, Board
class App:
    def __init__(self, root):
        self.writer = Writer()
        root.geometry("1000x600+600+100")
        self.fake_frame_coords = (1, 2, 3, 4)

        self.manager = Manager(root, self.writer, bg="grey", height=600, width=350)
        self.manager.geometry("+200+100")

        self.board = Board(root, height=600, width=1000)
        self.board.pack(fill=BOTH, expand=True)

        self.set_bind()

    def create_frame(self):
        P0, widget_dims, board_dims = self.board.get_geometry()
        x, y = P0
        width, height = widget_dims
        board_width, board_height = board_dims

        self.fake_frame_coords = (x, y, x + width, y + height)
        self.board.create_rectangle(x, y, x + width, y + height, width=0, fill="red")
        self.board.delete("line")

        x, y = x / board_width, y / board_height
        width, height = width / board_width, height / board_height
        self.manager.fake_frame_place_info = {"relx": x, "rely": y, "relwidth": width, "relheight": height, "anchor": "nw"}

        frame = "Frame"
        items = ["background"]

        self.manager.switch(frame, "Frame", items)

    def create_label(self):
        P0, widget_dims, board_dims = self.board.get_geometry()
        x, y = P0
        width, height = widget_dims
        board_width, board_height = board_dims

        x, y = x / board_width, y / board_height
        width, height = width / board_width, height / board_height

        label = Label(self.board, bg="red")
        label.place(relx=x, rely=y, relheight=height, relwidth=width, anchor="nw")
        self.board.delete("line")
        items = ["anchor", "background", "cursor", "foreground", "image",
                 "padx", "pady", "relief", "text", "underline", "wraplenght"]

        self.manager.switch(label, "Label", items)

    def create_entry(self):
        P0, widget_dims, board_dims = self.board.get_geometry()
        x, y = P0
        width, height = widget_dims
        board_width, board_height = board_dims

        x, y = x / board_width, y / board_height
        width, height = width / board_width, height / board_height

        entry = Entry(self.board)
        entry.place(relx=x, rely=y, relheight=height, relwidth=width, anchor="nw")
        self.board.delete("line")
        items = ["background", "cursor", "foreground", "highlightcolor", "justify",
                 "relief", "selectbackground", "selectborderwidth", "show", "state"]

        self.manager.switch(entry, "Entry", items)

    def create_button(self):
        P0, widget_dims, board_dims = self.board.get_geometry()
        x, y = P0
        width, height = widget_dims
        board_width, board_height = board_dims

        x, y = x / board_width, y / board_height
        width, height = width / board_width, height / board_height

        button = ttk.Button(self.board)
        button.place(relx=x, rely=y, relheight=height, relwidth=width, anchor="nw")
        self.board.delete("line")
        items = ["borderwidth", "foreground", "justify", "text"]

        self.manager.switch(button, "Button", items)

    def create_radiobutton(self):
        P0, widget_dims, board_dims = self.board.get_geometry()
        x, y = P0
        width, height = widget_dims
        board_width, board_height = board_dims

        x, y = x / board_width, y / board_height
        width, height = width / board_width, height / board_height

        button = Radiobutton(self.board)
        button.place(relx=x, rely=y, relheight=height, relwidth=width, anchor="nw")
        self.board.delete("line")
        items = ["anchor", "activebackground", "activeforeground", "background", "cursor",
                 "borderwidth", "disabledforeground", "foreground", "highlightbackground", "justify",
                 "highlightcolor", "relief", "overrelief", "text", "highlightthickness", "indicatoron",
                 "offrelief", "selectcolor", "value"
                 ]

        self.manager.switch(button, "Radiobutton", items)

    def create_checkbutton(self):
        P0, widget_dims, board_dims = self.board.get_geometry()
        x, y = P0
        width, height = widget_dims
        board_width, board_height = board_dims

        x, y = x / board_width, y / board_height
        width, height = width / board_width, height / board_height

        button = Checkbutton(self.board)
        button.place(relx=x, rely=y, relheight=height, relwidth=width, anchor="nw")
        self.board.delete("line")
        items = ["anchor", "activebackground", "activeforeground", "background", "cursor",
                 "borderwidth", "disabledforeground", "foreground", "highlightbackground", "justify",
                 "highlightcolor", "relief", "overrelief", "text", "highlightthickness", "indicatoron",
                 "offrelief", "selectcolor",
                 ]

        self.manager.switch(button, "Checkbutton", items)

    def create_combobox(self):
        P0, widget_dims, board_dims = self.board.get_geometry()
        x, y = P0
        width, height = widget_dims
        board_width, board_height = board_dims

        x, y = x / board_width, y / board_height
        width, height = width / board_width, height / board_height

        box = ttk.Combobox(self.board)
        box.place(relx=x, rely=y, relheight=height, relwidth=width, anchor="nw")
        self.board.delete("line")
        items = ["justify", "values", "background"]

        self.manager.switch(box, "Combobox", items)

    def create_spinbox(self):
        P0, widget_dims, board_dims = self.board.get_geometry()
        x, y = P0
        width, height = widget_dims
        board_width, board_height = board_dims

        x, y = x / board_width, y / board_height
        width, height = width / board_width, height / board_height

        box = Spinbox(self.board)
        box.place(relx=x, rely=y, relheight=height, relwidth=width, anchor="nw")
        self.board.delete("line")

        items = ["activebackground", "buttonbackground", "background", "disabledbackground", "from_"
                 "borderwidth", "disabledforeground", "foreground", "highlightbackground", "justify",
                 "highlightcolor", "relief", "highlightthickness", "values", "to_", "increment"
                 ]

        self.manager.switch(box, "Spinbox", items)

    def create_listbox(self):
        P0, widget_dims, board_dims = self.board.get_geometry()
        x, y = P0
        width, height = widget_dims
        board_width, board_height = board_dims

        x, y = x / board_width, y / board_height
        width, height = width / board_width, height / board_height

        box = Listbox(self.board)
        box.place(relx=x, rely=y, relheight=height, relwidth=width, anchor="nw")
        self.board.delete("line")

        items = ["activestyle", "background", "borderwidth", "disabledforeground", "foreground", "highlightbackground",
                 "highlightcolor", "relief", "highlightthickness"]

        self.manager.switch(box, "Listbox", items)

    def create_text(self):
        P0, widget_dims, board_dims = self.board.get_geometry()
        x, y = P0
        width, height = widget_dims
        board_width, board_height = board_dims

        x, y = x / board_width, y / board_height
        width, height = width / board_width, height / board_height

        text = Text(self.board, bg="red")
        text.place(relx=x, rely=y, relheight=height, relwidth=width, anchor="nw")
        self.board.delete("line")
        items = ["autoseparators", "background", "borderwidth", "cursor", "foreground", "highlightbackground",
                 "highlightcolor", "relief", "highlightthickness", "insertborderwidth"
                 "padx", "pady", "wrap"]

        self.manager.switch(text, "Text", items)

    def set_root(self):
        self.manager.set_root(self.board)

    def create_fake_frame(self):
        x, y, w, h = self.fake_frame_coords
        self.board.create_rectangle(x, y, w, h, width=0, fill=self.manager.frame_background)
        self.board.delete("line")

    def set_bind(self):
        self.manager.bind("<<LABEL>>", lambda *args: self.create_label())
        self.manager.bind("<<ENTRY>>", lambda *args: self.create_entry())
        self.manager.bind("<<SETROOT>>", lambda *args: self.set_root())
        self.manager.bind("<<BUTTON>>", lambda *args: self.create_button())
        self.manager.bind("<<RADIOBUTTON>>", lambda *args: self.create_radiobutton())
        self.manager.bind("<<CHECKBUTTON>>", lambda *args: self.create_checkbutton())
        self.manager.bind("<<COMBOBOX>>", lambda *args: self.create_combobox())
        self.manager.bind("<<TEXT>>", lambda *args: self.create_text())
        self.manager.bind("<<SPINBOX>>", lambda *args: self.create_spinbox())
        self.manager.bind("<<LISTBOX>>", lambda *args: self.create_listbox())
        self.manager.bind("<<FRAME>>", lambda *args: self.create_frame())
        self.manager.bind("<<GenFrame>>", lambda *args: self.create_fake_frame())


if __name__ == '__main__':
    root = Tk()

    App(root)

    root.mainloop()
