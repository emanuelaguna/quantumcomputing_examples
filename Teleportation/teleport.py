import cirq

# Función para crear el circuito de teleportación cuántica
def create_teleportation_circuit(q0, q1, q2):
    circuit = cirq.Circuit()

    # Crear un par de qubits entrelazados (q1 y q2)
    circuit += cirq.H(q1)
    circuit += cirq.CNOT(q1, q2)

    # Aplicar compuertas CNOT y Hadamard en q0 (qubit que queremos teleportar)
    circuit += cirq.CNOT(q0, q1)
    circuit += cirq.H(q0)

    # Realizar mediciones en q0 y q1
    circuit += cirq.measure(q0, q1)

    # Aplicar compuertas condicionales en q2
    circuit += cirq.CNOT(q1, q2).controlled_by(q0)
    circuit += cirq.CZ(q0, q2).controlled_by(q1)

    return circuit

# Preparar el estado inicial del qubit que queremos teleportar
def prepare_initial_state(qubit):
    circuit = cirq.Circuit()
    circuit += cirq.X(qubit)**0.5
    return circuit

# Crear los qubits
q0, q1, q2 = cirq.LineQubit.range(3)

# Preparar el estado inicial de q0
init_circuit = prepare_initial_state(q0)
print("Circuito de preparación del estado inicial:")
print(init_circuit)

# Crear el circuito de teleportación cuántica
teleportation_circuit = create_teleportation_circuit(q0, q1, q2)
print("\nCircuito de teleportación cuántica:")
print(teleportation_circuit)

# Combinar los circuitos y ejecutar en un simulador
full_circuit = init_circuit + teleportation_circuit
print("\nCircuito completo:")
print(full_circuit)

simulator = cirq.Simulator()
# Agregar una medida en el qubit teleportado (q2) al final del circuito
full_circuit_with_measurement = full_circuit + cirq.measure(q2, key='q2')

# Realizar la simulación
result = simulator.simulate(full_circuit_with_measurement)

print("\nResultado de la medida del qubit teleportado (q2):")
print(result)