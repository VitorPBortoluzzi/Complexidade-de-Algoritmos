## Resumo: 
- 2/3 Páginas
- Referências
- Discussão: O que entenderam sobre o assunto?
## Assunto
```
- Tratabilidade
- P/NP/NP-Completo
```


# Tratabilidade

Definição: Refere-se à capacidade de resolver um problema computacional de forma eficiente, utilizando algoritmos que funcionam dentro de limites razoáveis de tempo e recursos.

Tratável - Um problema é dito tratável se existe um algoritmo determinístico que o resolve em tempo polinomial, expresso como O(n^k).
    São aqueles que podem ser resolvido em tempo polinomial(P), o tempo de execu~ção do algoritmo que resolve o problema cresce de forma polinomial em relação ao tamanho da entrada.

Intratável - Problemas que não podem ser resolvidos em tempo polinomial são considerados intratáveis.
    São problemas para os quais não se conhece nenhum algoritmo que os resolva em tempo polinomial.
    São ditos como NP & NP-Completo

## Classes de Complexidade:
P (Polynomial Time)
Definição: Conjunto de problemas que podem ser resolvidos por um algoritmo determinístico em tempo polinomial.
Exemplo: Ordenar uma lista de números usando Merge Sort (O(n log n)).
NP (Nondeterministic Polynomial Time)
    Definição: Conjunto de problemas cujas soluções podem ser verificadas em tempo polinomial por um algoritmo determinístico.
    Exemplo: Problema de Satisfatibilidade Booleana (SAT), onde podemos verificar em tempo polinomial se uma atribuição de variáveis satisfaz uma fórmula booleana.
NP-completo
    Definição: Conjunto de problemas que são tanto NP quanto NP-difíceis. Um problema é NP-completo se for o mais difícil dentro de NP, ou seja, se todos os problemas em NP podem ser reduzidos a ele em tempo polinomial.
    Exemplo: Problema SAT, que foi o primeiro problema provado ser NP-completo.
NP-hard
    Definição: Conjunto de problemas que são pelo menos tão difíceis quanto os problemas NP-completos. Eles não precisam estar em NP (ou seja, suas soluções não precisam ser verificáveis em tempo polinomial), mas todos os problemas em NP podem ser reduzidos a eles em tempo polinomial.
    Exemplo: Problema de otimização de clique máximo.

https://theory.cs.princeton.edu/complexity/

A teoria da complexidade computacional é um ramo da teoria da computação em ciência da computação teórica e matemática que se concentra em classificar problemas computacionais de acordo com sua dificuldade inerente, e relacionar essas classes entre si. Neste contexto, um problema computacional é entendido como uma tarefa que é, em princípio, passível de ser resolvida por um computador (o que basicamente significa que o problema pode ser descrito por um conjunto de instruções matemáticas).
Informalmente, um problema computacional consiste de instâncias do problema e soluções para essas instâncias do problema. Por exemplo, o teste de primalidade é o problema de determinar se um dado número é primo ou não. As instâncias deste problema são números naturais, e a solução para uma instância é sim ou não, dependendo se o número é primo ou não.

Um problema é considerado como inerentemente difícil se a sua solução requer recursos significativos, qualquer que seja o algoritmo usado. A teoria formaliza esta intuição através da introdução de modelos matemáticos de computação para estudar estes problemas e quantificar os recursos necessários para resolvê-los, tais como tempo e armazenamento. Outras medidas de complexidade também são utilizadas, tais como a quantidade de comunicação (usada em complexidade de comunicação), o número de portas em um circuito (usado na complexidade de circuito) e o número de processadores (usados em computação paralela). Um dos papéis da teoria da complexidade computacional é determinar os limites práticos do que os computadores podem e não podem fazer.

