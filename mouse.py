from pymouse import PyMouse


class Mouse(PyMouse):

    def __init__(self):
        super().__init__()

    def left_click(self, x, y, n=1):
        self.click(x, y, button=1, n=n)

    def right_click(self, x, y, n=1):
        self.click(x, y, button=2, n=n)
