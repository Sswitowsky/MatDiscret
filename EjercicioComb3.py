import itertools

personas = ['A', 'B', 'C', 'D', 'E']
equipos = list(itertools.combinations(personas, 3))

print("Posibles equipos de 3 personas:")
print(equipos)