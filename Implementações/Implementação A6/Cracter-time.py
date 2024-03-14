"""
Construir um algoritmo que receba como parâmetro um texto e retorne o numero de ocorrências de cada caractere (ordenado pelos caracteres).
Construir um contador de tempo de execução antes e depois da função que contabiliza as ocorrências.
O texto teste encontra-se anexado a tarefa.
"""
import time

def contar_caracters(texto):
    ocorrencia_caracter = {}
    for c in texto:
        if c in ocorrencia_caracter:
            ocorrencia_caracter[c] += 1
        else:
            ocorrencia_caracter[c] = 1
    return ocorrencia_caracter 

texto = """
Um retrato das mulheres na pesquisa
Assessoria de Comunicação (ASSECOM) em 08/03/2024


Com objetivo de compreender como ocorreu a inserção de mulheres em organizações de pesquisa, com ênfase em suas trajetórias profissionais e tecnológicas, foi realizado o estudo ‘Mulheres nas ciências: análise da inserção e das trajetórias de cientistas em instituições de pesquisa (Rio Grande do Sul, 1950-1960)’. A pesquisa iniciou no ano de 2023, através da pesquisadora e docente da Universidade Franciscana, Daiane Silveira Rossi. 

A apuração priorizou um recorte temporal, o qual define as décadas de 1950 e 1960 como um marco inicial na produção científica, que corresponde também à década de criação da Coordenação de Aperfeiçoamento de Pessoal de Nível Superior (CAPES) e do Conselho Nacional de Pesquisas (CNPq), sendo ambos tratados como símbolos da institucionalização das ciências no Brasil. Para Daiane, “a ideia de trabalhar com a temática de mulheres na ciência surgiu a partir da oportunidade de trabalhar no projeto já em andamento na época sobre ‘Mulheres na Fiocruz’. Com a oportunidade de vir trabalhar em Santa Maria, na UFN, resolvi também migrar a pesquisa, ou melhor, ampliá-la para o Rio Grande do Sul”. 

A pesquisa ressalta o contexto do processo de institucionalização e profissionalização das ciências no Brasil entre as mesmas décadas, que coincidiu com a ampliação do acesso de homens e mulheres ao ensino superior, cujo resultado foi o acentuado aumento do número de matriculados nesse nível de ensino. Essa ampliação do acesso à educação se deu a partir da criação das Faculdades de Filosofia no país. 


“A partir das Faculdades de Filosofia temos o ingresso em cursos como: Pedagogia, Letras, História, Geografia, Ciências Sociais, Matemática, Física, Química, Filosofia E História Natural (atual Biologia). A partir dessa diversidade de cursos, o país estava preparando uma mão de obra qualificada para, em primeiro lugar, a educação básica”, destaca a pesquisadora.

O estudo também ressalta que a partir das reformas educacionais dos anos 1930, o foco recaía sobre a ampliação do ensino para o que atualmente é conhecido como ensino fundamental completo. Diante disso, foi necessário professores capacitados em cada uma das disciplinas específicas. Para Daiane, o que alguns consideram o "efeito inesperado" das faculdades de filosofia, foi o ingresso em instituições científicas, sobretudo do público feminino. “Mulheres que antes possuíam apenas o Magistério ou nenhuma formação, agora tinham a possibilidade de concluir o ensino superior e a partir dele tanto dar aulas, quanto estagiar nos laboratórios de seus professores, como no caso das alunas de química, física e história natural”, afirma. 

O desenvolvimento do projeto possui duas frentes, uma direcionada a pesquisa sobre a presença de mulheres cientistas no Rio Grande do Sul voltada a investigar suas trajetórias profissionais. “O estudo busca compreender quem é esse público feminino pioneiro no estado, onde se formaram, em quais cursos e quais as principais linhas de atuação. A segunda fase, que se dará a partir do segundo semestre desse ano e próximo ano, diz respeito a divulgação dessas trajetórias, divulgação científica nas escolas, através de oficinas, palestras e distribuição de materiais educativos que ilustrem as trajetórias e inspirem mulheres e meninas a seguir a carreira científica”, acrescenta a docente.

O estudo, que ainda está em desenvolvimento, obteve como resultados parciais uma identificação de 42 mulheres em atuação em instituições científicas no Rio Grande do Sul. Segundo a pesquisadora, “conseguimos informações de 19 delas, sobre nascimento, local de atuação, área de pesquisa, instituição e curso de formação, principais publicações, entre outras. Já sabemos, por exemplo, que a maioria delas trabalhava na área de pesquisas em educação, mas que também havia mulheres atuando na Agronomia, Psicologia, Fisiologia, Física E Matemática”. No entanto, a pesquisa segue em desenvolvimento, com o objetivo de seguir os próximos passos em busca de registros diretamente nas instituições onde as pesquisadoras atuaram na década de 1950. 





UFN e a Pesquisa

A produção científica na Universidade Franciscana (UFN) se iniciou em meados de 2004, através da criação do Mestrado profissionalizante em Ensino de Física e de Matemática. A partir do crescimento em conjunto com a criação de processos, produtos e demais tecnologias, foi implantado, o Programa de Pós-graduação em Nanociências: mestrado (2006) e doutorado (2012). Em 2014, se fez a concretização do Programa de Pós-graduação em Ensino de Ciências e Matemática, nas modalidades Mestrado e Doutorado. No ano de 2015 se iniciou o funcionamento do Mestrado Profissional em Saúde Materno Infantil e, em 2016, Mestrado Acadêmico em Ciências da Saúde e da Vida e o Mestrado em Ensino de Humanidades e Linguagens.

Na Universidade Franciscana, o público feminino desempenha papéis de destaque em várias áreas acadêmicas. Em 2023 a UFN contava com um total de 346 pesquisadores, sendo eles docentes e discentes, desse grupo temos cerca de 244 mulheres. Para a Vice-reitora, pesquisadora e professora, Solange Binotto Fagan, um cenário de reconhecimento se faz perceptível diante das produções científicas. “Na área de Nanociências, aproximadamente 70% dos pesquisadores, incluindo docentes e estudantes, são mulheres, engajadas em atividades científicas de impacto internacional. Esses números refletem o ambiente propício à equidade de gênero e ao reconhecimento do talento das mulheres cientistas aqui na UFN”, finaliza a docente.
"""
inicio_tempo = time.time_ns()
resultado_ocorrencias = contar_caracters(texto)
print("\nOcorrências de cada caractere:")
for c, ocorrencia_caracter in resultado_ocorrencias.items():
    print(f"{c}': {ocorrencia_caracter}")
final_tempo = time.time_ns()
tempo_exec = final_tempo - inicio_tempo
print(tempo_exec)


"""
dicionario = {}
arquivo = open(nomeArquivo,encoding="UTF-8")
linhas = arquivo.readlines()
for linha in linhas:
    palavras = linha.split(' ')
    for palavra in palavras:
        if c in dicionario:
            dicionario[c] += 1
        else:
            dicionario[c] = 1
"""