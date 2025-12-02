import math

n = 45 # Total de números
k = 6  # Números a elegir

# math.comb hace el cálculo directo de la fórmula
resultado = math.comb(n, k)

print(f"Probabilidades de ganar: 1 en {resultado}")