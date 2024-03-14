import time
import matplotlib.pyplot as plt
def cria_lista(tamanho):
    lista = []
    for i in range(tamanho):
        lista.append(tamanho-i)
    return lista

def ordena(lista):
    tamanho=len(lista)
    for i in range(tamanho):
        for j in range(tamanho-1):
            if lista[j]>lista[j+1]:
                lista[j],lista[j+1]=lista[j+1],lista[j]
            j+=1
        #print(lista)
        i+=1
        
def teste(nr_Testes):
    x=range(nr_Testes)
    #y=[]#tempos ordena
    z=[]#tempos sort
    for i in x:
        #lst = cria_lista(i)
        lst_copy=cria_lista(i)
        ini = time.time_ns()
        #ordena(lst)
        #fim = time.time_ns()
        #y.append(fim - ini)
        #print(lst)

        inil=time.time_ns()
        l=sorted(lst_copy)
        fiml=time.time_ns()
        z.append(fiml - inil)
        #print(lst_copy)
        

    ax,fig=plt.subplots()
    plt.title('Templo de exec')
    plt.xlabel('Tamanho lista')
    plt.ylabel('Tempos:')
    #plt.plot(x,y,label='ordena')
    plt.plot(x,z,label='sort')
    plt.legend()
    plt.show()
    #print('Tempos exeução: ',y)

teste(500)