class Writer:
    def __init__(self):
        self.app_background = "white"
        self.app_geometry = "1000x800+700+100"
        self.app_transparency = 1
        self.record = {}
        self.standard_params = {}
        self.beginning = "from tkinter import *\n"\
                         "from tkinter.ttk import Button as TButton\n"\
                         "from tkinter.ttk import Combobox as TCombobox\n\n\n"\
                         "class App(Frame):\n"\
                         "    def __init__(self, master):\n"\
                         "        super().__init__(master, bg='{}')\n"\
                         "        master.geometry('{}')\n"\
                         "        master.attributes('-alpha', {})\n\n"

        self.widgets = {}

    def define_widget(self, widget_name, widget_cls, place_info, modifying=False):
        text = f"        self.{widget_name} = {widget_cls}(self)\n" \
               f"        self.{widget_name}.place("

        if widget_cls == "Button":
            text = f"        self.{widget_name} = ttk.{widget_cls}(self)" \
                   f"\n        self.{widget_name}.place("

        for key, value in place_info.items():
            if key in ["relx", "rely", "relwidth", "relheight"]:
                text += f"{key}={value}, "

        if modifying:
            self.widgets[widget_name][0] = text[:-2] + ")\n"
            self.widgets[widget_name] = [self.widgets[widget_name][0]]
        else:
            self.widgets[widget_name] = [text[:-2] + ")\n"]

    def begin_configure(self, widget_name):
        self.widgets[widget_name].append(f"        self.{widget_name}.configure(")

    def write_configure(self, widget_name, key, value):
        self.widgets[widget_name].append(f"{key}={value}, ")

    def end_configure(self, widget_name):
        if self.widgets[widget_name][-1] == f"        self.{widget_name}.configure(":
            self.widgets[widget_name][-1] = "\n\n"
        else:
            self.widgets[widget_name][-1] = self.widgets[widget_name][-1][:-2] + ")\n\n"

    def write_py(self):
        for widget in self.widgets:
            self.beginning += f"        self.{widget} = None\n"
        self.beginning += "\n        self.set_layout()\n\n"\
                          "    def set_layout(self):\n"

        self.beginning = self.beginning.format(self.app_background, self.app_geometry, self.app_transparency)

        end = "\n" \
              "if __name__ == '__main__':\n" \
              "    root = Tk()\n\n" \
              "    App(root).place(relx=0, rely=0, relwidth=1, relheight=1)\n\n" \
              "    root.mainloop()\n\n"

        text = self.beginning

        for _, code in self.widgets.items():
            for couple in code:
                text += couple
        text += end

        with open("Prototype.py", "w") as file:
            file.write(text)
