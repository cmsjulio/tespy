from tespy.networks import Network
from tespy.components import (
    DiabaticCombustionChamber, Turbine, Source, Sink, Compressor,
    Generator, PowerBus, PowerSink
)
from tespy.connections import Connection, Ref, PowerConnection

# define full fluid list for the network's variable space
network = Network()
network.units.set_defaults(temperature="degC", pressure="bar", heat="MW", power="MW")

compressor = Compressor("Compressor")
combustionChamber = DiabaticCombustionChamber("combustion chamber")
turbine = Turbine("turbine")
air = Source("air source")
fuelSource = Source("fuel source")
flueGasSink = Sink("flue gas sink")

# connecting with ambient/air source instead of using compression

c2 = Connection(air, "out1", combustionChamber, "in1", label="2")
c3 = Connection(combustionChamber, "out1", flueGasSink, "in1", label="3")
c5 = Connection(fuelSource, "out1", combustionChamber, "in2", label="5")
network.add_conns(c2, c3, c5)

##########
# PARAMETRIZAÇÕES DO EXEMPLO
# eta: eficiência do componente, eta=1: sem perdas, processo adiabático
# pr: razão entre pressão de saída na câmara de combustão e pressão na entrada de ar
# pr=1: sem perda de pressão
# ti: thermal input
# lamb: air to stoichiometric air ratio, relação ar/combustível lambda
combustionChamber.set_attr(pr=1, eta=1, lamb=1.5, ti=10)

# composição do ar na conexão 2: entrada de ar na câmara de combustão
c2.set_attr(
    p=1, T=20,
    fluid={"Ar": 0.0129, "N2": 0.7553, "CO2": 0.0004, "O2": 0.2314}
)

# composição do combustível
c5.set_attr(p=1, T=20, fluid={"CO2": 0.04, "CH4": 0.96, "H2": 0})

# 
##########

network.solve(mode="design")
network.print_results()

# para imprimir conexões com composição de fluidos
print("##### CONEXÕES E FLUIDOS")
print(network.results["Connection"])

