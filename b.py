import time
from collections import defaultdict

def contar_ocorrencias(texto):
    # Inicializar um dicionário para armazenar as contagens de caracteres
    contagem_caracteres = defaultdict(int)

    # Contar as ocorrências de cada caractere no texto
    for caractere in texto:
        contagem_caracteres[caractere] += 1

    # Retornar as contagens ordenadas por caractere
    return dict(sorted(contagem_caracteres.items()))

# Função para medir o tempo de execução de uma função
def medir_tempo_execucao(funcao, *args, **kwargs):
    inicio_tempo = time.time()
    resultado = funcao(*args, **kwargs)
    fim_tempo = time.time()
    tempo_execucao = fim_tempo - inicio_tempo
    return resultado, tempo_execucao

# Texto de exemplo
texto_exemplo = "A pesquisa ressalta o contexto do processo de institucionalização e profissionalização das ciências no Brasil entre as mesmas décadas, que coincidiu com a ampliação do acesso de homens e mulheres ao ensino superior, cujo resultado foi o acentuado aumento do número de matriculados nesse nível de ensino. Essa ampliação do acesso à educação se deu a partir da criação das Faculdades de Filosofia no país."

# Medir o tempo de execução da função contar_ocorrencias
contagens, tempo_execucao = medir_tempo_execucao(contar_ocorrencias, texto_exemplo)

# Exibir resultados
print("Contagens de caracteres:\n", contagens)
print("Tempo de execução:", tempo_execucao, "segundos")
