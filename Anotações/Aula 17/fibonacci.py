p1=0
p2=1
import time
def fibonacci(q):
    global p1,p2
    if q>0:
        n = p1+p2
        print(n)
        p1 = p2
        p2 = n
        fibonacci(q-1)
    else:
        return
    return 0

quantidade = int(input("Digite a quantidade de valores da série: "))
inicio_tempo = time.time_ns()
print(p1)
print(p2)
fibonacci(quantidade - 2)
final_tempo = time.time_ns()
tempo_exec = final_tempo - inicio_tempo
print(tempo_exec)