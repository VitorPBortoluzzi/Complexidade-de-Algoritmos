# Regras:

## 1ªRegra: Calcular o laço mais interno;
```C
for no C:
N--> (1*I)+(N+1)*C+(NIn)+N(Bloco)
```
NIn = N * (numero de incremento e decrementos)
### Inicialização + (Condição+1) + incremento/decremento
```C
for(i=0;i=j;i>m && j<100;i++,j++,k--){}

(1*2)+(N+1)*2)+(N*3)+(N*3)  
2+2N+2+3N+3N  
8N+4 
```


Laço em C do Google Sorte  
For_Interno
```c
if(vetor[j] > vetor[j+1]){
    aux = vetor[j];
    vetor[j] = vetor[j+1]
    vetor[j+1] = aux;
}
# Bloco possui 6 Instruções:
# 1+N+1+N+6N  
# 8N+2  
``` 
For_Externo:
```c
for(k=1;k<n;k++>) {
    printf("\n[%d] ",k);
    for(j=0;j < n-1; j++){
        if(vetor[j] > vetor[j+1]){
            aux = vetor[j];
            vetor[j] = vetor[j+1]
            vetor[j+1] = aux;
        }
    }
}
# 1+N+1+N+N(Bloco)
# Bloco=2+8N+2
# Bloco8N+4
# 2N+2+N(8N+4)
# 2N+2+8N^2+4N
# Bubble = 8N^2+6N+2
```
 

### https://www.sortvisualizer.com/insertionsort/
```c
 void insertionSort(int arr[], int n)
{
    int i, key, j;
    for (i = 1; i < n; i++) {
        key = arr[i];
        j = i - 1;

        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j = j -1;
        }
        arr[j + 1] = key;
    }
}

1+(N+1)+(N)+N*(Bloco)  
Bloco:  
1a  
1a  
while = (N+1)*(n_Comparações)+N*(Bloco)  
{
    2N+2+2N
    4N+2
}
1a  
Bloco: 2+4N+2+1= 4N+5
F:2N+2+4N²+5N
4N²+7N+2
---





### **while = for**

    while (j >= 0 && arr[j] > key) {
                arr[j + 1] = arr[j];
                j--;
            }

    for ( ;j>= 0 && arr[j] > key; j--){
        arr[j + 1] = arr[j];
    }
    0 + (N+1)*2+(N)+N(Bloco)
    2N+2 + N + N
    4N+2
```


### Professor - Insertion Sort

```c
 void insertionSort(int arr[], int n)
{
    int i, key, j;
    for (i = 1; i < n; i++) {
        key = arr[i];
        j = i - 1;

        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j = j - 1;
        }
        arr[j + 1] = key;
    }
}

While = (N+1)(Comparação)+N(Bloco)
4N+2

Bloco:2+4N+2+1 = 4N+5
For:1+N+1+N+N(4N+5) = 4N²+7N+2

)```