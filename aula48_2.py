"""
Lista em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: 
    append, insert, pop, del, clear, extend, +
Create Read Update  Delete
Criar, Ler, Alterar,Apagar = lista[i] (CRUD)
"""

lista = [10,20,30,40]
#numero = lista[2] #criar
#lista[2] = 300 #alterar valor
# del lista[2] #deletar
# print(lista[2])
lista.append(50) #adicionar na lista ao final
lista.pop() #remove o ultimo elemento da lista
ultimo_valor = lista.pop(0)
print(ultimo_valor,lista)