Campos intimamente relacionados com a ciência da computação teórica são a análise de algoritmos e a teoria da computabilidade. Uma distinção chave entre a análise de algoritmos e teoria da complexidade computacional é que a primeira é dedicada a analisar a quantidade de recursos necessários para um determinado algoritmo resolver um problema, enquanto o segundo faz uma pergunta mais geral sobre todos os possíveis algoritmos que podem ser usados para resolver o mesmo problema. Mais precisamente, ele tenta classificar os problemas que podem ou não podem ser resolvidos com os recursos devidamente restritos. Por sua vez, impondo restrições sobre os recursos disponíveis é o que distingue a complexidade computacional da teoria da computabilidade: a segunda pergunta que tipos de problemas podem, em princípio, ser resolvidos através de algoritmos.

*Mensuração do tamanho de uma instância
Para medir a dificuldade de resolver um problema computacional, pode-se desejar ver quanto tempo o melhor algoritmo necessita para resolver o problema. No entanto, o tempo de execução pode, em geral, depender da instância. Em particular, instâncias maiores exigirão mais tempo para resolver. Assim, o tempo necessário para resolver um problema (ou o espaço necessário, ou qualquer outra medida de complexidade) é calculado em função do tamanho da instância. Isso geralmente leva em consideração o tamanho da entrada em bits. A Teoria da Complexidade está interessada em como os tempos de execução de algoritmos crescem com um aumento no tamanho da entrada. Por exemplo, no problema de descobrir se um grafo é conectado, quanto tempo a mais leva para resolver um problema para um grafo com 2n vértices comparado ao tempo levado para um grafo com n vértices?

Se o tamanho da entrada é n, o tempo gasto pode ser expresso como uma função de n. Já que o tempo gasto em diferentes entradas de mesmo tamanho pode ser diferente, o pior caso em complexidade de tempo T(n) é definido como sendo o tempo máximo dentre todas as entradas de tamanho n. Se T(n) é um polinômio em n, então o algoritmo é dito ser um algoritmo de tempo polinomial. A tese de Cobham diz que um problema pode ser resolvido com uma quantidade factível de recursos se ele admite um algoritmo de tempo polinomial.

Para uma definição precisa do que significa resolver um problema utilizando uma determinada quantidade de tempo e espaço, um modelo computacional tal como a máquina de Turing determinística é utilizado. O tempo exigido por uma máquina de Turing determinística M na entrada x é o número total de transições de estado, ou etapas, que a máquina faz antes de parar e responder com a saída ("sim" ou "não"). Diz-se que a máquina de Turing M opera dentro do tempo f(n), se o tempo exigido por M em cada entrada de comprimento n é no máximo f(n). Um problema de decisão A pode ser resolvido em tempo f(n) se existe uma operação da máquina de Turing em tempo f(n) que resolve o problema. Como a teoria da complexidade está interessada em classificar problemas com base na sua dificuldade, definem-se conjuntos de problemas com base em alguns critérios. Por exemplo, o conjunto de problemas solucionáveis no tempo f(n) em uma máquina de Turing determinística é então indicado por DTIME(f(n)).

Definições análogas podem ser feitas para os requisitos de espaço. Embora o tempo e o espaço sejam os mais conhecidos recursos de complexidade, qualquer medida de complexidade pode ser vista como um recurso computacional. Medidas de complexidade são geralmente definidas pelos axiomas de complexidade de Blum. Outras medidas de complexidade utilizadas na teoria da complexidade incluem a complexidade de comunicação, a complexidade do circuito e a complexidade da árvore de decisão.


*Melhor, pior e caso médio de complexidade

O melhor, o pior e o caso médio de complexidade referem-se a três maneiras diferentes de medir a complexidade de tempo (ou qualquer outra medida de complexidade) de entradas diferentes do mesmo tamanho. Uma vez que algumas entradas de tamanho n podem ser mais rápidas para resolver do que outras, definimos as seguintes complexidades:

