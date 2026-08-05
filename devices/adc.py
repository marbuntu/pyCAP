import numpy as np
from pyCAP.core.bbox import BBox
from pyCAP.core.timing import TimeValue
from pyCAP.core.signals import SignalPort


class ADC(BBox):

    def __init__(self, Vref : float, differential : bool = True, bit_width : int = 24):
        """
            ## ADC Converter

            Parameters
            ----------
            Vref : float
                Analog Reference Voltage.
                Unitless, the value should be in the same domain as the target signal

            differential : bool - default True
                Voltage swing is Differential (+Vref to -Vref) or Single Ended (+Vref to Gnd)

            bit_width : int - default 24
                Number of Bits

        """
        super().__init__("adc")
        self.ain = self._add_input("Ain")
        self.dout = self._add_output("Dout")

        self.Vref = Vref
        self.bitw = bit_width
        self.diff = differential

        self.last = 0.0

        if (differential):
            sstep = Vref / ((2**(bit_width-1))-1)

            posh = np.arange(0, Vref + sstep, sstep)
            negh = np.arange(-(Vref + sstep), 0, sstep)

            self._steps = np.append(negh, posh)

        else:

            self._steps = np.linspace(0, Vref, 2**bit_width)


    def getSteps(self) -> np.array:
        return self._steps


    def convert(self, signal : float) -> float:

        # Clip the voltage to the valid range
        if self.diff:
            signal = np.clip(signal, -self.Vref, self.Vref)

        else:
            signal = np.clip(signal, 0, self.Vref)

        id = np.argmin(np.abs(self._steps - signal))
        self.last = self._steps[id]

        return self._steps[id]
    

    def getValue(self) -> float:
        """
            Returns the Value of the last Conversion

            Return
            -------
            float - Last Conversion Value
        """
        return self.last

    def connectInput(self, port : SignalPort):
        self.ain.connect(port)
        return self

    def update(self, t : TimeValue):
        self.dout.value = self.convert(self.ain.value)
        #print(self.sig_out.value)



if __name__ == "__main__":
    import matplotlib.pyplot as plt

    adc = ADC(2.4, True, 4)

    steps = adc.getSteps()

    sig = np.linspace(-4, 3, 20)
    n = np.arange(len(sig))

    cv = [adc.convert(s) for s in sig]
 
    plt.step(n, sig)
    plt.step(n, cv)
    plt.show()