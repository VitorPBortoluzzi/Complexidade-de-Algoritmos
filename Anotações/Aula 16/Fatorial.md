```c
//Fatorial com recursividade:
int fatorial (int numero){
    if (numero==0 || numero ==1)  //N*
        return 1;   //1
    return numero*fatorial(numero-1); //(N-1)*2   --> 2 Passagens de parametro
}

==============================
3!
-----
(N*2) + 1 + (N-1)*(2)
4n-1

//Calculo de fibonacci recursivo:

int fibonacci(int n) {
  if (n == 1 || n == 2) {   // N*2
    return 1;   // +1
  } 
  return fibonacci(n-1) + fibonacci(n-2); // (N-1)*3
}
===============
[(N*2) + 1] + (N-1)*1 + (N-2)*1

2N+1 + (N-1)*3
2N+1 + 3N-3
5N-2


```