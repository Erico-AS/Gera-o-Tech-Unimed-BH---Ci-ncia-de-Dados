# -*- coding: utf-8 -*-

"""
Estruturas de repetição

while == enquanto
for in = para cada elemento na variável

variáveis iguais arrays ultilizando []
"""

lista1 = [0,1,2,3,4,5]
lista2 = ["Ankara", "Messi", "Messii", "Messiii"]
lista3 = ["golo", 30, "goloo", 19, "golooo", 10]
messi = 10

while messi > 1:
	print(messi)
	messi-= 1

print("The best")

for elemento in lista2: #Para cada elemento dentro da lista, printar cada elemento da lista
	print(elemento)


"""
Range == retorna lista
Exp:

for elemento range (incioLista, términoLista, passoDaContagemDosElemento[Exp: 2 em 2, 3 em 3])

"""

for elemento in range(10,30,5):
	print(elemento)