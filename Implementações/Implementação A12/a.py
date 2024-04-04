def somaVetores(vetorA, vetorB):
    result = [] #1 atrib
    if len(vetorA)==len(vetorB): #3 i(1comp,2aatrib)
        #{ Laço de repetição: n * Atribuições (3 + 2) = 5N
        for i in range(len(vetorA)): #3i (Atribuição)
            result.append(vetorA[i]+vetorB[i]) #2I(Atribuição,Parametro)
        #}
        return result #1i
        
# 1 + 3 + 5n + 1 => (5n + 5)
    
a=[1,2,3]
b=[4,5,6]
print(somaVetores(a,b))

#Estimar como um algoritmo fnciona a partir da expançao do numero de dados