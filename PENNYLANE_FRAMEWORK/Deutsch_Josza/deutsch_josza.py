import pennylane as qml
from pennylane import numpy as np

n = 2  # Número de qubits en el string de entrada

dev = qml.device('default.qubit', wires=n+1)

# Definimos el oráculo, en este caso, para una función balanceada
oracle =  1/2*np.array([[1, 1, 1, 1],
                        [1, -1, 1, -1],
                        [1, 1, -1, -1],
                        [1, -1, -1, 1]])

@qml.qnode(dev)
def deutsch_jozsa(oracle):

    # Aplicamos la compuerta de Hadamard a todos los qubits
    for i in range(n+1):
        qml.Hadamard(wires=i)

    # Aplicamos el oráculo
    qml.QubitUnitary(oracle, wires=[1, 0])

    # Aplicamos la compuerta de Hadamard a todos los qubits
    for i in range(n+1):
        qml.Hadamard(wires=i)

    # Medimos el primer n qubits en la base computacional
    return qml.probs(wires=range(n))

probs = deutsch_jozsa(oracle)

print("Probabilidades de los estados computacionales:", probs)