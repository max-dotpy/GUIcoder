from tkinter import Frame, Label, Spinbox, Listbox, Entry
from myTkinter import myButton


class Settings(Frame):
    def __init__(self, master, widget, items, modifying=False):
        super().__init__(master, bg="#435661")

        self.widget = widget
        self.modifying = modifying
        self.record = {}
        self.index = 0
        self.spin_relx = None
        self.spin_rely = None
        self.spin_relw = None
        self.spin_relh = None
        self.label_arguments = None
        self.entry_arguments = None
        self.listbox = None
        self.entry_name = None
        self.set_layout()
        self.set_bindings()
        self.set_listbox(items)
        self.set_spinboxes()

    def set_layout(self):
        # self-explanatory
        Label(self, background='#435661', text='relx:', foreground='#defffc') \
            .place(relx=0.145, rely=0.0125, relwidth=0.1625, relheight=0.025, anchor='nw')

        Label(self, background='#435661', foreground='#defffc', text='rely:') \
            .place(relx=0.6845, rely=0.0135, relwidth=0.155, relheight=0.0225, anchor='nw')

        Label(self, background='#435661', text='relwidth:', foreground='#defffc') \
            .place(relx=0.044, rely=0.089, relwidth=0.37, relheight=0.02125, anchor='nw')

        Label(self, background='#435661', foreground='#defffc', text='relheight:') \
            .place(relx=0.667, rely=0.0875, relwidth=0.195, relheight=0.02375, anchor='nw')

        self.spin_relx = Spinbox(self, readonlybackground='#defffc', highlightthickness=0,
                                 foreground='#435661', from_=0, command=self.mod_relx, to_=1,
                                 increment=0.001, justify='center')
        self.spin_relx.place(relx=0.085, rely=0.0425, relwidth=0.295, relheight=0.03375, anchor='nw')

        self.spin_rely = Spinbox(self, readonlybackground='#defffc', foreground='#435661',
                                 justify='center', highlightthickness=0, command=self.mod_rely,
                                 from_=0, to_=1, increment=0.001)
        self.spin_rely.place(relx=0.6135, rely=0.0425, relwidth=0.3005, relheight=0.03375, anchor='nw')

        self.spin_relw = Spinbox(self, readonlybackground='#defffc', foreground='#435661',
                                 justify='center', highlightthickness=0, command=self.mod_relwidth,
                                 from_=0, to_=1, increment=0.001)
        self.spin_relw.place(relx=0.084, rely=0.1175, relwidth=0.295, relheight=0.035, anchor='nw')

        self.spin_relh = Spinbox(self, readonlybackground='#defffc', foreground='#435661',
                                 justify='center', highlightthickness=0, command=self.mod_relheight,
                                 from_=0, to_=1, increment=0.001)
        self.spin_relh.place(relx=0.6115, rely=0.1177, relwidth=0.304, relheight=0.035, anchor='nw')

        self.label_arguments = Label(self, background='#557282', foreground='#defffc')
        self.label_arguments.place(relx=0.086, rely=0.1832, relwidth=0.8305, relheight=0.06125, anchor='nw')

        self.entry_arguments = Entry(self, background='#defffc', foreground='#435661', justify='center')
        self.entry_arguments.place(relx=0.22, rely=0.2625, relwidth=0.545, relheight=0.04375, anchor='nw')

        self.listbox = Listbox(self, background='#557282', foreground='#defffc', borderwidth=0)
        self.listbox.place(relx=0.085, rely=0.3275, relwidth=0.83, relheight=0.4062, anchor='nw')

        myButton(self, command=lambda *a: self.set_value(), text='OK') \
            .place(relx=0.8245, rely=0.2672, relwidth=0.13, relheight=0.0355, anchor='nw')

        Label(self, background='#435661', foreground='#defffc', text='Name:', anchor='w') \
            .place(relx=0.083, rely=0.766, relwidth=0.1205, relheight=0.035, anchor='nw')

        self.entry_name = Entry(self, background='#defffc', foreground='#435661', justify='center')
        self.entry_name.place(relx=0.245, rely=0.7662, relwidth=0.5225, relheight=0.035, anchor='nw')

        self.entry_name.bind("<Return>", lambda *a: self.confirm())

        myButton(self, command=lambda *a: self.confirm(), text='CONFIRM') \
            .place(relx=0.201, rely=0.8575, relwidth=0.6155, relheight=0.0825, anchor='nw')

    def set_bindings(self):
        # self-explanatory
        self.entry_arguments.bind("<Return>", lambda *a: self.set_value())
        self.listbox.bind("<ButtonRelease-1>", lambda *a: self.listbox_clicked())

        self.master.root.bind("<Left>", lambda event: self.pressed_left_right(-1))
        self.master.root.bind("<Right>", lambda event: self.pressed_left_right(1))

        self.master.root.bind("<Up>", lambda event: self.pressed_up_down(-1))
        self.master.root.bind("<Down>", lambda event: self.pressed_up_down(1))

    def set_spinboxes(self):
        # self-explanatory
        self.spin_relx.delete(0, "end")
        self.spin_rely.delete(0, "end")
        self.spin_relw.delete(0, "end")
        self.spin_relh.delete(0, "end")

        self.spin_relx.insert("end", self.widget.place_info()["relx"])
        self.spin_rely.insert("end", self.widget.place_info()["rely"])
        self.spin_relw.insert("end", self.widget.place_info()["relwidth"])
        self.spin_relh.insert("end", self.widget.place_info()["relheight"])

        self.spin_relx.configure(state="readonly")
        self.spin_rely.configure(state="readonly")
        self.spin_relw.configure(state="readonly")
        self.spin_relh.configure(state="readonly")

    def mod_relx(self):
        # Changes widget's relx parameter accordingly
        value = float(self.spin_relx.get())
        self.widget.place_configure(relx=value)

    def mod_rely(self):
        # Changes widget's rely parameter accordingly
        value = float(self.spin_rely.get())
        self.widget.place_configure(rely=value)

    def mod_relwidth(self):
        # Changes widget's relwidth parameter accordingly
        value = float(self.spin_relw.get())
        self.widget.place_configure(relwidth=value)

    def mod_relheight(self):
        # Changes widget's relheight parameter accordingly
        value = float(self.spin_relh.get())
        self.widget.place_configure(relheight=value)

    def pressed_left_right(self, factor):
        value = float(self.spin_relx.get())
        self.spin_relx.configure(state="normal")
        self.spin_relx.delete(0, "end")
        self.spin_relx.insert("end", value + factor * 0.001)
        self.spin_relx.configure(state="readonly")
        self.widget.place_configure(relx=value + factor * 0.001)

    def pressed_up_down(self, factor):
        value = float(self.spin_rely.get())
        self.spin_rely.configure(state="normal")
        self.spin_rely.delete(0, "end")
        self.spin_rely.insert("end", value + factor * 0.001)
        self.spin_rely.configure(state="readonly")
        self.widget.place_configure(rely=value + factor * 0.001)

    def set_listbox(self, items):
        for item in items:
            self.listbox.insert("end", item)
            self.record[item] = self.widget.cget(item)

    def listbox_clicked(self):
        # Changes entry_arguments's text and label_arguments's text, sets focus on entry_name
        self.index = self.listbox.curselection()[0]
        parameter = list(self.record.keys())[self.index]
        value = self.record[parameter]
        self.entry_arguments.delete(0, "end")
        self.entry_arguments.insert("end", value)
        self.label_arguments.configure(text=f"{parameter} = {value}")
        self.entry_arguments.focus_set()

    def set_value(self):
        # Sets entry_arguments's value as widget's argument, it needs to be evaluated first to avoid errors
        parameter = list(self.record.keys())[self.index]
        value = self.entry_arguments.get()

        try:
            evaluated_value = eval(value)
            self.record[parameter] = evaluated_value
        except:
            evaluated_value = value
            self.record[parameter] = f"{evaluated_value}"

        self.widget.configure({parameter: evaluated_value})

        self.label_arguments.configure(text=f"{parameter} = {value}")

    def confirm(self):
        # Checks if entry_name isn't empty or already used and then sends it to the master.Writer
        # After that it quits with .destroy()
        name = self.entry_name.get().replace(" ", "")
        if not self.modifying:
            if name and name not in self.master.record_of_names:
                self.master.record_of_names[name] = self.widget
                widget_cls = self.widget.winfo_class()

                self.master.writer.define_widget(name, widget_cls, self.widget.place_info())
                self.master.writer.begin_configure(name)
                for key, value in self.record.items():
                    if value:
                        self.master.writer.write_configure(name, key, f"'{value}'")
                self.master.writer.end_configure(name)

                self.master.root.unbind("<Down>")
                self.master.root.unbind("<Up>")
                self.master.root.unbind("<Left>")
                self.master.root.unbind("<Right>")

                self.destroy()
        else:
            widget_cls = self.widget.winfo_class()

            try:
                self.master.writer.define_widget(name, widget_cls, self.widget.place_info(), True)
                self.master.writer.begin_configure(name)
            except KeyError:
                self.entry_name.delete(0, "end")
                self.entry_name.insert("end", "NOME SBAGLIATO")
                return None

            for key, value in self.record.items():
                if value:
                    self.master.writer.write_configure(name, key, f"'{value}'")
            self.master.writer.end_configure(name)

            self.master.root.unbind("<Down>")
            self.master.root.unbind("<Up>")
            self.master.root.unbind("<Left>")
            self.master.root.unbind("<Right>")

            self.destroy()


