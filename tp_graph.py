import sys
import networkx as nx
from networkx.algorithms.approximation import maximum_independent_set

INPUT_FILENAME = "input.txt"
OUTPUT_FILENAME = "output.txt"

sys.stdout = open(OUTPUT_FILENAME, 'w')



with open(INPUT_FILENAME) as input:
    header = input.readline().split()

    cant_prendas = int(header[0])
    cant_incompatibilidades = int(header[1])

    compatibilidades = nx.Graph()
    incompatibilidades = {}
    incompatibilidades_graph = nx.Graph()

    prendas = {}

    prendas_posibles = list(range(1, cant_prendas))
    for prenda in prendas_posibles:
        compatibilidades.add_node(prenda)
        incompatibilidades_graph.add_node(prenda)


    for _ in range(cant_incompatibilidades):
        prenda, prenda_incompatible = input.readline().split()

        prenda = int(prenda)
        prenda_incompatible = int(prenda_incompatible)

        incompatibilidad_para_esta_prenda = incompatibilidades.get(prenda, set())
        incompatibilidad_para_esta_prenda.add(prenda_incompatible)
        incompatibilidades[prenda] = incompatibilidad_para_esta_prenda

        incompatibilidad_para_esta_otra_prenda = incompatibilidades.get(prenda_incompatible, set())
        incompatibilidad_para_esta_otra_prenda.add(prenda)
        incompatibilidades[prenda_incompatible] = incompatibilidad_para_esta_otra_prenda

        incompatibilidades_graph.add_edge(prenda, prenda_incompatible)

    for _ in range(cant_prendas):
        prenda, peso_prenda  = input.readline().split()
        prendas[prenda] = int(peso_prenda)

    for prenda, prendas_incompatibles in incompatibilidades.items():
        for otra_prenda in prendas_posibles:
            if otra_prenda not in prendas_incompatibles and otra_prenda != prenda:
                compatibilidades.add_edge(prenda, otra_prenda)

    lavado = 1
    while incompatibilidades_graph.size() != 0:
        prendas_a_lavar = maximum_independent_set(incompatibilidades_graph)
        incompatibilidades_graph.remove_nodes_from(prendas_a_lavar)
        for prenda in prendas_a_lavar:
            print(f'{prenda},{lavado}')
        lavado += 1
    prenda_suelta = incompatibilidades_graph.nodes()
    if len(prenda_suelta) != 0:
        for node in prenda_suelta:
            print(f'{node},{lavado}')
            lavado += 1

sys.stdout.close()
