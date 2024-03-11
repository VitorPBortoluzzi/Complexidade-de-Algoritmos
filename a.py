import time

def contar_ocorrencias(texto):
    ocorrencias = {}
    for char in texto:
        if char in ocorrencias:
            ocorrencias[char] += 1
        else:
            ocorrencias[char] = 1

    return ocorrencias

if __name__ == "__main__":
    texto = input("Digite um texto: ")

    # Marcar o tempo de início
    inicio_tempo = time.time()

    # Contar o número de ocorrências de cada caractere
    resultado_ocorrencias = contar_ocorrencias(texto)

    # Marcar o tempo de fim
    fim_tempo = time.time()

    # Calcular o tempo total de execução
    tempo_total = fim_tempo - inicio_tempo

    # Exibir resultados
    print("\nOcorrências de cada caractere:")
    for char, ocorrencias in resultado_ocorrencias.items():
        print(f"'{char}': {ocorrencias}")

    print(f"\nTempo de execução: {tempo_total} segundos")
