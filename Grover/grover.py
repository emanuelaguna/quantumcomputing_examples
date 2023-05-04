
'''
Este código define un oráculo de fase utilizando PhaseOracle('x0 & x1'), 
lo que indica que estás buscando un estado en el que ambos qubits sean 1 
(es decir, |11⟩). Luego, creas un problema de amplificación con este oráculo 
y ejecutas el algoritmo de Grover en una instancia cuántica que utiliza el backend "aer_simulator".

Finalmente, imprimes y visualizas el resultado del algoritmo de Grover,
que en este caso es '11', lo que indica se ha encontrado el estado deseado.
'''

from qiskit import Aer
from qiskit.circuit.library import PhaseOracle
from qiskit.algorithms import Grover
from qiskit.utils import QuantumInstance
from qiskit.algorithms import AmplificationProblem
from qiskit.primitives import Sampler
from qiskit.visualization import plot_histogram

# Definir la función oráculo
oracle = PhaseOracle('x0 & x1')

# Crear el problema de amplificación para el algoritmo de Grover
problem = AmplificationProblem(oracle=oracle)

# Crear una instancia cuántica utilizando el simulador cuántico Aer
backend = Aer.get_backend('aer_simulator')
quantum_instance = QuantumInstance(backend, shots=1024)

# Ejecutar el algoritmo de Grover
grover = Grover(sampler=Sampler()) # Aquí puedes ajustar el número de iteraciones
result = grover.amplify(problem)

# Visualizar los resultados
print("Resultado del algoritmo de Grover:", result.top_measurement)
plot_histogram(result.circuit_results[0])