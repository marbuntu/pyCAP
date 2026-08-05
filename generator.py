
from bbox import BBox
from signals import Signal

class SignalGenerator(BBox):

    def __init__(self):
        super().__init__("generator")
        self._inner = 0


    def update(self):

        self._inner += 1
        self.sig_out.value = self._inner

        print(self._inner)