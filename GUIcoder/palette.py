from tkinter import Toplevel, Frame
from GUIcoder.myTkinter import myButton
from GUIcoder.selector import ColorSelector
from pyperclip import copy


class Palette(Frame):
    def __init__(self, master):
        super().__init__(master, bg='#435661')
        master.geometry('200x400+50+100')
        master.title("")
        self.record = [None for _ in range(32)]

        self.b11 = myButton(self, text=" + ", font=("", 32), command=lambda *args: self.clicked(0))
        self.b11.place(relx=0.025, rely=0.012, relwidth=0.215, relheight=0.108, anchor='nw')

        self.b12 = myButton(self, text=" + ", font=("", 32), command=lambda *args: self.clicked(1))
        self.b12.place(relx=0.27, rely=0.012, relwidth=0.215, relheight=0.108, anchor='nw')

        self.b13 = myButton(self, text=" + ", font=("", 32), command=lambda *args: self.clicked(2))
        self.b13.place(relx=0.515, rely=0.012, relwidth=0.215, relheight=0.108, anchor='nw')

        self.b14 = myButton(self, text=" + ", font=("", 32), command=lambda *args: self.clicked(3))
        self.b14.place(relx=0.758, rely=0.012, relwidth=0.215, relheight=0.108, anchor='nw')

        self.b21 = myButton(self, text=" + ", font=("", 32), command=lambda *args: self.clicked(4))
        self.b21.place(relx=0.025, rely=0.135, relwidth=0.215, relheight=0.108, anchor='nw')

        self.b22 = myButton(self, text=" + ", font=("", 32), command=lambda *args: self.clicked(5))
        self.b22.place(relx=0.271, rely=0.135, relwidth=0.215, relheight=0.108, anchor='nw')

        self.b23 = myButton(self, text=" + ", font=("", 32), command=lambda *args: self.clicked(6))
        self.b23.place(relx=0.517, rely=0.135, relwidth=0.215, relheight=0.108, anchor='nw')

        self.b24 = myButton(self, text=" + ", font=("", 32), command=lambda *args: self.clicked(7))
        self.b24.place(relx=0.761, rely=0.136, relwidth=0.215, relheight=0.108, anchor='nw')

        self.b31 = myButton(self, text=" + ", font=("", 32), command=lambda *args: self.clicked(8))
        self.b31.place(relx=0.025, rely=0.258, relwidth=0.215, relheight=0.108, anchor='nw')

        self.b32 = myButton(self, text=" + ", font=("", 32), command=lambda *args: self.clicked(9))
        self.b32.place(relx=0.27, rely=0.258, relwidth=0.215, relheight=0.108, anchor='nw')

        self.b33 = myButton(self, text=" + ", font=("", 32), command=lambda *args: self.clicked(10))
        self.b33.place(relx=0.517, rely=0.258, relwidth=0.215, relheight=0.108, anchor='nw')

        self.b34 = myButton(self, text=" + ", font=("", 32), command=lambda *args: self.clicked(11))
        self.b34.place(relx=0.759, rely=0.258, relwidth=0.215, relheight=0.108, anchor='nw')

        self.b41 = myButton(self, text=" + ", font=("", 32), command=lambda *args: self.clicked(12))
        self.b41.place(relx=0.025, rely=0.38, relwidth=0.215, relheight=0.108, anchor='nw')

        self.b42 = myButton(self, text=" + ", font=("", 32), command=lambda *args: self.clicked(13))
        self.b42.place(relx=0.268, rely=0.38, relwidth=0.215, relheight=0.108, anchor='nw')

        self.b43 = myButton(self, text=" + ", font=("", 32), command=lambda *args: self.clicked(14))
        self.b43.place(relx=0.515, rely=0.38, relwidth=0.215, relheight=0.108, anchor='nw')

        self.b44 = myButton(self, text=" + ", font=("", 32), command=lambda *args: self.clicked(15))
        self.b44.place(relx=0.76, rely=0.38, relwidth=0.215, relheight=0.108, anchor='nw')

        self.b51 = myButton(self, text=" + ", font=("", 32), command=lambda *args: self.clicked(16))
        self.b51.place(relx=0.025, rely=0.502, relwidth=0.215, relheight=0.108, anchor='nw')

        self.b52 = myButton(self, text=" + ", font=("", 32), command=lambda *args: self.clicked(17))
        self.b52.place(relx=0.27, rely=0.502, relwidth=0.215, relheight=0.108, anchor='nw')

        self.b53 = myButton(self, text=" + ", font=("", 32), command=lambda *args: self.clicked(18))
        self.b53.place(relx=0.515, rely=0.502, relwidth=0.215, relheight=0.108, anchor='nw')

        self.b54 = myButton(self, text=" + ", font=("", 32), command=lambda *args: self.clicked(19))
        self.b54.place(relx=0.761, rely=0.502, relwidth=0.215, relheight=0.108, anchor='nw')

        self.b61 = myButton(self, text=" + ", font=("", 32), command=lambda *args: self.clicked(20))
        self.b61.place(relx=0.025, rely=0.625, relwidth=0.215, relheight=0.108, anchor='nw')

        self.b62 = myButton(self, text=" + ", font=("", 32), command=lambda *args: self.clicked(21))
        self.b62.place(relx=0.27, rely=0.625, relwidth=0.215, relheight=0.108, anchor='nw')

        self.b63 = myButton(self, text=" + ", font=("", 32), command=lambda *args: self.clicked(22))
        self.b63.place(relx=0.515, rely=0.625, relwidth=0.215, relheight=0.108, anchor='nw')

        self.b64 = myButton(self, text=" + ", font=("", 32), command=lambda *args: self.clicked(23))
        self.b64.place(relx=0.76, rely=0.625, relwidth=0.215, relheight=0.108, anchor='nw')

        self.b71 = myButton(self, text=" + ", font=("", 32), command=lambda *args: self.clicked(24))
        self.b71.place(relx=0.025, rely=0.748, relwidth=0.215, relheight=0.108, anchor='nw')

        self.b72 = myButton(self, text=" + ", font=("", 32), command=lambda *args: self.clicked(25))
        self.b72.place(relx=0.272, rely=0.748, relwidth=0.215, relheight=0.108, anchor='nw')

        self.b73 = myButton(self, text=" + ", font=("", 32), command=lambda *args: self.clicked(26))
        self.b73.place(relx=0.515, rely=0.748, relwidth=0.215, relheight=0.108, anchor='nw')

        self.b74 = myButton(self, text=" + ", font=("", 32), command=lambda *args: self.clicked(27))
        self.b74.place(relx=0.76, rely=0.748, relwidth=0.215, relheight=0.108, anchor='nw')

        self.b81 = myButton(self, text=" + ", font=("", 32), command=lambda *args: self.clicked(28))
        self.b81.place(relx=0.025, rely=0.87, relwidth=0.215, relheight=0.108, anchor='nw')

        self.b82 = myButton(self, text=" + ", font=("", 32), command=lambda *args: self.clicked(29))
        self.b82.place(relx=0.27, rely=0.87, relwidth=0.215, relheight=0.108, anchor='nw')

        self.b83 = myButton(self, text=" + ", font=("", 32), command=lambda *args: self.clicked(30))
        self.b83.place(relx=0.517, rely=0.87, relwidth=0.215, relheight=0.108, anchor='nw')

        self.b84 = myButton(self, text=" + ", font=("", 32), command=lambda *args: self.clicked(31))
        self.b84.place(relx=0.76, rely=0.87, relwidth=0.215, relheight=0.108, anchor='nw')

        self.lst = [self.b11, self.b12, self.b13, self.b14,
                    self.b21, self.b22, self.b23, self.b24,
                    self.b31, self.b32, self.b33, self.b34,
                    self.b41, self.b42, self.b43, self.b44,
                    self.b51, self.b52, self.b53, self.b54,
                    self.b61, self.b62, self.b63, self.b64,
                    self.b71, self.b72, self.b73, self.b74,
                    self.b81, self.b82, self.b83, self.b84]

    def clicked(self, k, color=False):
        button = self.lst[k]
        top = Toplevel(self)
        top.geometry("200x400+50+100")
        top.title("")

        selec = ColorSelector(top, k, color) if color else ColorSelector(top, k)
        selec.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.wait_window(top)

        _hex = selec.color
        if _hex:
            button.configure(text="", bg=_hex)
            button.command = lambda *args: copy(_hex)  # !!!!!
            button.bind("<Button-3>", lambda *args: self.clicked(k, _hex))
        else:
            button.unbind("<Button-3>")
            button.command = lambda *args: self.clicked(k)
            button.configure(text=" + ", font=("", 32), bg="#557282")
