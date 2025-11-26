import numpy as np
import matplotlib.pyplot as plt
from tespy.networks import Network
from tespy.components import (
    DiabaticCombustionChamber, Turbine, Source, Sink, Compressor,
    Generator, PowerBus, PowerSink
)
from tespy.connections import Connection, Ref, PowerConnection

network = Network()
network.units.set_defaults(temperature="degC", pressure="bar",
                           heat="MW", power="MW")


lowPressureCompressor = Compressor("Low Pressure Compressor")
highPressureCompressor = Compressor("High Pressure Compressor")
combustionChamber = DiabaticCombustionChamber("Combustion Chamber")
highPressureTurbine = Turbine("High Pressure Turbine")
lowPressureTurbine = Turbine("Low Pressure Turbine")
air = Source("Air Source")
fuel = Source("Fuel Source")
flueGasSink = Sink("Flue Gas Sink")
lowPressureShaft = PowerBus("Low Pressure Shaft", num_in=1, num_out=1)
highPressureShaft = PowerBus("High Pressure Shaft", num_in=1, num_out=1)


# 1: air->lowPressureCompressor
c1 = Connection(air, "out1", lowPressureCompressor, "in1", label="1")

# 2: lowPressureCompressor->highPressureCompressor
c2 = Connection(lowPressureCompressor, "out1",
                highPressureCompressor, "in1", label="2")

# 3: highPressureCompressor->combustionChamber
c3 = Connection(highPressureCompressor, "out1",
                combustionChamber, "in1", label="3")

# 4: combustionChamber->highPressureTurbine
c4 = Connection(combustionChamber, "out1",
                highPressureTurbine, "in1", label="4")

# 5: fuel->combustionChamber
c5 = Connection(fuel, "out1", combustionChamber, "in2", label="5")

# 6: highPressureTurbine->lowPressureTurbine
c6 = Connection(highPressureTurbine, "out1",
                lowPressureTurbine, "in1", label="6")

# 7: lowPressureTurbine->flueGasSink
c7 = Connection(lowPressureTurbine, "out1", flueGasSink, "in1", label="7")

# e1: highPressureTurbine->highPressureShaft
e1 = PowerConnection(highPressureTurbine, "power",
                     highPressureShaft, "power_in1", label="e1")

# e2: highPressureShaft->highPressureCompressor
e2 = PowerConnection(highPressureShaft, "power_out1",
                     highPressureCompressor, "power", label="e2")

# e3: lowPressureTurbine->lowPressureShaft
e3 = PowerConnection(lowPressureTurbine, "power",
                     lowPressureShaft, "power_in1", label="e3")

# e4: lowPressureShaft->lowPressureCompressor
e4 = PowerConnection(lowPressureShaft, "power_out1",
                     lowPressureCompressor, "power", label="e4")

network.add_conns(c1, c2, c3, c4, c5, c6, c7, e1, e2, e3, e4)


# Parametrização
c1.set_attr(
    p=1, T=20,
    fluid={"Ar": 0.0129, "N2": 0.7553, "CO2": 0.0004, "O2": 0.2314}
)
c5.set_attr(fluid={"CO2": 0.04, "CH4": 0.96, "H2": 0})

network.solve("design")
