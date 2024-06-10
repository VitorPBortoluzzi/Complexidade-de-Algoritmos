```c
void selecao (int vet, int tam){
    int i, j, min, x;
    for (i=1; i<=tam-1; i++){
        min = i;
	for (j=i+1; j<=tam; j++){
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







---


#Mirkos@ufn.edu.br
#Assunto: Cálculo de instruções


```c
void shellSort(int *vet, int size) {
    int i , j , value;
    int gap = 1;
    while(gap < size) {
        gap = 3*gap+1;
    }
    while ( gap > 1) {
        gap /= 3;
        for(i = gap; i < size; i++) {
            value = vet[i];
            j = i - gap;
            while (j >= 0 && value < vet[j]) {
                vet [j + gap] = vet[j];
                j -= gap;
            }
            vet [j + gap] = value;
        }
    }
}

// while interno do for:
// while (j >= 0 && value < vet[j]) {
//     vet [j + gap] = vet[j];
//     j -= gap;
// }
// while = (N+1)*(n_Comparações)+N*(Bloco)  
// for(;j>=0 && value < vet[j];j -= gap){
//     vet [j + gap] = vet[j];
// }
* (1\*Ini) + [(N+1)\* C] + N\*Incremento + N \* Bloco
// 0 + [(N+1)*2] + N + N*{1}
// 2N+2+N+N
// 4N+2
==================================================
Calculo:
for interno:
1 + (N+1) + N + N*{2 + 4N+2 + 1}
4N²+7N+2
==================================================
2ºwhile(while externo[99]):
while ( gap > 1) {
        gap /= 3;
        4N²+7N+2
}
---
for(;gap>1;){
    gap /= 3;
    4N²+7N+2
}
==================================================
Calculo:
0 + N+1 + 0 + N*{1 + 4N²+7N+2}
4N³+7N²+4N+1
==================================================

while[96]:
while(gap < size) {
        gap = 3*gap+1;
    }
---
for(;gap < size;)
    gap = 3*gap+1;

==================================================
Calculo:
0 + N+1 + 0 + N
2N+1
==================================================
```
```c
shell_sort:
void shellSort(int *vet, int size) {
    int i , j , value;
    int gap = 1;
    2N+1
                // while(gap < size) {
                //     gap = 3*gap+1;
                // }
    4N³+7N²+4N+1
                // while ( gap > 1) {
                //     gap /= 3;
                //     for(i = gap; i < size; i++) {
                //         value = vet[i];
                //         j = i - gap;
                //         while (j >= 0 && value < vet[j]) {
                //             vet [j + gap] = vet[j];
                //             j -= gap;
                //         }
                //         vet [j + gap] = value;
                //     }
                // }
}

```

