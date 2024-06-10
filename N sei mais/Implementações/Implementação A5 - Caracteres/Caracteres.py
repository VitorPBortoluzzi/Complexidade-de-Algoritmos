def n_caracteres(palavra):
    #palavra = palavra.strip()
    palavra = palavra.replace(" ","")
    return len(palavra)

palavra = "Couro de Pano"
print(n_caracteres(palavra))
"""
|n_caracteres   |   referencia < 1 espaço> 
|função<replace>|   ? espaços <for?>
|len()          |   1 <Espaços>                 
|palavra        |   instrução <1 espaço> (String)
|print          |   instrução <1 espaço>
|               |   ("Impressão")("Atribuição")       
"""