Complexidade no melhor caso: Esta é a complexidade de resolver o problema para a melhor entrada de tamanho n.
Complexidade no pior caso: Esta é a complexidade de resolver o problema para a pior entrada de tamanho n.
Complexidade no caso médio: Esta é a complexidade de resolver o problema na média. Essa complexidade só é definida com relação a uma distribuição de probabilidade sobre as entradas. Por exemplo, se todas as entradas do mesmo tamanho são consideradas terem a mesma probabilidade de aparecer, a complexidade do caso médio pode ser definida com relação à distribuição uniforme sobre todas as entradas de tamanho n.
Por exemplo, considere o algoritmo de ordenação quicksort. Isso resolve o problema de ordenar uma lista de inteiros que é dada como entrada. O pior caso é quando a entrada já está ordenada ou está em ordem inversa, e o algoritmo leva tempo O(n2) para este caso. Se assumirmos que todas as permutações possíveis da lista de entrada são igualmente prováveis, o tempo médio necessário para a ordenação é O(n log n). O melhor caso ocorre quando cada pivô divide a lista pela metade, também precisando tempo O(n log n).

*Limites superior e inferior da complexidade dos problemas
Para classificar o tempo de computação (ou recursos semelhantes, como o consumo de espaço), é necessário provar os limites superiores e inferiores sobre a quantidade mínima de tempo exigida pelo algoritmo mais eficiente para resolver um determinado problema. A complexidade de um algoritmo é geralmente entendida como a sua complexidade de pior caso, a menos que seja especificado o contrário. A análise de um determinado algoritmo cai sob o campo de análise de algoritmos. Para mostrar um limite superior T(n) sobre a complexidade de tempo de um problema, é necessário mostrar apenas que há um determinado algoritmo com tempo de funcionamento, no máximo, T(n). No entanto, provar limites inferiores é muito mais difícil, uma vez que limites inferiores fazem uma declaração sobre todos os possíveis algoritmos que resolvem um determinado problema. A frase "todos os algoritmos possíveis" inclui não apenas os algoritmos conhecidos hoje, mas qualquer algoritmo que possa ser descoberto no futuro. Para mostrar um limite inferior de T(n) para um problema requer mostrar que nenhum algoritmo pode ter complexidade de tempo menor do que T(n).

Limites superiores são geralmente indicados usando a notação O-grande, que desconsidera fatores constantes e termos menores. Isso faz com que os limites independam dos detalhes específicos do modelo computacional utilizado. Por exemplo, T(n) = 7n2 + 15n + 40, em notação O-grande seria escrito da seguinte forma T(n) = O(n2).

Limites inferiores são geralmente indicados usando a notação Ω


#Classes de complexidade
*Definição de classes de complexidade
Uma classe de complexidade é um conjunto de problemas de complexidade relacionados. As classes mais simples de complexidade são definidas pelos seguintes fatores:

O tipo de problema computacional: Os problemas mais comumente utilizados são problemas de decisão. No entanto, classes de complexidade podem ser definidas com base em problemas de função, problemas de contagem, problemas de otimização, problemas de promessa, etc.
O modelo de computação: O modelo mais comum de computação é a máquina de Turing determinística, mas muitas classes de complexidade são baseadas em máquinas de Turing não-determinísticas, circuitos Booleanos, máquinas de Turing quânticas, circuitos monótonos, etc.
O recurso (ou recursos) que está sendo limitado e os limites: Essas duas propriedades são geralmente declaradas em conjunto, tais como "tempo polinomial", "espaço logarítmico", "profundidade constante", etc.
É claro, algumas classes de complexidade têm definições complexas que não se encaixam nesse quadro. Assim, uma classe de complexidade típica tem uma definição como a seguinte:

O conjunto de problemas de decisão solúveis por uma máquina de Turing determinística dentro do tempo f(n). (Esta classe de complexidade é conhecida como DTIME(f(n))).
Mas limitar o tempo de computação acima por alguma função concreta f(n) muitas vezes produz classes de complexidade que dependem do modelo da máquina escolhida. Por exemplo, a linguagem {xx | x é uma sequência binária qualquer} pode ser resolvida em tempo linear em uma máquina de Turing multi-fitas, mas necessariamente exige tempo quadrático no modelo de máquinas de Turing single-fita. Se permitirmos variações no tempo polinomial em execução, a tese de Cobham-Edmonds afirma que "as complexidades do tempo em quaisquer dois modelos razoáveis e gerais de computação são polinomialmente relacionados" (Goldreich 2008, Chapter 1.2). Isto forma a base para a classe de complexidade P, que é o conjunto de problemas de decisão solúveis por uma máquina de Turing determinística dentro do tempo polinomial. O conjunto correspondente de problemas de função é FP.

