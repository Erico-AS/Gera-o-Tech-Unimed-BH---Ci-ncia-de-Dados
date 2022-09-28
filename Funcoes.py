# -*- coding: utf-8 -*-

"""
Funções:

lower() == tudo em minusculo 
upper() == tudo em maiusculo
strip() == remove caracteres especiais e espaços
split() == divide uma string em um array -> a.split("critério")
find() == busca a posição que certo elemento está na string
replace() == susbtitui um elemento selecionado por outro elemento = a.replace("a", "b")

"""

frase1 = "rato roeu a roupa do rei de Roma."

print(frase1.lower())
print(frase1.upper())
print(frase1.strip("."))
print(frase1.split())
print(frase1.find("rato"))
print(frase1.replace("rato", "rã"))
