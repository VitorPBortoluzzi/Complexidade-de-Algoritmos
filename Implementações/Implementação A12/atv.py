#identifique por linhas o numero de instruções.

import time
import matplotlib.pyplot as plt 

# [
def cria_lista(tamanho):
    lista = []                      #1Atrib
    #{ n * 4
    for i in range(tamanho):        #2Atrib
        lista.append(tamanho-i)     #2I
    #}
    return lista                    #1Atrib
#] #1Atribuição Apenas Quando chamado
        
def teste(nr_Testes):
    global nrAtrib,x
    nrAtrib = []                    #1Atrib
    x=range(nr_Testes)              #1Atrib
    z=[]#tempos sort                #1Atrib
    #{Laço (n * 7)
    for i in x:                     #1Atrib
        lst_copy=cria_lista(i)      #1Atrib 
        ini = time.time_ns()        #1Atrib
        inil=time.time_ns()         #1Atrib
        l=sorted(lst_copy)          #1Atrib
        fiml=time.time_ns()         #1Atrib
        z.append(fiml - inil)       #1Atrib
        if i > 0:                   #1Comp
            nrAtrib.append(nrAtrib[i-1] + 10)    #1Atrib
        else:
            nrAtrib.append(24)      
    #}    

    ax,fig=plt.subplots()           #1Atrib
    plt.title('Templo de exec')     #1Atrib
    plt.xlabel('Tamanho lista')     #1Atrib
    plt.ylabel('Tempos:')           #1atrib
    plt.plot(x,z,label='sort')      #1Atrib

    ax,fig = plt.subplots()                                     #1Atrib
    plt.title('Número de atribuições vs. Número de testes')     #1Atrib
    plt.xlabel('Número de testes')                              #1Atrib
    plt.ylabel('Número de atribuições')                         #1Atrib
    plt.plot(x, nrAtrib, label='atribuições')                   #1Atrib
    plt.legend()                    
    plt.show()              

teste(500)
print(nrAtrib)
print(x)

#Gráfico:
#Gráfico de instruções
#mirkos@ufn.edu.br