import random
import time
import matplotlib.pyplot as plt

def lista_matriz(tamanho):
    lista = []
    for i in range(tamanho):
        lista.append(random.randint(1, tamanho))

    matriz = []
    for i in range(tamanho):
        matriz_x = []
        for i in range(tamanho):
            matriz_x.append(random.randint(1, tamanho))
        matriz.append(matriz_x)
    
    resultado = []
    for linha in matriz:
        l_resultado = 0
        for i in range(len(lista)):
            l_resultado += lista[i] * linha[i]
        resultado.append(l_resultado)
    return resultado

def teste(tamanhos, nr_teste):
    for tamanho in tamanhos:
        temp = [] # Tempo execuções
        for i in range(nr_teste):
            ini = time.time_ns()
            lista_matriz(tamanho)
            fim = time.time_ns()
            temp.append(fim - ini)

        plt.plot(range(nr_teste), temp, label=f'Size {tamanho}')

    plt.title('Tempo de execução')
    plt.xlabel('Número de Testes')
    plt.ylabel('Tempo (ns)')
    plt.legend()
    plt.show()

tamanhos = [5, 10, 50, 100, 500, 1000, 1500]
x_testes = int(input("Digite o numero de testes por tamanho: "))
teste(tamanhos, x_testes)
