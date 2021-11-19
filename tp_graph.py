import sys
import networkx as nx
from networkx import max_weight_clique
from networkx.algorithms.approximation import maximum_independent_set

INPUT_FILENAME = "input.txt"
OUTPUT_FILENAME = "output.txt"

sys.stdout = open(OUTPUT_FILENAME, 'w')

def calcular_peso(cant_compatibilidades, cant_prendas, peso_prenda):
    return peso_prenda * (cant_prendas / cant_compatibilidades) * 100

with open(INPUT_FILENAME) as input:
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

    prendas_posibles = list(range(1, cant_prendas + 1))

    for prenda in prendas_posibles:
        compatibilidades.add_node(prenda, weight=prendas[prenda])
        incompatibilidades_graph.add_node(prenda)

    for incompatibilidad in incompatibilidades_list:

        prenda = int(incompatibilidad[0])
        prenda_incompatible = int(incompatibilidad[1])

        incompatibilidad_para_esta_prenda = incompatibilidades.get(prenda, set())
        incompatibilidad_para_esta_prenda.add(prenda_incompatible)
        incompatibilidades[prenda] = incompatibilidad_para_esta_prenda

        incompatibilidad_para_esta_otra_prenda = incompatibilidades.get(prenda_incompatible, set())
        incompatibilidad_para_esta_otra_prenda.add(prenda)
        incompatibilidades[prenda_incompatible] = incompatibilidad_para_esta_otra_prenda

        incompatibilidades_graph.add_edge(prenda, prenda_incompatible)


    for prenda, prendas_incompatibles in incompatibilidades.items():
        for otra_prenda in prendas_posibles:
            if otra_prenda not in prendas_incompatibles and otra_prenda != prenda:
                compatibilidades.add_edge(prenda, otra_prenda)

    weights = nx.get_node_attributes(compatibilidades, 'weight')

    for prenda, incompatibilidades in incompatibilidades.items():
        cant_incompatibilidades_de_prenda = len(incompatibilidades)
        cant_compatibilidades = cant_prendas - cant_incompatibilidades_de_prenda
        peso_prenda = prendas[prenda]
        weight = calcular_peso(cant_compatibilidades, cant_prendas, peso_prenda)
        nx.set_node_attributes(compatibilidades, {prenda: {'weight': int(weight)}})


    lavado = 1
    prendas_lavadas = []
    while compatibilidades.size() != 0:
        prendas_a_lavar = max_weight_clique(compatibilidades, weight='weight')[0]
        compatibilidades.remove_nodes_from(prendas_a_lavar)
        prendas_lavadas += prendas_a_lavar
        # for prenda, prendas_incompatibles in incompatibilidades.items():
        #     for otra_prenda in prendas_posibles:
        #         if otra_prenda not in prendas_incompatibles and otra_prenda != prenda and prenda not in prendas_lavadas and otra_prenda not in prendas_lavadas:
        #             peso_prenda = prendas[prenda]
        #             # capaz en algun momento me convenga guardar el peso de las aristas
        #             peso_otra_prenda = prendas[otra_prenda]
        #             peso_max = max(peso_prenda, peso_otra_prenda)
        #
        #             weights = nx.get_node_attributes(compatibilidades, 'weight')
        #
        #             if weights[prenda] < peso_max:
        #                 nx.set_node_attributes(compatibilidades,
        #                                        {prenda: {'weight': max(peso_max - peso_prenda, peso_prenda)}})
        #
        #             if weights[otra_prenda] < peso_max:
        #                 nx.set_node_attributes(compatibilidades, {
        #                     otra_prenda: {'weight': min(peso_max - peso_otra_prenda, peso_otra_prenda)}})
        #
        #             compatibilidades.add_edge(prenda, otra_prenda, weight=peso_max)
        for prenda in prendas_a_lavar:
            print(f'{prenda} {lavado}')
        lavado += 1
        if len(prendas_a_lavar) == 0:
            break

    prenda_suelta = compatibilidades.nodes()
    if len(prenda_suelta) != 0:
        for node in prenda_suelta:
            print(f'{node} {lavado}')
            lavado += 1

sys.stdout.close()