lista = [10,8,3,15,4]

def ordena(listagem):
    i = 0
    j = 0
    tamanho = len(listagem)
    while j<(tamanho-1):
        while i<(tamanho-1):
            if listagem[i]>listagem[i+1]:
                listagem[i],listagem[i+1] = listagem[i+1],listagem[i]
            i+=1
        i= 0
        j+=1
    return listagem
print(lista)
ordena(lista)
print(lista)

""" 
------------------------------------------
lista = [10,8,3,15,4] (7 espaços??? <16bits?>)

def ordena(listagem):   ordena(Guarda referencia -> 16bits)

------------------------------------------

# 1 var --> 16bits
# 1 instrução --> 16bits

---------------------------------------------------------------------
|lista[]        |   7<Espaços>                                      |
{===================================================================}
{lista[1]	    |	16bits <int>    					            }
{lista[0]	    |	16bits <int>    					            }
{lista[3]	    |	16bits <int>    					            }
{lista[2]	    |	16bits <int>    					            }
{lista[4]	    |	16bits <int>    					            }
{lista[5]	    |	16bits <int>    					            }
{lista[6]	    |	16bits <int>    					            }
{lista<ponteiro>|   <16bits>                                        }
{===================================================================}
|ordena         |   16bits                                          |
|listagem	    |	1 <Espaços> 					                |
|i              |   1 <Espaços>                                     |
|j              |   1 <Espaços>                                     |
|tamanho        |   1 <Espaços>  (atribuição<int>(Função<len>))     |
|len()          |   1 <Espaços> --> <p = listagem>                  |
|

|instruções	    |	("")("")("Atribuição")|
---------------------------------------------------------------------
"""