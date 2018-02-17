import math
from kivy.uix.widget import Widget
from kivy.graphics import Color, Line, Ellipse


class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.color = (1, 1, 1)
        self.width = 1

    def draw(self, canvas):
        with canvas:
            Color(*self.color)
            Ellipse(pos=(self.x - self.width / 2, self.y - self.width / 2),
                    size=(self.width, self.width))


class Segment:

    def __init__(self, x1, y1, x2, y2):
        self.p1 = Point(x1, y1)
        self.p2 = Point(x2, y2)
        self.color = (1, 1, 1)
        self.width = 1

    def draw(self, canvas):
        with canvas:
            Color(*self.color)
            Line(points=(self.p1.x, self.p1.y, self.p2.x, self.p2.y),
                 width=self.width)

    def get_angle(self):

        dx = self.p2.x - self.p1.x
        dy = self.p2.y - self.p1.y

        if dx != 0:
            a = math.atan(dy / dx) / math.pi * 180
            if dx > 0:
                if dy >= 0:
                    pass
                else:
                    a += 360
            else:
                a += 180
        else:
            if dy >= 0:
                a = 90
            else:
                a = 270

        return a


class Tree:

    def __init__(self):
        self.age = 0
        self.pos = 400
        self.stem_len = 100
        self.branch_len = 20
        self.angle = 45
        self.thickness = 2
        self.color = (0, 1, 0)
        self.branches = []

    def get_new_branch(self, branch, direction):
        a = branch.get_angle() + direction * self.angle / 2
        dx = self.branch_len * math.cos(a / 180 * math.pi)
        dy = self.branch_len * math.sin(a / 180 * math.pi)
        b = Segment(branch.p2.x, branch.p2.y, branch.p2.x + dx, branch.p2.y + dy)
        b.color = self.color
        b.width = self.thickness
        return b

    def grow(self, ages=1):
        for i in range(ages):
            if not self.branches:
                stem = Segment(self.pos, 0, self.pos, self.stem_len)
                stem.color = self.color
                stem.width = self.thickness
                self.branches.append(stem)
            else:
                new_branches = []
                for b in self.branches:
                    new_branches.append(self.get_new_branch(b, -1))
                    new_branches.append(self.get_new_branch(b, +1))
                self.branches += new_branches
            self.age += 1
        return self

    def draw(self, canvas):
        for b in self.branches:
            b.draw(canvas)


class DrawBoard(Widget):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.figures = []

    def add(self, figure):
        self.figures.append(figure)

    def move_up(self, fig):
        i = self.figures.index(fig)
        if i < self.figures.__len__() - 1:
            self.figures[i], self.figures[i + 1] = self.figures[i + 1], self.figures[i]

    def move_down(self, fig):
        i = self.figures.index(fig)
        if i > 0:
            self.figures[i - 1], self.figures[i] = self.figures[i], self.figures[i - 1]

    def remove(self, fig):
        self.figures.remove(fig)

    def paint(self):
        self.canvas.clear()
        for fig in self.figures:
            fig.draw(self.canvas)


if __name__ == "__main__":
    pass
