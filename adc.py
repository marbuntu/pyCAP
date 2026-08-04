import numpy as np



class ADC():
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

        self.Vref = Vref
        self.bitw = bit_width
        self.diff = differential

        if (differential):
            sstep = Vref / ((2**(bit_width-1))-1)
            print(sstep, (2*Vref) / sstep)
            # posh = np.ara(0, Vref, 2**(bit_width-1))
            # negh = np.linspace(-Vref, 0, 2**(bit_width-1),)

            posh = np.arange(0, Vref + sstep, sstep)
            negh = np.arange(-(Vref + sstep), 0, sstep)

            self._steps = np.append(negh, posh)

        print(self._steps)

        # print(self._steps)


    def getSteps(self) -> np.array:
        return self._steps


    def convert(self, signal : float):

        # Clip the voltage to the valid range
        if self.diff:
            signal = np.clip(signal, -self.Vref, self.Vref)

        else:
            signal = np.clip(signal, 0, self.Vref)

        print(self._steps - signal)
        id = np.argmin(np.abs(self._steps - signal))

        return self._steps[id]




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