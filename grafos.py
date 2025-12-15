def calcular_grados(grafo_str):
    grados = {}

    partes = grafo_str.split(';')


    for parte in partes:
        vertice = parte.split(':')[0]
        grados[vertice] = 0

    # contar entradas y salidas
    for parte in partes:
        origen, destinos = parte.split(':')
        for d in destinos:
            grados[origen] += 1 
            grados[d] += 1       
    return grados


def main():
    t = int(input().strip())

    for _ in range(t):
        grafo = input().strip()
        grados = calcular_grados(grafo)

        salida = []
        for v in sorted(grados):
            salida.append(f"{v}={grados[v]}")

        print(", ".join(salida))


main()
