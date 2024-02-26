#Chta GPT
def bubble_sort(arr):
    n = len(arr)
    trocas = 0
    
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                trocas += 1
                
    return trocas

# Exemplo de uso
lista = [64, 25, 12, 22, 11]
trocas_realizadas = bubble_sort(lista)

print("Lista ordenada:", lista)
print("Número de trocas realizadas:", trocas_realizadas)

lista_inversa = list(range(100, 0, -1))
trocas_na_lista_inversa = bubble_sort(lista_inversa)
print("Lista ordenada inversamente:", lista_inversa)
print("Número de trocas realizadas na lista inversamente ordenada:", trocas_na_lista_inversa)


#Criar função para gerir o Sort
#
#def Ordenar(listaVal):
#   n = len(listaVal):  # Passa tamanho da lista.
#   trocas = 0          # Zera numero de trocas.
#
#   for i in range(n):  # 
#        for j in range(0, n-i-1):
#           if listaVal[j] > listaVal[j+1]
# 
# 
# 
# 
# 
# 
# 
# 
#     