Importantes classes de complexidade

Uma representação da relação entre as classes de complexidade
Muitas classes de complexidade importantes podem ser definidas por limitando o tempo ou espaço usado pelo algoritmo. Algumas importantes classes de complexidade de problemas de decisão definidas desta maneira são as seguintes:

Classe de complexidade	Modelo de computação	Limitação de recursos
DTIME(f(n))	Máquina de Turing Determinística	Tempo f(n)
P	Máquina de Turing Determinística	Tempo poly(n)
EXPTIME	Máquina de Turing Determinística	Tempo 2poly(n)
NTIME(f(n))	Máquina de Turing Não-Determinística	Tempo f(n)
NP	Máquina de Turing Não-Determinística	Time poly(n)
NEXPTIME	Máquina de Turing Não-Determinística	Tempo 2poly(n)
DSPACE(f(n))	Máquina de Turing Determinística	Espaço f(n)
L	Máquina de Turing Determinística	Espaço O(log n)
PSPACE	Máquina de Turing Determinística	Espaço poly(n)
EXPSPACE	Máquina de Turing Determinística	Espaço 2poly(n)
NSPACE(f(n))	Máquina de Turing Não-Determinística	Espaço f(n)
NL	Máquina de Turing Não-Determinística	Espaço O(log n)
NPSPACE	Máquina de Turing Não-Determinística	Espaço poly(n)
NEXPSPACE	Máquina de Turing Não-Determinística	Espaço 2poly(n)



Problemas que podem ser resolvidos na teoria (por exemplo, dado um tempo infinito), mas que na prática levam muito tempo para as suas soluções sejam úteis, são conhecidos como problemas intratáveis.[11] Na teoria da complexidade, os problemas que não apresentam soluções em tempo polinomial são considerados intratáveis por mais pequenas que sejam suas entradas. Na verdade, a tese de Cobham-Edmonds afirma que apenas os problemas que podem ser resolvidos em tempo polinomial podem ser computados de maneira factível por algum dispositivo computacional. Problemas que são conhecidos por serem intratáveis neste sentido incluem aqueles que são EXPTIME-difícil. Se NP não é o mesmo que P, então os problemas NP-completo são também intratáveis neste sentido. Para ver porque algoritmos de tempo exponencial podem ser impraticáveis, considere um programa que faz 2n operações antes de parar. Para n pequeno, digamos 100, e assumindo, por exemplo, que o computador faz 1012 operações por segundo, o programa seria executado por cerca de 4 × 1010 anos, que é aproximadamente a idade do universo. Mesmo com um computador muito mais rápido, o programa só seria útil para casos muito pequenos e, nesse sentido, a intratabilidade de um problema é um tanto independente do progresso tecnológico. No entanto, um algoritmo de tempo polinomial não é sempre prático. Se seu tempo de execução é, digamos "n"15, não é razoável considerá-lo eficiente e ainda é inútil, salvo em casos de pequeno porte.

O que intratabilidade significa na prática está aberto em debate. Dizer que um problema não está em P não implica que todos os grandes casos de problemas são difíceis ou até mesmo que a maioria deles são. Por exemplo, o problema da decisão na Aritmética de Presburger tem demonstrado não estar em P, ainda foram escritos algoritmos que resolvem o problema em tempos razoáveis na maioria dos casos. Da mesma forma, os algoritmos podem resolver o problema da mochila NP-completo em uma ampla faixa de tamanhos em menos que o tempo quadrático e resolvedores de SAT rotineiramente lidam com grandes instâncias do problema de satisfatibilidade booleana NP-completo.