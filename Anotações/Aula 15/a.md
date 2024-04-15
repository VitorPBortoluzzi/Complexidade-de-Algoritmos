```c
void selecao (int vet, int tam){
    int i, j, min, x;
    for (i=1; i<=n-1; i++){
        min = i;
        for (j=i+1; j<=n; j++){
                if (vet[j] < vet[min])
                min = j;
        }
	x = vet[min];
	vet[min] = vet[i];
	vet[i] = x;
    }
}
```
## 0ª Identificar instruções de atribuição e comparação
* 12 Instruções
## 1ªRegra: Calcular o laço mais interno;
* **Inicialização + (Condição+1) + incremento/decremento**  
* **Inicialização + ((N+1)*n_condições) + (N * n_incrementos/decremento)**  
* Intruções For:
  * (1\*Ini) + [(N+1)\* C] + N\*Incremento + N \* Bloco  
    1\*1 + (N+1) + (N\*1)
---
Calculo:

### 1º For(+Interno): 
```c
for (j=i+1; j<=n; j++){
    if (vet[j] < vet[min])
    min = j;
}
``` 
```
    Pior caso:
    1 \* 1 + [(N+1) \* 1] + N\* 1 + {N \* 2}
    1 + N + 1 + N + 2N
    4N + 2
```
```
    Melhor caso:
    1 \* 1 + [(N+1) \* 1] + N\* 1 + {N \* 1}
    1 + N + 1 + N + 1N
    3N+2
```
___
### 2º For:
```c
for (i=1; i<=n-1; i++){
        min = i;
        for (j=i+1; j<=n; j++){
                if (vet[j] < vet[min])
                min = j;
        }
	x = vet[min];
	vet[min] = vet[i];
	vet[i] = x;
    }
```
* (1\*Ini) + [(N+1)\* C] + N\*Incremento + N \* Bloco 
```
Bloco = Pior Caso:4N+2  
[(4N+2)+4]  
1+(N+1)*1 + N\*1 + N * bloco  
1+N+1+N+(4N²+2N+4N)
4N²+8N+2
```
**4N²+8N+2**

```
Bloco = Melhor Caso:3N+2 
[(3N+2)+4]
1+(N+1)*1 + N\*1 + N * bloco 
1+N+1+N+(3N²+2N+4N)
3N²+8N+2
```
**3N²+8N+2**