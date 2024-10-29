"""
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com
erros de índices inexistentes na lista
"""
import os
lista = []

while True:
    entrada = input('Selecione uma opção:\n[i]nserir [a]pagar [l]istar:')    

    if entrada == 'l':
        indice = 0
        tamanho = len(lista)
        os.system('cls')
        if tamanho == 0:
            print('Nada para listar')
        else:
            for nome in lista:
                print(indice, nome)
                indice += 1
    elif entrada == 'i':
        inserir = input('Valor:')
        lista.append(inserir)
        os.system('cls')
    elif entrada == 'a':
        try:
            apagar = int(input('Escolha o índice para apagar:'))
            lista.pop(apagar)
            os.system('cls')
        except:
            print('Não foi possível apagar da lista')
    else:
        print('Por favor escolha "i", "a" ou "l"')
