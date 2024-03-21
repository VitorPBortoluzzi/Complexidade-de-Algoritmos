# - Implementar um algoritmo para multiplicar dois vetores (litas) do mesmo tamanho
import random
import time
import matplotlib.pyplot as plt

def mult_listas():
    lista_1 = []
    lista_2 = []

    for i in range(tamanho):
        lista_1.append(random.randint(1,tamanho))
        lista_2.append(random.randint(1,tamanho))

    resultado = []
    for i in range (len(lista_1)):
        resultado.append(lista_1[i] * lista_2[i])
    return resultado

tamanho = int(input("Digite o tamanho das Listas: "))

def teste(nr_teste):
    x=(range(nr_teste))
    temp = [] #Tempo execuções
    for i in x:
        ini = time.time_ns()
        mult_listas()
        fim = time.time_ns()
        temp.append(fim-ini)

    ax,fig=plt.subplots()
    plt.title('Templo de exec')
    plt.xlabel('Numero Testes')
    plt.ylabel('Tempos:')
    plt.plot(x,temp,label='List')
    plt.legend()
    plt.show()

x_testes = int(input("Digite o numero de testes: "))
teste(x_testes)