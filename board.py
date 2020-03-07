from tkinter import Canvas


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

    def draw_constraints(self, relx, rely, relw, relh):
        w, h = self.get_dims()

        x0, y0 = int(relx * w), int(rely * h)
        x1, y1 = x0 + int(relw * w), y0 + int(relh * h)

        self.create_line(x0, 0, x0, h, tag="constraint", width=1)
        self.create_line(x1, 0, x1, h, tag="constraint", width=1)
        self.create_line(0, y1, w, y1, tag="constraint", width=1)
        self.create_line(0, y0, w, y0, tag="constraint", width=1)
