
from signals import Signal

class BBox:

    def __init__(self, module_name : str):
        self.sig_in = Signal(f"{module_name}.in", 0.0)
        self.sig_out = Signal(f"{module_name}.out", 0.0)

