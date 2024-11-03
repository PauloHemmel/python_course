"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeoros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.: 746.824.890-70


"""

entrada = input('Digite um CPF com 9 DI')
indice = 0
indice2 = 0
indice3 = 1

lista = [10, 9, 8]
lista2 = []
lista3 = []
soma = 0
for valores in entrada:
    lista3.append(int(valores)*(lista[indice]))
     
    indice += 1
    
while indice2 <= 2:
    soma = lista3[indice2] + lista3[indice3] 
    indice2 += 1
    indice3 += 1

print(lista3, soma)
# while indice <= 3:
#     resultado = (lista[indice])*(lista2[indice])
#     indice += 1
# print(resultado)