class Settings_for_frame(Frame):
    def __init__(self, master, board, tag, board_dims):
        super().__init__(master, bg="#435661")

        self.board = board
        self.board_width, self.board_height = board_dims
        self.tag = tag
        self.background = "white"
        self.record = {}
        self.index = 0
        self.spin_relx = None
        self.spin_rely = None
        self.spin_relw = None
        self.spin_relh = None
        self.label_arguments = None
        self.entry_arguments = None
        self.listbox = None
        self.entry_name = None
        self.set_layout()
        self.set_bindings()
        self.set_listbox()
        self.set_spinboxes()

    def set_layout(self):
        # self-explanatory
        Label(self, background='#435661', text='relx:', foreground='#defffc') \
            .place(relx=0.145, rely=0.0125, relwidth=0.1625, relheight=0.025, anchor='nw')

        Label(self, background='#435661', foreground='#defffc', text='rely:') \
            .place(relx=0.6845, rely=0.0135, relwidth=0.155, relheight=0.0225, anchor='nw')

        Label(self, background='#435661', text='relwidth:', foreground='#defffc') \
            .place(relx=0.044, rely=0.089, relwidth=0.37, relheight=0.02125, anchor='nw')

        Label(self, background='#435661', foreground='#defffc', text='relheight:') \
            .place(relx=0.667, rely=0.0875, relwidth=0.195, relheight=0.02375, anchor='nw')

        self.spin_relx = Spinbox(self, readonlybackground='#defffc', highlightthickness=0,
                                 foreground='#435661', from_=0, command=self.mod, to_=1,
                                 increment=0.001, justify='center')
        self.spin_relx.place(relx=0.085, rely=0.0425, relwidth=0.295, relheight=0.03375, anchor='nw')

        self.spin_rely = Spinbox(self, readonlybackground='#defffc', foreground='#435661',
                                 justify='center', highlightthickness=0, command=self.mod,
                                 from_=0, to_=1, increment=0.001)
        self.spin_rely.place(relx=0.6135, rely=0.0425, relwidth=0.3005, relheight=0.03375, anchor='nw')

        self.spin_relw = Spinbox(self, readonlybackground='#defffc', foreground='#435661',
                                 justify='center', highlightthickness=0, command=self.mod,
                                 from_=0, to_=1, increment=0.001)
        self.spin_relw.place(relx=0.084, rely=0.1175, relwidth=0.295, relheight=0.035, anchor='nw')

        self.spin_relh = Spinbox(self, readonlybackground='#defffc', foreground='#435661',
                                 justify='center', highlightthickness=0, command=self.mod,
                                 from_=0, to_=1, increment=0.001)
        self.spin_relh.place(relx=0.6115, rely=0.1177, relwidth=0.304, relheight=0.035, anchor='nw')

        self.label_arguments = Label(self, background='#557282', foreground='#defffc')
        self.label_arguments.place(relx=0.086, rely=0.1832, relwidth=0.8305, relheight=0.06125, anchor='nw')

        self.entry_arguments = Entry(self, background='#defffc', foreground='#435661', justify='center')
        self.entry_arguments.place(relx=0.22, rely=0.2625, relwidth=0.545, relheight=0.04375, anchor='nw')

        self.listbox = Listbox(self, background='#557282', foreground='#defffc', borderwidth=0)
        self.listbox.place(relx=0.085, rely=0.3275, relwidth=0.83, relheight=0.4062, anchor='nw')

        myButton(self, command=lambda *a: self.set_value(), text='OK') \
            .place(relx=0.8245, rely=0.2672, relwidth=0.13, relheight=0.0355, anchor='nw')

        Label(self, background='#435661', foreground='#defffc', text='Name:', anchor='w') \
            .place(relx=0.083, rely=0.766, relwidth=0.1205, relheight=0.035, anchor='nw')

        self.entry_name = Entry(self, background='#defffc', foreground='#435661', justify='center')
        self.entry_name.place(relx=0.245, rely=0.7662, relwidth=0.5225, relheight=0.035, anchor='nw')

        myButton(self, command=lambda *a: self.confirm(), text='CONFIRM') \
            .place(relx=0.201, rely=0.8575, relwidth=0.6155, relheight=0.0825, anchor='nw')

    def set_bindings(self):
        # self-explanatory
        self.entry_arguments.bind("<Return>", lambda *a: self.set_value())
        self.listbox.bind("<ButtonRelease-1>", lambda *a: self.listbox_clicked())

    def set_spinboxes(self):
        # self-explanatory
        self.spin_relx.delete(0, "end")
        self.spin_rely.delete(0, "end")
        self.spin_relw.delete(0, "end")
        self.spin_relh.delete(0, "end")

        self.spin_relx.insert("end", self.master.fake_frame_place_info["relx"])
        self.spin_rely.insert("end", self.master.fake_frame_place_info["rely"])
        self.spin_relw.insert("end", self.master.fake_frame_place_info["relwidth"])
        self.spin_relh.insert("end", self.master.fake_frame_place_info["relheight"])

        self.spin_relx.configure(state="readonly")
        self.spin_rely.configure(state="readonly")
        self.spin_relw.configure(state="readonly")
        self.spin_relh.configure(state="readonly")

    def mod(self):
        relx = float(self.spin_relx.get())
        rely = float(self.spin_rely.get())
        relw = float(self.spin_relw.get())
        relh = float(self.spin_relh.get())

        x, y = int(relx * self.board_width), int(rely * self.board_height)
        width, height = int(relw * self.board_width), int(relh * self.board_height)

        self.board.delete(self.tag)
        self.board.create_rectangle(x, y, x + width, y + height, width=0, fill=self.background, tag=self.tag)

    def set_listbox(self):
        self.listbox.insert("end", "background")
        self.record["background"] = self.master.fake_frame_background

    def listbox_clicked(self):
        # Changes entry_arguments's text and label_arguments's text, sets focus on entry_name
        self.index = self.listbox.curselection()[0]
        parameter = list(self.record.keys())[self.index]
        value = self.record[parameter]
        self.entry_arguments.delete(0, "end")
        self.entry_arguments.insert("end", value)
        self.label_arguments.configure(text=f"{parameter} = {value}")
        self.entry_arguments.focus_set()

    def set_value(self):

        parameter = list(self.record.keys())[self.index]
        value = self.entry_arguments.get()

        try:
            evaluated_value = eval(value)
            self.record[parameter] = evaluated_value
        except:
            evaluated_value = value
            self.record[parameter] = f"{evaluated_value}"

        self.background = evaluated_value
        self.mod()

        self.label_arguments.configure(text=f"{parameter} = {value}")

    def fake_place_info(self):
        relx = float(self.spin_relx.get())
        rely = float(self.spin_rely.get())
        relw = float(self.spin_relw.get())
        relh = float(self.spin_relh.get())
        return {"relx": relx, "rely": rely, "relwidth": relw, "relheight": relh, "anchor": "nw"}

    def confirm(self):
        name = self.entry_name.get().replace(" ", "")
        if name and name not in self.master.record_of_names:
            self.master.record_of_names[name] = Frame(self.board)
            widget_cls = "Frame"

            self.master.writer.define_widget(name, widget_cls, self.fake_place_info())
            self.master.writer.begin_configure(name)
            for key, value in self.record.items():
                if value:
                    self.master.writer.write_configure(name, key, f"'{value}'")
            self.master.writer.end_configure(name)

            self.destroy()


