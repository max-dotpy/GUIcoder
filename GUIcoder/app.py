from tkinter import Toplevel, Label, Entry, Radiobutton, Checkbutton, Spinbox, Listbox, Text, Tk
from tkinter import ttk
from GUIcoder.board import Board
from GUIcoder.manager import Manager
from GUIcoder.writer import Writer
from GUIcoder.palette import Palette
from time import time


class App:
    def __init__(self, root):
        self.root = root
        self.writer = Writer()
        w = root.winfo_screenwidth() // 2
        root.geometry(f"{w}x800+{w // 4 * 3}+100")
        root.title("")

        top = Toplevel(root)
        Palette(top).place(relx=0, rely=0, relheight=1, relwidth=1)

        self.board = Board(root, height=800, width=w)
        self.board.pack(fill="both", expand=True)

        self.manager = Manager(root, self.writer, self.root, bg="#435661", height=800, width=w // 5 * 2)
        self.manager.geometry("+250+100")

        self.set_bind()

    def create_frame(self):
        P0, widget_dims, board_dims = self.board.get_geometry()
        x, y = P0
        width, height = widget_dims
        board_width, board_height = board_dims

        tag = str(time())

        self.board.create_rectangle(x, y, x + width, y + height, width=0, tag=tag)
        self.board.delete("line")

        x, y = x / board_width, y / board_height
        width, height = width / board_width, height / board_height
        self.manager.fake_frame_place_info = {"relx": x, "rely": y,
                                              "relwidth": width, "relheight": height, "anchor": "nw"}
        self.manager.switch_for_frame(self.board, tag, board_dims)

    def create_label(self):
        P0, widget_dims, board_dims = self.board.get_geometry()
        x, y = P0
        width, height = widget_dims
        board_width, board_height = board_dims

        x, y = x / board_width, y / board_height
        width, height = width / board_width, height / board_height

        label = Label(self.board)
        label.place(relx=x, rely=y, relheight=height, relwidth=width, anchor="nw")
        self.board.delete("line")
        items = [item for item in label.keys() if len(item) > 2]

        label.bind("<Enter>", lambda event: self.get_widget_info(label))
        label.bind("<Leave>", lambda event: self.focus_out())
        label.bind("<Button-3>", lambda event: self.modify(label, items))

        self.manager.switch(label, items)

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
        items = [item for item in entry.keys() if len(item) > 2]

        entry.bind("<Enter>", lambda event: self.get_widget_info(entry))
        entry.bind("<Leave>", lambda event: self.focus_out())
        entry.bind("<Button-3>", lambda event: self.modify(entry, items))

        self.manager.switch(entry, items)

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
        items = [item for item in button.keys() if len(item) > 2]

        button.bind("<Enter>", lambda event: self.get_widget_info(button))
        button.bind("<Leave>", lambda event: self.focus_out())
        button.bind("<Button-3>", lambda event: self.modify(button, items))

        self.manager.switch(button, items)

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
        items = [item for item in button.keys() if len(item) > 2]

        button.bind("<Enter>", lambda event: self.get_widget_info(button))
        button.bind("<Leave>", lambda event: self.focus_out())
        button.bind("<Button-3>", lambda event: self.modify(button, items))

        self.manager.switch(button, items)

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
        items = [item for item in button.keys() if len(item) > 2]

        button.bind("<Enter>", lambda event: self.get_widget_info(button))
        button.bind("<Leave>", lambda event: self.focus_out())
        button.bind("<Button-3>", lambda event: self.modify(button, items))

        self.manager.switch(button, items)

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
        items = [item for item in box.keys() if len(item) > 2]

        box.bind("<Enter>", lambda event: self.get_widget_info(box))
        box.bind("<Leave>", lambda event: self.focus_out())
        box.bind("<Button-3>", lambda event: self.modify(box, items))

        self.manager.switch(box, items)

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

        items = [item for item in box.keys() if len(item) > 2]

        box.bind("<Enter>", lambda event: self.get_widget_info(box))
        box.bind("<Leave>", lambda event: self.focus_out())
        box.bind("<Button-3>", lambda event: self.modify(box, items))

        self.manager.switch(box, items)

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

        items = [item for item in box.keys() if len(item) > 2]

        box.bind("<Enter>", lambda event: self.get_widget_info(box))
        box.bind("<Leave>", lambda event: self.focus_out())
        box.bind("<Button-3>", lambda event: self.modify(box, items))

        self.manager.switch(box, items)

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
        items = [item for item in text.keys() if len(item) > 2]

        text.bind("<Enter>", lambda event: self.get_widget_info(text))
        text.bind("<Leave>", lambda event: self.focus_out())
        text.bind("<Button-3>", lambda event: self.modify(text, items))

        self.manager.switch(text, items)

    def get_widget_info(self, widget):
        text = widget.winfo_geometry() + ",      ({}, {}, {}, {}) = (relx, rely, relwidth, relheight)"
        rels = []
        for key, value in widget.place_info().items():
            if key in ["relx", "rely", "relwidth", "relheight"]:
                rels.append(float(value))
        self.root.title(text.format(*rels))
        self.board.draw_constraints(*rels)

    def focus_out(self):
        self.root.title("")
        self.board.delete("constraint")

    def modify(self, widget, items):
        self.manager.switch(widget, items, modifying=True)

    def set_root(self):
        self.manager.set_root(self.board)

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


def main():
    root = Tk()

    App(root)

    root.mainloop()

    
if __name__ == '__main__':
    main()
