import random
import string

def gerar_sequencia_aleatoria(tamanho):
    caracteres = string.ascii_letters + string.digits
    return ''.join(random.choice(caracteres) for _ in range(tamanho))

def quebraSenha(senha):
    quebraS = senha

senha = gerar_sequencia_aleatoria(4)
print(f"Sequência Aleatória: {senha}")




# def advinhar_sequencia(alvo):
#     tamanho = len(alvo)
#     tentativa = gerar_sequencia_aleatoria(tamanho)
#     tentativas = 1

#     while tentativa != alvo:
#         tentativa = gerar_sequencia_aleatoria(tamanho)
#         tentativas += 1

#     return tentativa, tentativas

# Usando a função para gerar uma sequência aleatória

# # Usando a função para advinhar uma sequência alvo
# sequencia_alvo = "AbCd1234"
# resultado, tentativas = advinhar_sequencia(sequencia_alvo)

# # Exibindo o resultado
# print(f"Sequência alvo: {sequencia_alvo}")
# print(f"Tentativa: {resultado}")
# print(f"Número de tentativas: {tentativas}")