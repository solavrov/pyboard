from kivy.app import App
from drawboard import *


class MyApp(App):

    def build(self):

        b = DrawBoard()

        t = Tree()
        t.grow(10)
        b.add(t)

        b.paint()

        return b


if __name__ == "__main__":
    MyApp().run()
