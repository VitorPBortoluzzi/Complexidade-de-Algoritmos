"""
Construir um algoritmo que receba como parâmetro um texto e retorne o numero de ocorrências de cada caractere (ordenado pelos caracteres).
Construir um contador de tempo de execução antes e depois da função que contabiliza as ocorrências.
O texto teste encontra-se anexado a tarefa.
"""
import time
inicio_tempo = time.time()
def contar_caracters(texto):
    ocorrencia_caracter = {}
    for c in texto:
        if c in ocorrencia_caracter:
            ocorrencia_caracter[c] += 1
        else:
            ocorrencia_caracter[c] = 1
    return ocorrencia_caracter 

texto = input("Digite o texto")
resultado_ocorrencias = contar_caracters(texto)
print("\nOcorrências de cada caractere:")
for c, ocorrencia_caracter in resultado_ocorrencias.items():
    print(f"'{c}': {ocorrencia_caracter}")
final_tempo = time.time()
tempo_exec = final_tempo - inicio_tempo
print(tempo_exec)