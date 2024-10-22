"""
Exercício
Exiba os índices da lista
0 Maria
1 Paulo
2 José
"""
lista = ['Maria', 'Paulo', 'José', 'Pedro']

#listas são iteraveis por isso é possível usar o for

indice = 0
for nome in lista:
    print(indice, nome, type(nome))
    indice += 1

"""
Método Professor

lista = ['Maria', 'Paulo', 'José', 'Pedro']

#listas são iteraveis por isso é possível usar o for

indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))

"""