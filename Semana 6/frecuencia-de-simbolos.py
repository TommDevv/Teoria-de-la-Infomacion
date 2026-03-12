import math
import heapq


class Nodo:
    # Nodo del árbol de Huffman
    def __init__(self, probabilidad, simbolo=None, izquierda=None, derecha=None):
        self.probabilidad = probabilidad
        self.simbolo = simbolo
        self.izquierda = izquierda
        self.derecha = derecha

    def __lt__(self, other):
        return self.probabilidad < other.probabilidad


def validar_probabilidades(simbolos_probabilidades):
    # Verifica probabilidades válidas y suma unitaria
    if not simbolos_probabilidades:
        raise ValueError("No se ingresaron símbolos.")

    suma = 0.0
    for simbolo, probabilidad in simbolos_probabilidades:
        if probabilidad <= 0:
            raise ValueError(f"La probabilidad de '{simbolo}' debe ser mayor que 0.")
        suma += probabilidad

    if not math.isclose(suma, 1.0, rel_tol=1e-9, abs_tol=1e-9):
        raise ValueError(
            f"La suma de probabilidades debe ser 1. Valor actual: {suma:.10f}"
        )


def construir_arbol_huffman(simbolos_probabilidades):
    # Construye el árbol combinando los nodos menos probables
    heap = [Nodo(probabilidad, simbolo=simbolo) for simbolo, probabilidad in simbolos_probabilidades]
    heapq.heapify(heap)

    if len(heap) == 1:
        unico = heapq.heappop(heap)
        return Nodo(unico.probabilidad, izquierda=unico)

    while len(heap) > 1:
        izquierdo = heapq.heappop(heap)
        derecho = heapq.heappop(heap)

        combinado = Nodo(
            izquierdo.probabilidad + derecho.probabilidad,
            izquierda=izquierdo,
            derecha=derecho
        )
        heapq.heappush(heap, combinado)

    return heap[0]


def generar_codigos(nodo, prefijo="", codigos=None):
    # Recorre el árbol y asigna palabras código
    if codigos is None:
        codigos = {}

    if nodo is None:
        return codigos

    if nodo.simbolo is not None:
        codigos[nodo.simbolo] = prefijo if prefijo else "0"
        return codigos

    generar_codigos(nodo.izquierda, prefijo + "0", codigos)
    generar_codigos(nodo.derecha, prefijo + "1", codigos)
    return codigos


def calcular_entropia(simbolos_probabilidades):
    # Calcula H = sum p(x) log2(1/p(x))
    return sum(p * math.log2(1 / p) for _, p in simbolos_probabilidades)


def calcular_longitud_promedio(simbolos_probabilidades, codigos):
    # Calcula L = sum p(x) * l(x)
    return sum(probabilidad * len(codigos[simbolo]) for simbolo, probabilidad in simbolos_probabilidades)


def calcular_eficiencia(entropia, longitud_promedio):
    # Calcula eta = H / L
    if longitud_promedio == 0:
        return 0.0
    return entropia / longitud_promedio


def calcular_redundancia(eficiencia):
    # Calcula 1 - eta
    return 1 - eficiencia


def leer_datos_desde_consola():
    # Lee símbolos y probabilidades desde terminal
    simbolos_probabilidades = []

    n = int(input("Ingrese la cantidad de símbolos: ").strip())

    if n <= 0:
        raise ValueError("La cantidad de símbolos debe ser mayor que 0.")

    print("\nIngrese cada símbolo con su probabilidad.")
    print("Ejemplo: A 0.25\n")

    simbolos_vistos = set()

    for i in range(n):
        entrada = input(f"Símbolo #{i + 1}: ").strip().split()

        if len(entrada) != 2:
            raise ValueError("Cada línea debe tener exactamente: simbolo probabilidad")

        simbolo, probabilidad_texto = entrada
        probabilidad = float(probabilidad_texto)

        if simbolo in simbolos_vistos:
            raise ValueError(f"El símbolo '{simbolo}' está repetido.")

        simbolos_vistos.add(simbolo)
        simbolos_probabilidades.append((simbolo, probabilidad))

    return simbolos_probabilidades


def imprimir_resultados(simbolos_probabilidades, codigos, entropia, longitud_promedio, eficiencia, redundancia):
    # Muestra resultados en consola
    print("\n--- Códigos asignados ---")
    for simbolo, probabilidad in sorted(simbolos_probabilidades, key=lambda x: x[1], reverse=True):
        print(
            f"Símbolo: {simbolo:>5} | "
            f"Probabilidad: {probabilidad:.6f} | "
            f"Código: {codigos[simbolo]}"
        )

    print("\n--- Métricas de la codificación ---")
    print(f"Entropía H: {entropia:.6f} bits/símbolo")
    print(f"Longitud promedio L: {longitud_promedio:.6f} bits/símbolo")
    print(f"Eficiencia: {eficiencia:.6f} ({eficiencia * 100:.2f}%)")
    print(f"Redundancia: {redundancia:.6f} ({redundancia * 100:.2f}%)")


def main():
    # Ejecuta el flujo principal
    try:
        simbolos_probabilidades = leer_datos_desde_consola()
        validar_probabilidades(simbolos_probabilidades)

        arbol = construir_arbol_huffman(simbolos_probabilidades)
        codigos = generar_codigos(arbol)

        entropia = calcular_entropia(simbolos_probabilidades)
        longitud_promedio = calcular_longitud_promedio(simbolos_probabilidades, codigos)
        eficiencia = calcular_eficiencia(entropia, longitud_promedio)
        redundancia = calcular_redundancia(eficiencia)

        imprimir_resultados(
            simbolos_probabilidades,
            codigos,
            entropia,
            longitud_promedio,
            eficiencia,
            redundancia
        )

    except ValueError as e:
        print(f"\nError: {e}")
    except Exception as e:
        print(f"\nOcurrió un error inesperado: {e}")


if __name__ == "__main__":
    main()