import networkx as nx

INPUT_FILENAME = "input.txt"
OUTPUT_FILENAME = "output.txt"


with open(INPUT_FILENAME) as input, open(OUTPUT_FILENAME) as output:
    header = input.readline().split()

    cant_prendas = int(header[0])
    cant_incompatibilidades = int(header[1])

    compatibilidades = nx.Graph()
    incompatibilidades = {}
    incompatibilidades_graph = nx.Graph()

    prendas = {}
    incompatibilidades_list = []

    for _ in range(cant_incompatibilidades):
        incompatibilidad = input.readline().split()
        incompatibilidades_list.append(incompatibilidad)

    for _ in range(cant_prendas):
        prenda, peso_prenda = input.readline().split()
        prendas[int(prenda)] = int(peso_prenda)

    pesos_por_lavado = {}

    for _ in range(cant_prendas):
        prenda, lavado = output.readline().split()
        prenda = int(prenda)
        lavado = int(lavado)
        peso_actual = pesos_por_lavado.get(lavado, 0)
        pesos_por_lavado[lavado] = max(peso_actual, prendas[prenda])
    print(pesos_por_lavado)
    peso_total = 0
    for lavado, peso in pesos_por_lavado.items():
        peso_total += peso
    print(peso_total)