class Settings_for_root(Frame):
    def __init__(self, master, board, writer, background, dimensions):
        super().__init__(master, bg='#435661')

        self.board = board
        self.writer = writer
        self.entry_background = None
        self.spinbox_w = None
        self.spinbox_h = None
        self.spinbox_x = None
        self.spinbox_y = None
        self.set_layout(background, dimensions)

    def set_layout(self, background, dimensions):
        w, h, x, y = dimensions

        Label(self, background='#435661', foreground='#defffc', highlightbackground='White', text='width:') \
            .place(relx=0.065, rely=0.0125, relwidth=0.375, relheight=0.02875, anchor='nw')

        Label(self, background='#435661', foreground='#defffc', text='height:') \
            .place(relx=0.591, rely=0.012, relwidth=0.262, relheight=0.028, anchor='nw')

        self.spinbox_w = Spinbox(self, background='#defffc', foreground='#435661', from_=0, to_=10000,
                                 justify='center', highlightthickness=0, increment=1, command=self.apply)
        self.spinbox_w.place(relx=0.115, rely=0.0525, relwidth=0.2875, relheight=0.04625, anchor='nw')

        self.spinbox_h = Spinbox(self, background='#defffc', foreground='#435661', from_=0, to_=10000,
                                 justify='center', highlightthickness=0, increment=1, command=self.apply)
        self.spinbox_h.place(relx=0.595, rely=0.053, relwidth=0.279, relheight=0.046, anchor='nw')

        Label(self, background='#435661', foreground='#defffc', highlightbackground='White',
              text="x offset:                                         y offset:") \
            .place(relx=0.067, rely=0.16, relwidth=0.835, relheight=0.03375, anchor='nw')

        self.spinbox_x = Spinbox(self, background='#defffc', foreground='#435661', from_=0, to_=10000,
                                 justify='center', highlightthickness=0, increment=1, command=self.apply)
        self.spinbox_x.place(relx=0.1175, rely=0.2062, relwidth=0.279, relheight=0.048, anchor='nw')

        self.spinbox_y = Spinbox(self, background='#defffc', foreground='#435661', from_=0, to_=10000,
                                 justify='center', highlightthickness=0, increment=1, command=self.apply)
        self.spinbox_y.place(relx=0.593, rely=0.206, relwidth=0.2775, relheight=0.048, anchor='nw')

        Label(self, background='#435661', foreground='#defffc', text='background:') \
            .place(relx=0.293, rely=0.3287, relwidth=0.405, relheight=0.0475, anchor='nw')

        self.entry_background = Entry(self, background='#defffc', foreground='#435661', justify="center")
        self.entry_background.place(relx=0.29, rely=0.3837, relwidth=0.405, relheight=0.043, anchor='nw')

        myButton(self, text='APPLY', command=self.apply) \
            .place(relx=0.217, rely=0.5475, relwidth=0.549, relheight=0.06375, anchor='nw')

        myButton(self, text='CONFIRM', command=self.confirm) \
            .place(relx=0.305, rely=0.8, relwidth=0.385, relheight=0.08875, anchor='nw')

        self.spinbox_w.delete(0, "end")
        self.spinbox_h.delete(0, "end")
        self.spinbox_x.delete(0, "end")
        self.spinbox_y.delete(0, "end")
        self.spinbox_w.insert("end", w)
        self.spinbox_h.insert("end", h)
        self.spinbox_x.insert("end", x)
        self.spinbox_y.insert("end", y)

        self.entry_background.insert("end", background)

    def apply(self):
        self.board.configure(bg=self.entry_background.get())

        w = self.spinbox_w.get()
        h = self.spinbox_h.get()
        x = self.spinbox_x.get()
        y = self.spinbox_y.get()
        self.board.master.geometry(f"{w}x{h}+{x}+{y}")

    def confirm(self):
        self.board.configure(bg=self.entry_background.get())
        self.writer.app_background = self.entry_background.get()
        w = self.spinbox_w.get()
        h = self.spinbox_h.get()
        x = self.spinbox_x.get()
        y = self.spinbox_y.get()
        self.board.master.geometry(f"{w}x{h}+{x}+{y}")
        self.writer.app_geometry = f"{w}x{h}+{x}+{y}"
        self.destroy()
