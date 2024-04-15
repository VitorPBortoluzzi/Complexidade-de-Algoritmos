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
// N+1*2 + N*2
// 2N+2+2N
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
}
==================================================
Calculo:
while = (N+1)*(n_Comparações)+N*(Bloco)
N+1*1+ N*{1 + 4N²+7N+2}
4N³+7N²+4N+1
==================================================

while[96]:
while(gap < size) {
        gap = 3*gap+1;
    }
==================================================
Calculo:
while = (N+1)*(n_Comparações)+N*(Bloco)
(N+1)*1+(N*1)
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