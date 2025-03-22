##Função com Retorno



def media(nota1, nota2, nota3): 
    resultado = (nota1 + nota2 + nota3) / 3
    return resultado

nota1 = 5,5
nota2 = 3,6
nota3 = 9,8

resultado_media = media(nota1, nota2, nota3)
print(f"A média das notas é: {resultado_media}")
