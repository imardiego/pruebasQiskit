#!/usr/bin/env python3
"""
Ejemplo de cómo obtener los valores de qubits medidos en Qiskit
"""

import numpy as np
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit import execute, Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Crear los registros (igual que en tu notebook)
nqr = 3  # número de qubits
ncr = 3  # número de bits clásicos

qr = QuantumRegister(nqr, name='q')  
cr = ClassicalRegister(ncr, name='c')

# Crear el circuito (igual que tu qc3)
qc3 = QuantumCircuit(qr, cr, name='quantum circuit3')
qc3.h(0)        # Hadamard en qubit 0
qc3.x(1)        # X gate en qubit 1  
qc3.cx(1, 2)    # CNOT entre qubit 1 y 2
qc3.measure(qr, cr)  # Medir todos los qubits

print("Circuito creado:")
print(qc3.draw())

# Ejecutar el circuito en el simulador
simulator = Aer.get_backend('qasm_simulator')
job = execute(qc3, simulator, shots=1024)
result = job.result()

# Obtener los conteos
counts = result.get_counts(qc3)

print("\n=== RESULTADOS DE LAS MEDICIONES ===")
print("Conteos brutos:", counts)

print("\n=== INTERPRETACIÓN DETALLADA ===")
for state, count in counts.items():
    percentage = count/1024*100
    # Recordar que el orden está invertido: bit más a la derecha = qubit 0
    q0_value = state[2]  # Último bit = qubit 0
    q1_value = state[1]  # Bit del medio = qubit 1  
    q2_value = state[0]  # Primer bit = qubit 2
    
    print(f"Estado '{state}': {count} veces ({percentage:.1f}%)")
    print(f"  -> qubit[0] = {q0_value}, qubit[1] = {q1_value}, qubit[2] = {q2_value}")

print("\n=== ANÁLISIS DEL CIRCUITO ===")
print("Tu circuito hace:")
print("1. H(0): Pone qubit 0 en superposición (50% |0⟩, 50% |1⟩)")
print("2. X(1): Pone qubit 1 en estado |1⟩")  
print("3. CNOT(1,2): Si qubit 1 = |1⟩, invierte qubit 2")
print("4. Como qubit 1 siempre es |1⟩, qubit 2 siempre será |1⟩")
print("5. Resultado esperado: ~50% '011' y ~50% '111'")

# Crear histograma
try:
    plt.figure(figsize=(10, 6))
    plot_histogram(counts)
    plt.title('Distribución de resultados de medición')
    plt.tight_layout()
    plt.savefig('/home/miguel/pruebasQiskit/histograma_medicion.png', dpi=150, bbox_inches='tight')
    print(f"\nHistograma guardado en: /home/miguel/pruebasQiskit/histograma_medicion.png")
except Exception as e:
    print(f"Error al crear histograma: {e}")

print("\n=== ACCESO A VALORES INDIVIDUALES ===")
print("Para acceder a valores específicos:")
print("- counts['011']: número de veces que se midió el estado 011")
print("- list(counts.keys()): lista de todos los estados medidos")
print("- sum(counts.values()): total de mediciones (debería ser 1024)")

# Ejemplo de cómo acceder a valores específicos
if '011' in counts:
    print(f"El estado '011' se midió {counts['011']} veces")
if '111' in counts:
    print(f"El estado '111' se midió {counts['111']} veces")