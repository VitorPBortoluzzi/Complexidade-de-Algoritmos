import time
import matplotlib.pyplot as plt

def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def shellSort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

def cocktail_sort(arr):
    n = len(arr)
    swapped = True
    start = 0
    end = n - 1

    while swapped:
        swapped = False
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        if not swapped:
            break
        swapped = False
        end -= 1
        for i in range(end - 1, start - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        start += 1

def medir_tempo(algoritmo, N):
    arr = list(range(N, 0, -1))

    inicio = time.time()
    algoritmo(arr)
    fim = time.time()
    
    return fim - inicio

N_values = list(range(1, 10001))
tempos_bubble = [medir_tempo(bubbleSort, N) for N in N_values]
tempos_shell = [medir_tempo(shellSort, N) for N in N_values]
tempos_cocktail = [medir_tempo(cocktail_sort, N) for N in N_values]

# Plotar o gráfico
plt.plot(N_values, tempos_bubble, label='Bubble Sort')
plt.plot(N_values, tempos_shell, label='Shell Sort')
plt.plot(N_values, tempos_cocktail, label='Cocktail Sort')
plt.xlabel('Tamanho do Array (N)')
plt.ylabel('Tempo de Execução (ns)')
plt.title('Tempo de Execução dos algoritmos;')
plt.legend()
plt.grid(True)
plt.show()
