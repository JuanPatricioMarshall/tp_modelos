import sys

INPUT_FILENAME = "input.txt"
OUTPUT_FILENAME = "output.txt"

sys.stdout = open(OUTPUT_FILENAME, 'w')

with open(INPUT_FILENAME) as input:
    header = input.readline().split()

    cant_prendas = int(header[0])
    cant_incompatibilidades = int(header[1])

    #print(f'{cant_incompatibilidades} + {cant_prendas}')

    incompatibilidades = {}
    prendas = {}

    for _ in range(cant_incompatibilidades):
        prenda, prenda_incompatible  = input.readline().split()

        incompatibilidad_para_esta_prenda = incompatibilidades.get(prenda, [])
        incompatibilidad_para_esta_prenda.append(prenda_incompatible)
        incompatibilidades[prenda] = incompatibilidad_para_esta_prenda

    for _ in range(cant_prendas):
        prenda, peso_prenda  = input.readline().split()
        prendas[prenda] = int(peso_prenda)

    prendas_ordenadas = sorted(prendas, key=prendas.get, reverse=True)

    prendas_usadas = set()
    nro_lavado = 1

    lavado = set()

    for i, prenda in enumerate(prendas_ordenadas):
        if prenda in prendas_usadas:
            continue
        prendas_incompatibles = incompatibilidades.get(prenda, [])
        lavado.add(prenda)
        prendas_usadas.add(prenda)
        for j in range(i+1, len(prendas_ordenadas)):
            posible_prenda = prendas_ordenadas[j]
            if posible_prenda not in prendas_usadas and posible_prenda not in prendas_incompatibles:
                prendas_usadas.add(posible_prenda)
                lavado.add(posible_prenda)
                prendas_incompatibles += incompatibilidades.get(posible_prenda, [])
        for prenda in lavado:
            print(f'{prenda} {nro_lavado}')
        nro_lavado += 1
        lavado = set()


sys.stdout.close()
