"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeoros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.: 746.824.890-70


"""
#Feito por Paulo

# entrada = input('Digite um CPF com 9 Dígitos: ')
# indice = 0
# lista = [10, 9, 8, 7, 6, 5, 4, 3, 2]
# lista3 = []
# soma = 0
# for valores in entrada:
#     lista3.append(int(valores)*(lista[indice]))
     
#     indice += 1

# for item in lista3:
#     soma += item

# resultado = (soma * 10) % 11

# if resultado > 9:
#     final = 0
#     print(f'{entrada}{final}0')
# else:
#     print(f'{entrada}{resultado}0')

#Feito pelo Professor

cpf = '74682489070'
nove_digitos = cpf[:9]
contador_regressivo_1 = 10

resultado_digito_1 = 0
for digito in nove_digitos:
    resultado_digito_1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1
digito_1 = ((resultado_digito_1 * 10) % 11)
digito_1 = digito_1 if digito_1 <= 9 else 0
print(digito_1)