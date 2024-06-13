# **Notação BIG-O**

* Abstração para classificar em grupos os diferentes algoritmos conforme seu comportamento no pior caso.

**f(N) = N + 5 ---> *O(F(N)) = N***

**g(N) = 4N² + 8N + 5 ---> O(g(N))=N²**

**h(N)=5 --:> O(h(N))=1 == O(h(N^0))**

# Propriedades:
* i) Sendo f(N), O(f(N))=Maior expoente
* ii) Sendo k uma constante k*f(N) = O(f(N))
* iii) O(f(N)) + O(f(N)) = O(f(N))  
    *    --> 2*(O(f(N))) = O(f(N)) = 2ª Propriedade
* iv) O(f(N)) + O(g(N)) = **Max(f(N),g(N))**
* v) O(g(f(N))) = O(g(N)) * O(f(N)) = N² * N = N³

Atv 2:UN3P2
Calcular o Big O do código inteiro