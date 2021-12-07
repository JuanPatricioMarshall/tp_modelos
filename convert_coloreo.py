import networkx as nx

OUTPUT_FILENAME = "output.txt"


with open(OUTPUT_FILENAME) as output:

    for _ in range(95):
        prenda, lavado = output.readline().split()
        prenda = int(prenda)
        lavado = int(lavado)
        print(f'coloreoValido[{prenda -1}] = {lavado};')