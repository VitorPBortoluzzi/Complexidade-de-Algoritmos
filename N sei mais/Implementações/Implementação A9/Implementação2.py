# - Implementar um algoritmo que multiplique um vetor (lista) com uma matriz quadrada adequada

import random
import time
import matplotlib.pyplot as plt

def lista_matriz(tamanho):
    lista = []
    for i in range(tamanho):
        lista.append(random.randint(1,tamanho))

    matriz = []
    for i in range(tamanho):
        matriz_x = []
        for i in range(tamanho):
            matriz_x.append(random.randint(1,tamanho))
        matriz.append(matriz_x)
    
    resultado = []
    for linha in matriz:
        l_resultado = 0
        for i in range(len(lista)):
            l_resultado += lista[i] * linha[i]
        resultado.append(l_resultado)
    return resultado

tamanho = int(input("Digite o tamanho das Listas: "))

def teste(nr_teste):
    x=(range(nr_teste))
    temp = [] #Tempo execuções
    for i in x:
        ini = time.time_ns()
        lista_matriz(tamanho)
        fim = time.time_ns()
        temp.append(fim-ini)

    ax,fig=plt.subplots()
    plt.title('Tempo de exec')
    plt.xlabel('Numero Testes')
    plt.ylabel('Tempos:')
    plt.plot(x,temp,label='List')
    plt.legend()
    plt.show()

x_testes = int(input("Digite o numero de testes: "))
teste(x_testes)