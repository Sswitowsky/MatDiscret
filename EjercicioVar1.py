import itertools

corredores = ["Juan", "Ana", "Luis", "Maria"]

# permutations(lista, tamaño_grupo)
podios = list(itertools.permutations(corredores, 3))

print(f"Formas distintas de armar el podio: {len(podios)}")
for p in podios:
    print(p)