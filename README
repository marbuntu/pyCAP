# pyCAP

**pyCAP** is an open-source Python framework for building and simulating modular signal-processing and mixed-signal systems.

The project aims to provide a lightweight and extensible environment for rapidly prototyping signal chains composed of reusable functional blocks, such as signal generators, ADCs, DSP algorithms, and other processing elements. The framework is built around a clean block-and-port abstraction with an event-driven simulation engine and integrated signal tracing.

## Features

* Modular block-based architecture
* Typed input, output, and debug ports
* Event-driven simulation scheduler
* Automatic signal tracing and visualization
* Simple API for implementing custom processing blocks
* Fully written in Python

## Example

```python
with Simulator(Tsim, dTsim) as sim:

    gen = SignalGenerator() \
        .every(dTsim)

    adc = ADC(5.0, True, 12) \
        .every(sample_period, conversion_delay)

    adc.inp_Ain.connect(gen.out_Aout)

    sim.add(gen)
    sim.add(adc)

    sim.run()
```

## Status

pyCAP is currently in an early stage of development. The API is evolving and breaking changes should be expected while the core architecture is refined.

Feedback, suggestions, and contributions are always welcome.

## License

This project is released under the MIT License.
