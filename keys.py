from pykeyboard import PyKeyboard
from time import sleep


class Keys(PyKeyboard):

    def __init__(self):
        super().__init__()

    # ------------------------------
    # region MAIN FUNCTIONS
    def tap(self, *chars, n=1, wait=0):
        for _ in range(n):
            for char in chars:
                self.press_key(char)
            for char in chars:
                self.release_key(char)
            sleep(wait)

    def hold(self, key, t=1):
        self.press_key(key)
        sleep(t)
        self.release_key(key)
    # endregion
    # ------------------------------

    # ------------------------------
    # region PRESS SINGLE KEY
    def press_tab(self, n=1, wait=0):
        self.tap(self.tab_key, n=n, wait=wait)

    def press_space(self, n=1, wait=0):
        self.tap(self.space, n=n, wait=wait)

    def press_enter(self, n=1, wait=0):
        self.tap(self.enter_key, n=n, wait=wait)

    def press_down(self, n=1, wait=0):
        self.tap(self.down_key, n=n, wait=wait)

    def press_up(self, n=1, wait=0):
        self.tap(self.up_key, n=n, wait=wait)

    def press_right(self, n=1, wait=0):
        self.tap(self.right_key, n=n, wait=wait)

    def press_left(self, n=1, wait=0):
        self.tap(self.left_key, n=n, wait=wait)

    def press_esc(self, n=1, wait=0):
        self.tap(self.escape_key, n=n, wait=wait)
    # endregion
    # ------------------------------

    # ------------------------------
    # region PRESS CTRL &
    def press_ctrl_enter(self, n=1, wait=0):
        self.tap(self.control_key, self.enter_key, n=n, wait=wait)

    def press_ctrl_tab(self, n=1, wait=0):
        self.tap(self.control_key, self.tab_key, n=n, wait=wait)

    def press_ctrl_w(self, n=1, wait=0):
        self.tap(self.control_key, 'w', n=n, wait=wait)
    # endregion
    # ------------------------------

    # ------------------------------
    # region PRESS SHIFT &
    def press_shift_left(self, n=1, wait=0):
        self.tap(self.shift_key, self.left_key, n=n, wait=wait)

    def press_shift_tab(self, n=1, wait=0):
        self.tap(self.shift_key, self.tab_key, n=n, wait=wait)
    # endregion
    # ------------------------------

    # ------------------------------
    # region PRESS ALT &
    def press_alt_tab(self, n=1, wait=0):
        self.tap(self.alt_key, self.tab_key, n=n, wait=wait)
    # endregion
    # ------------------------------

    def hold_down(self, t=1):
        self.hold(self.down_key, t)
