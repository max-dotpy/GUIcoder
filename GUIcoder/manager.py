from tkinter import Toplevel
from GUIcoder.selector import Selector
from GUIcoder.settings import Settings, Settings_for_frame, Settings_for_root


# Toplevel, Frame, Setting, Selector
class Manager(Toplevel):
    def __init__(self, master, writer, root, **kwargs):
        super().__init__(master, **kwargs)
        self.title("Settings")
        self.master = master
        self.writer = writer
        self.root = root
        self.record_of_names = {}
        self.record_of_ids = {}
        self.selector = Selector(self, bg=self["bg"])
        self.fake_frame_background = "white"
        self.fake_frame_place_info = {}

        self.selector.place(relx=0, rely=0, relwidth=1, relheight=1)

    def switch(self, widget, items, modifying=False):
        settings = Settings(self, widget, items, modifying)
        settings.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.wait_window(settings)

    def switch_for_frame(self, board, tag, board_dims):
        settings = Settings_for_frame(self, board, tag, board_dims)
        settings.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.wait_window(settings)

    def set_root(self, board):
        str_dimensions = self.writer.app_geometry.replace("+", " ").replace("x", " ").split()
        dimensions = [int(dim) for dim in str_dimensions]
        settings = Settings_for_root(self, board, self.writer, self.writer.app_background,
                                     dimensions, self.writer.app_transparency)
        settings.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.wait_window(settings)
