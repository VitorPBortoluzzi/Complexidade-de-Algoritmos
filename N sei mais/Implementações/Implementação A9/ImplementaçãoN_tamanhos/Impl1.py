# - Implementar um algoritmo para multiplicar dois vetores (litas) do mesmo tamanho
import random
import time
import matplotlib.pyplot as plt

def mult_listas(tamanho):
    lista_1 = []
    lista_2 = []

    for i in range(tamanho):
        lista_1.append(random.randint(1, tamanho))
        lista_2.append(random.randint(1, tamanho))

    resultado = []
    for i in range(len(lista_1)):
        resultado.append(lista_1[i] * lista_2[i])
    return resultado

def teste(tamanhos):
    for tamanho in tamanhos:
        temp = []  # Tempo execuções
        for _ in range(nr_teste):
            ini = time.time_ns()
            mult_listas(tamanho)
            fim = time.time_ns()
            temp.append(fim - ini)

        plt.plot(range(nr_teste), temp, label=f'Size {tamanho}')

    plt.title('Tempo de execução')
    plt.xlabel('Número de Testes')
    plt.ylabel('Tempo (ns)')
    plt.legend()
    plt.show()

tamanhos = [5, 10, 50, 100, 500, 1000, 1500]
nr_teste = int(input("Digite o número de testes por tamanho: "))
teste(tamanhos)