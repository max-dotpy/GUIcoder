from tkinter import Frame
from myTkinter import myButton


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
