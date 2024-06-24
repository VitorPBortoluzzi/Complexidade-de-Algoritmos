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


A teoria da complexidade computacional é um ramo da teoria da computação em ciência da computação teórica e matemática que se concentra em classificar problemas computacionais de acordo com sua dificuldade inerente, e relacionar essas classes entre si. Neste contexto, um problema computacional é entendido como uma tarefa que é, em princípio, passível de ser resolvida por um computador (o que basicamente significa que o problema pode ser descrito por um conjunto de instruções matemáticas).
Informalmente, um problema computacional consiste de instâncias do problema e soluções para essas instâncias do problema. Por exemplo, o teste de primalidade é o problema de determinar se um dado número é primo ou não. As instâncias deste problema são números naturais, e a solução para uma instância é sim ou não, dependendo se o número é primo ou não.

Um problema é considerado como inerentemente difícil se a sua solução requer recursos significativos, qualquer que seja o algoritmo usado. A teoria formaliza esta intuição através da introdução de modelos matemáticos de computação para estudar estes problemas e quantificar os recursos necessários para resolvê-los, tais como tempo e armazenamento. Outras medidas de complexidade também são utilizadas, tais como a quantidade de comunicação (usada em complexidade de comunicação), o número de portas em um circuito (usado na complexidade de circuito) e o número de processadores (usados em computação paralela). Um dos papéis da teoria da complexidade computacional é determinar os limites práticos do que os computadores podem e não podem fazer.

Campos intimamente relacionados com a ciência da computação teórica são a análise de algoritmos e a teoria da computabilidade. Uma distinção chave entre a análise de algoritmos e teoria da complexidade computacional é que a primeira é dedicada a analisar a quantidade de recursos necessários para um determinado algoritmo resolver um problema, enquanto o segundo faz uma pergunta mais geral sobre todos os possíveis algoritmos que podem ser usados para resolver o mesmo problema. Mais precisamente, ele tenta classificar os problemas que podem ou não podem ser resolvidos com os recursos devidamente restritos. Por sua vez, impondo restrições sobre os recursos disponíveis é o que distingue a complexidade computacional da teoria da computabilidade: a segunda pergunta que tipos de problemas podem, em princípio, ser resolvidos através de algoritmos.

Mensuração do tamanho de uma instância
Para medir a dificuldade de resolver um problema computacional, pode-se desejar ver quanto tempo o melhor algoritmo necessita para resolver o problema. No entanto, o tempo de execução pode, em geral, depender da instância. Em particular, instâncias maiores exigirão mais tempo para resolver. Assim, o tempo necessário para resolver um problema (ou o espaço necessário, ou qualquer outra medida de complexidade) é calculado em função do tamanho da instância. Isso geralmente leva em consideração o tamanho da entrada em bits. A Teoria da Complexidade está interessada em como os tempos de execução de algoritmos crescem com um aumento no tamanho da entrada. Por exemplo, no problema de descobrir se um grafo é conectado, quanto tempo a mais leva para resolver um problema para um grafo com 2n vértices comparado ao tempo levado para um grafo com n vértices?

Se o tamanho da entrada é n, o tempo gasto pode ser expresso como uma função de n. Já que o tempo gasto em diferentes entradas de mesmo tamanho pode ser diferente, o pior caso em complexidade de tempo T(n) é definido como sendo o tempo máximo dentre todas as entradas de tamanho n. Se T(n) é um polinômio em n, então o algoritmo é dito ser um algoritmo de tempo polinomial. A tese de Cobham diz que um problema pode ser resolvido com uma quantidade factível de recursos se ele admite um algoritmo de tempo polinomial.