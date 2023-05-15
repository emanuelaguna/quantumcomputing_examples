import pennylane as qml
from pennylane import numpy as np

n = 1  # Número de qutrits en el string de entrada
numwires = 3*n
dev = qml.device('default.qubit', wires=numwires)

# Definimos el oráculo para una función constante y otra balanceada
# Oráculo para una función constante
oracle_constant = np.eye(8)

# Oráculo para una función balanceada
oracle_balanced = np.diag([1, -1, 1, -1, 1, -1, 1, -1])


@qml.qnode(dev)
def deutsch_jozsa(oracle):
    # Aplicamos la compuerta de Hadamard a todos los qubits
    for i in range(numwires):
        qml.Hadamard(wires=i)

    # Aplicamos el oráculo
    qml.QubitUnitary(oracle, wires=[2, 1, 0])

    # Aplicamos la compuerta de Hadamard a todos los qubits
    for i in range(numwires):
        qml.Hadamard(wires=i)

    # Medimos el primer n qubits en la base computacional
    return qml.probs(wires=range(numwires))

probs_constant = deutsch_jozsa(oracle_constant)
probs_balanced = deutsch_jozsa(oracle_balanced)

print("Probabilidades de los estados para una funcion constante:\n", probs_constant)
print("Probabilidades de los estados para una funcion balanceada:\n", probs_balanced)
