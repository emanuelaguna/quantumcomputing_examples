from qiskit import QuantumCircuit, execute, Aer
from qiskit.visualization import plot_histogram

# Create a Quantum Circuit with 2 qubits (to simulate a qutrit)
circuit = QuantumCircuit(2)

# Initialize the 'qutrit' to the state |1> (00 -> 0, 01 -> 1, 10 -> 2)
circuit.x(1)

# Add your gates here

# Measure the 'qutrit'
circuit.measure_all()

# Run the quantum circuit on a simulator backend
simulator = Aer.get_backend('qasm_simulator')
job = execute(circuit, simulator, shots=1000)

# Grab the results from the job
result = job.result()

# Return counts
counts = result.get_counts(circuit)
print("\nTotal counts are:",counts)

# Draw the circuit
print(circuit.draw())