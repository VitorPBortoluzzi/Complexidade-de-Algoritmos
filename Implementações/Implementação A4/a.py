lista = [10,8,3,15,4]

def ordena(listagem):
    i = 0
    tamanho = len(listagem)
    while i<(tamanho-1):
        if listagem[i]>listagem[i+1]:
            listagem[i],listagem[i+1] = listagem[i+1],listagem[i]
        i+=1
    return listagem
print(lista)
ordena(lista)
print(lista)

# 1 var --> 16bits
# 1 instrução --> 16bits