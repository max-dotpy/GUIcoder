from tkinter import Toplevel, Entry


class Palette(Toplevel):
    def __init__(self, master):
        super().__init__(master, bg='#435661')
        self.geometry('200x400+50+100')
        self.title("Palette")

        Entry(self, background='#defffc', borderwidth='2', justify='center', highlightthickness=0)\
            .place(relx=0.15, rely=0.065, relwidth=0.7, relheight=0.07, anchor='nw')

        Entry(self, background='#defffc', borderwidth='2', justify='center', highlightthickness=0)\
            .place(relx=0.15, rely=0.203, relwidth=0.7, relheight=0.074, anchor='nw')

        Entry(self, background='#defffc', borderwidth='2', justify='center', highlightthickness=0)\
            .place(relx=0.15, rely=0.343, relwidth=0.7, relheight=0.075, anchor='nw')

        Entry(self, background='#defffc', borderwidth='2', justify='center', highlightthickness=0)\
            .place(relx=0.15, rely=0.480, relwidth=0.7, relheight=0.075, anchor='nw')

        Entry(self, background='#defffc', borderwidth='2', justify='center', highlightthickness=0)\
            .place(relx=0.15, rely=0.633, relwidth=0.7, relheight=0.079, anchor='nw')

        Entry(self, background='#defffc', borderwidth='2', justify='center', highlightthickness=0)\
            .place(relx=0.15, rely=0.785, relwidth=0.7, relheight=0.078, anchor='nw')
