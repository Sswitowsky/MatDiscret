import itertools

frutas = ["Manzana", "Pera", "Uva", "Mango"]

# combinations(lista, tamaño_del_grupo)
combinaciones = list(itertools.combinations(frutas, 2))

print(f"Total de combinaciones: {len(combinaciones)}")
for c in combinaciones:
    print(c)