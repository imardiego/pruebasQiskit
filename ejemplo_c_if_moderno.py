#!/usr/bin/env python3
"""
Ejemplo de medición condicional con sintaxis moderna
"""

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit import execute, Aer

# Crear registros
qr = QuantumRegister(3, name='q')
cr = ClassicalRegister(3, name='c')

# === MÉTODO MODERNO (RECOMENDADO) ===
qc6_moderno = QuantumCircuit(qr, cr, name='quantum_circuit6_moderno')
qc6_moderno.h(0)
qc6_moderno.x(1)
qc6_moderno.cx(1, 2)
qc6_moderno.measure(qr[0:2], cr[0:2])  # Medir qubits 0 y 1

# Sintaxis moderna para operación condicional
qc6_moderno.x(2).c_if(cr[0], 1)  # X en qubit 2 si cr[0] == 1

print("=== CIRCUITO CON MEDICIÓN CONDICIONAL (MODERNO) ===")
print(qc6_moderno.draw())

# === MÉTODO ALTERNATIVO (SI EL ANTERIOR NO FUNCIONA) ===
qc6_alt = QuantumCircuit(qr, cr, name='quantum_circuit6_alternativo')
qc6_alt.h(0)
qc6_alt.x(1)
qc6_alt.cx(1, 2)
qc6_alt.measure(qr[0:2], cr[0:2])

# Método alternativo
with qc6_alt.if_test((cr[0], 1)):  # Si cr[0] == 1
    qc6_alt.x(2)  # Aplica X al qubit 2

print("\n=== CIRCUITO CON MEDICIÓN CONDICIONAL (ALTERNATIVO) ===")
print(qc6_alt.draw())

# Ejecutar el circuito moderno
try:
    simulator = Aer.get_backend('qasm_simulator')
    job = execute(qc6_moderno, simulator, shots=1000)
    result = job.result()
    counts = result.get_counts(qc6_moderno)
    
    print("\n=== RESULTADOS ===")
    print("Conteos:", counts)
    
    print("\n=== ANÁLISIS ===")
    print("Tu circuito hace:")
    print("1. H(0): Qubit 0 en superposición (50% |0⟩, 50% |1⟩)")
    print("2. X(1): Qubit 1 = |1⟩")
    print("3. CNOT(1,2): Qubit 2 = |1⟩ (porque qubit 1 es |1⟩)")
    print("4. Mide qubits 0 y 1 → guarda en cr[0] y cr[1]")
    print("5. SI cr[0] == 1, aplica X al qubit 2")
    print("   - Si cr[0] = 0: qubit 2 permanece |1⟩")
    print("   - Si cr[0] = 1: qubit 2 se convierte en |0⟩")
    
except Exception as e:
    print(f"Error al ejecutar: {e}")
    print("Probablemente necesitas una versión más reciente de Qiskit")