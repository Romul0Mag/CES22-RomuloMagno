from SimularAutomovel import *

sim = SimularCaminhao()
auto = sim.createAutomovelCombustao()
print(f'o automovel é {type(auto).__name__}')
print(f'o motor é {type(auto.motor).__name__}')
auto.motor.poluir()
sim.acelerar(auto)
sim.acelerar(auto)
sim.acelerar(auto)
sim.freiar(auto)
sim.fazerCurva(auto, 90)
sim.fazerCurva(auto, 272)
sim.fazerCurva(auto, -2)

print('\n')

sim = SimularCaminhao()
auto = sim.createAutomovelHibrido()
print(f'o automovel é {type(auto).__name__}')
print(f'o motor é {type(auto.motor).__name__}')
auto.motor.poluir()
sim.acelerar(auto)
sim.acelerar(auto)
sim.acelerar(auto)
sim.freiar(auto)
sim.fazerCurva(auto, 90)
sim.fazerCurva(auto, 272)
sim.fazerCurva(auto, -2)

print('\n')

sim = SimularCaminhao()
auto = sim.createAutomovelEletrico()
print(f'o automovel é {type(auto).__name__}')
print(f'o motor é {type(auto.motor).__name__}')
auto.motor.poluir()
sim.acelerar(auto)
sim.acelerar(auto)
sim.acelerar(auto)
sim.freiar(auto)
sim.fazerCurva(auto, 90)
sim.fazerCurva(auto, 272)
sim.fazerCurva(auto, -2)

print('\n')

sim = SimularCarro()
auto = sim.createAutomovelEletrico()
print(f'o automovel é {type(auto).__name__}')
print(f'o motor é {type(auto.motor).__name__}')
sim.acelerar(auto)
sim.acelerar(auto)
sim.acelerar(auto)
sim.freiar(auto)
sim.fazerCurva(auto, 90)
sim.fazerCurva(auto, 272)
sim.fazerCurva(auto, -2)

print('\n')

sim = SimularMoto()
auto = sim.createAutomovelEletrico()
print(f'o automovel é {type(auto).__name__}')
print(f'o motor é {type(auto.motor).__name__}')
sim.acelerar(auto)
sim.acelerar(auto)
sim.acelerar(auto)
sim.freiar(auto)
sim.fazerCurva(auto, 90)
sim.fazerCurva(auto, 272)
sim.fazerCurva(auto, -2)