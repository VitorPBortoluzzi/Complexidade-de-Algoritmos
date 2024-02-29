//Usando GO
package main

import (
	"fmt"
)

func mySoma(a int, b int) int {
	return a + b
}

func main() {
	fmt.Println(mySoma(5, 10))
}


/*------------------
|main		|	
|mySoma		|	return func (int64)
|a			|	int64
|b			|	int64
|instruções	|	("soma")("impressão")("Atribuição")
*/