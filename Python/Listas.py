lista = ["Messi", "Cristano Ronaldo", "Neymar", "Haaland", "Mbappé"]
lista.append("Iniesta")
print(lista)

"""
clear() -> limpar lista
copy() -> evita fazer alterações na lista original
count() -> quantas vezes um valor aparece na lista
extend() -> unir duas linguas sem eliminar itens duplicados
index() -> saber índice de um valor da lista, apenas retorna primeira ocorrência
pop() -> retira ultimo elemento adicionado, ou pode usar o índice para retirar
remove() -> seleciona o valor que você deseja retirar da lista
reverse() -> espelha a lista
sort(
    reverse -> ordena alista de tráz para a frente
    key -> criar uma função anônima
) -> ordena a lista

"""

lista2 = lista.copy()
lista2.clear()
lista2.append("Lista zerada")
print(lista2)

Melhores = lista.copy()
"""
                    #parametro
                        #|  #expressão
"""
Melhores.sort(key = lambda x: len(x))
           #função anonima|cada item na lista vai ser ordenado pelo número de letras, está automaticamente em ordem ascendente
print(Melhores)