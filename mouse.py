from pymouse import PyMouse
from time import sleep


class Mouse(PyMouse):

    def __init__(self):
        super().__init__()

    def left_click(self, x, y, n=1, wait=.1):
        self.click(x, y, button=1, n=n)
        sleep(wait)

    def right_click(self, x, y, n=1, wait=.1):
        self.click(x, y, button=2, n=n)
        sleep(wait)

    def drag(self, x0, y0, x1=0, y1=0):
        self.move(x0, y0)
        super().drag(x1, y1)

    def move(self, x, y, wait=0):
        super().move(int(x), int(y))
        sleep(wait)
