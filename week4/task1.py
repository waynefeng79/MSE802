from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector
from qiskit.quantum_info import DensityMatrix
from qiskit.visualization import plot_state_city
from qiskit.visualization import plot_state_qsphere
import matplotlib.pyplot as plot


qc = QuantumCircuit(2)
qc.h(0)
qc.x(1)
qc.s(0)
print(qc)
state = Statevector(qc)
print(state)
#state.draw("latex")  # psi is a Statevector object
#DensityMatrix(state).draw("latex")  # convert to a DensityMatrix and draw
#state.draw("city")
state.draw("qsphere")
#plot_bloch_multivector(state)
plot.show()
