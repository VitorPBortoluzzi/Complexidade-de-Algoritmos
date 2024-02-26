package main

import (
  "fmt"
  "runtime"
)

func main() {
  // Antes de realizar o cálculo
  printMemoryUsage("Antes do Cálculo")

  // Seu cálculo aqui
  resultado := realizarCalculo()

  // Após o cálculo
  printMemoryUsage("Após o Cálculo")

  // Use o resultado, faça o que for necessário
  fmt.Println("Resultado do cálculo:", resultado)
}

func realizarCalculo() int {
  // Simulando algum tipo de cálculo
  slice := make([]int, 100000)
  for i := range slice {
    slice[i] = i
  }

  return len(slice)
}

func printMemoryUsage(msg string) {
  var m runtime.MemStats
  runtime.ReadMemStats(&m)

  fmt.Printf("%s:\n", msg)
  fmt.Printf("  Alloc: %v MB\n", bToMb(m.Alloc))
  fmt.Printf("  TotalAlloc: %v MB\n", bToMb(m.TotalAlloc))
  fmt.Printf("  Sys: %v MB\n", bToMb(m.Sys))
  fmt.Printf("  NumGC: %v\n", m.NumGC)
  fmt.Println()
}

func bToMb(b uint64) uint64 {
  return b / 1024 / 1024
}
