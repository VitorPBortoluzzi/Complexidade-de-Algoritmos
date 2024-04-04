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
    #}
        

    ax,fig=plt.subplots()           #1Atrib
    plt.title('Templo de exec')     #1Atrib
    plt.xlabel('Tamanho lista')     #1Atrib
    plt.ylabel('Tempos:')           #1atrib
    plt.plot(x,z,label='sort')      #1Atrib
    plt.legend()                    
    plt.show()                      

# 7 + (n*7)
# 0,00000001 p/instrução
# 7+(500*7) = 7 + 3500 = 3.507
# 3.507*0,0000000,1 = 0,00003507
teste(500)