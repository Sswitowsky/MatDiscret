import math

n = 9 # Números disponibles (1-9)
k = 4 # Longitud de la clave

# math.perm hace el cálculo de variación
resultado = math.perm(n, k)

print(f"Total de contraseñas posibles: {resultado}")