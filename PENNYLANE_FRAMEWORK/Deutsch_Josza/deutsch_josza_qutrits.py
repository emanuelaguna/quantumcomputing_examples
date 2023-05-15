# This script implements the Deutsch-Jozsa algorithm using the PennyLane framework.
# The Deutsch-Jozsa algorithm solves the Deutsch problem: given a function that is either constant or balanced,
# the task is to determine which type the function is with just one query.
# Here, we simulate this algorithm using qubits to represent qutrits.

import pennylane as qml
from pennylane import numpy as np

n = 1  # Number of qutrits in the input string
numwires = 3*n

# We specify the number of runs 'shots' to ensure that
# the algorithm performs the calculations in a single run and thus
# demonstrate its efficiency compared to the classical case.
dev = qml.device('default.qubit', wires=numwires, shots=1) 

# Define the oracle for a constant function and a balanced function
# Oracle for a constant function
oracle_constant = np.eye(8)

# Oracle for a balanced function
oracle_balanced = np.diag([1, -1, 1, -1, 1, -1, 1, -1])


@qml.qnode(dev)
def deutsch_jozsa(oracle):
    # Apply the Hadamard gate to all qubits
    for i in range(numwires):
        qml.Hadamard(wires=i)

    # Apply the oracle
    qml.QubitUnitary(oracle, wires=[2, 1, 0])

    # Apply the Hadamard gate to all qubits
    for i in range(numwires):
        qml.Hadamard(wires=i)

    # Measure the first n qubits in the computational basis
    return qml.probs(wires=range(numwires))

probs_constant = deutsch_jozsa(oracle_constant)
probs_balanced = deutsch_jozsa(oracle_balanced)

print("Probabilities of the states for a constant function:\n", probs_constant)
print("Probabilities of the states for a balanced function:\n", probs_balanced)
