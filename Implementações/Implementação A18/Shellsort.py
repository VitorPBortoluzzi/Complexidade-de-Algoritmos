#https://www.sortvisualizer.com/bubblesort/

# - Contar as instruções (polinômio de pendente de N)
# - Montar o gráfico de instruções por N = [1,1000]
# - Montar o gráfico de __Tempo__ de execução de N =[1,1000] para os 3 algoritmos.  
import time
import matplotlib.pyplot as plt 

def shellSort(arr):
    n = len(arr)                                        #1
    gap = n//2                                          #1

    while gap > 0:                                      #(N+1)+ 4N²+5 + 1

        for i in range(gap,n):                          # N*[2 + 4N+2 + 1] = 4N²+5
            temp = arr[i]                               # 1
            j = i                                       # 1
            while  j >= gap and arr[j-gap] >temp:       #(N+1)*2+ [N*2]
                arr[j] = arr[j-gap]                     #
                j -= gap                                #
            arr[j] = temp                               #1
        gap //= 2                                       #1

def bubbleSort(arr):
    n = len(arr)                                        #1
    for i in range(n-1):                                #N*[2]
        for j in range(0, n-i-1):                       #N*[2]
            if arr[j] > arr[j+1]:                       #1
                arr[j], arr[j+1] = arr[j+1], arr[j]     #1

#4N+3

def cocktail_sort(arr):
    n = len(arr)                                        #1
    swapped = True                                      #1
    start = 0                                           #1
    end = n - 1                                         #1
    while swapped:                                      #(N+1)+[N*6 + 5]
        swapped = False                                 #1
        # movendo o maior elemento para o final
        for i in range(start, end):                     #N*[3]
            if arr[i] > arr[i + 1]:                     #
                arr[i], arr[i + 1] = arr[i + 1], arr[i] #
                swapped = True                          #
        if not swapped:                                 #1
            break                               
        swapped = False                                 #1
        end -= 1                                        #1
        # movendo o menor elemento para o início
        for i in range(end - 1, start - 1, -1):         #N*[3]
            if arr[i] > arr[i + 1]:                     #
                arr[i], arr[i + 1] = arr[i + 1], arr[i] #
                swapped = True                          #
        start += 1                                      #1

#7N+10