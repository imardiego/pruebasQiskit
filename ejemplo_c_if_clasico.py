#!/usr/bin/env python3
"""
Ejemplo de medición condicional con sintaxis clásica
"""

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit import execute, Aer

# Crear registros
qr = QuantumRegister(3, name='q')
cr = ClassicalRegister(3, name='c')

# === MÉTODO CLÁSICO ===
qc6_clasico = QuantumCircuit(qr, cr, name='quantum_circuit6_clasico')
qc6_clasico.h(0)
qc6_clasico.x(1)
qc6_clasico.cx(1, 2)
qc6_clasico.measure(qr[0:2], cr[0:2])

# Sintaxis clásica - diferentes formas de intentar
try:
    # Opción 1: Tu sintaxis original
    qc6_clasico.x(2).c_if(cr[0], 1)
    print("✓ Sintaxis original funcionó")
except Exception as e:
    print(f"✗ Sintaxis original falló: {e}")
    
    try:
        # Opción 2: Especificar el registro completo
        qc6_clasico.x(2).c_if(cr, 1)  # Compara todo el registro cr con 1
        print("✓ Sintaxis con registro completo funcionó")
    except Exception as e2:
        print(f"✗ Sintaxis con registro completo falló: {e2}")
        
        try:
            # Opción 3: Crear la operación por separado
            x_gate = qc6_clasico.x(2)
            x_gate.c_if(cr[0], 1)
            print("✓ Sintaxis separada funcionó")
        except Exception as e3:
            print(f"✗ Sintaxis separada falló: {e3}")

print("\n=== CIRCUITO RESULTANTE ===")
print(qc6_clasico.draw())

# Intentar ejecutar
try:
    simulator = Aer.get_backend('qasm_simulator')
    job = execute(qc6_clasico, simulator, shots=100)
    result = job.result()
    counts = result.get_counts(qc6_clasico)
    print("\n=== RESULTADOS ===")
    print("Conteos:", counts)
except Exception as e:
    print(f"Error al ejecutar: {e}")

print("\n=== EXPLICACIÓN DE c_if ===")
print("qc6.x(2).c_if(cr[0], 1) significa:")
print("- Aplica puerta X al qubit 2")
print("- SOLO si el bit clásico cr[0] tiene valor 1")
print("- Es una operación condicional basada en medición previa")
print("- Permite crear circuitos que 'reaccionan' a resultados de medición")