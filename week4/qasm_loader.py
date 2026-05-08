import sys
import os
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plot
import qiskit.qasm2

def main():
    if len(sys.argv) < 2:
        print("Usage: python qasm_loader.py <filename.qasm>")
        return

    qasm_file = sys.argv[1]

    if not os.path.exists(qasm_file):
        print(f"Error: File '{qasm_file}' not found.")
        return

    try:
        print(f"Loading file: {qasm_file}")
        qc = qiskit.qasm2.load(qasm_file)
        print(qc)

        simulator = AerSimulator()
        job = simulator.run(qc, shots=1024)
        result = job.result()
        counts = result.get_counts(qc)

        plot_histogram(counts)
        plot.show()

    except Exception as e:
        print(f"An error occurred while processing the QASM file: {e}")

if __name__ == "__main__":
    main()
