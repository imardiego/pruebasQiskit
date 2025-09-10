#!/usr/bin/env python3
"""
Ejemplo simple para entender qc3.measure(qr, cr)
"""

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit import execute, Aer

# Crear registros
qr = QuantumRegister(2, name='q')
cr = ClassicalRegister(2, name='c')

# === CIRCUITO SIN MEDICIÓN ===
qc_sin_medicion = QuantumCircuit(qr, cr, name='sin_medicion')
qc_sin_medicion.h(0)  # Qubit 0 en superposición
qc_sin_medicion.x(1)  # Qubit 1 = |1⟩

print("=== CIRCUITO SIN MEDICIÓN ===")
print(qc_sin_medicion.draw())
print("Este circuito NO produce resultados clásicos")

# === CIRCUITO CON MEDICIÓN ===
qc_con_medicion = QuantumCircuit(qr, cr, name='con_medicion')
qc_con_medicion.h(0)  # Qubit 0 en superposición  
qc_con_medicion.x(1)  # Qubit 1 = |1⟩
qc_con_medicion.measure(qr, cr)  # ¡AQUÍ ESTÁ LA CLAVE!

print("\n=== CIRCUITO CON MEDICIÓN ===")
print(qc_con_medicion.draw())

# Ejecutar solo el circuito CON medición
simulator = Aer.get_backend('qasm_simulator')
job = execute(qc_con_medicion, simulator, shots=100)
result = job.result()
counts = result.get_counts(qc_con_medicion)

print("\n=== RESULTADOS ===")
print("Conteos:", counts)
print("\nInterpretación:")
for state, count in counts.items():
    q0 = state[1]  # Bit derecho = qubit 0
    q1 = state[0]  # Bit izquierdo = qubit 1
    print(f"Estado '{state}': qubit[0]={q0}, qubit[1]={q1} → {count} veces")

print("\n=== ¿QUÉ HIZO measure(qr, cr)? ===")
print("1. Midió el qubit 0 (que estaba en superposición)")
print("2. Obtuvo 0 o 1 con 50% de probabilidad cada uno")
print("3. Guardó el resultado en el bit clásico c[0]")
print("4. Midió el qubit 1 (que siempre es |1⟩)")
print("5. Obtuvo 1 (100% probabilidad)")
print("6. Guardó el resultado en el bit clásico c[1]")
print("7. Ahora tenemos resultados clásicos que podemos leer")