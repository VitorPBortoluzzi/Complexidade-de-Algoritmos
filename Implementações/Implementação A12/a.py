def somaVetores(vetorA, vetorB):
    result = [] #1 atrib
    if len(vetorA)==len(vetorB): #3 i(1comp,2aatrib)
        #{ Laço de repetição: n * Atribuições (3 + 1) = 4*N
        for i in range(len(vetorA)): #3i (Atribuição)
            result.append(vetorA[i]+vetorB[i]) #1I(Atribuição) A+B
        #}
    return result #1i


#Entrou no if:
# 1 + 3 + 4n + 1 => (4n + 5)
    
#Não entrou no if:
# 1 + 1

a=[1,2,3]
b=[4,5,6]
print(somaVetores(a,b))

#Estimar como um algoritmo fnciona a partir da expançao do numero de dados