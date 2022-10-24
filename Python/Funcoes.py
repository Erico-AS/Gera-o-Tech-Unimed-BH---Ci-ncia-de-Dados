# -*- coding: utf-8 -*-

"""
Funções:

lower() == tudo em minusculo 
upper() == tudo em maiusculo
title() == primeira letra maiuscula, resto minusculo

strip() == remove caracteres especiais e espaços
lstrip() == remove espaços a esquerda
rstrip() == remove espaços a direita

split() == divide uma string em um array -> a.split("critério")
find() == busca a posição que certo elemento está na string
replace() == susbtitui um elemento selecionado por outro elemento = a.replace("a", "b")
.count("palavra") == no exemplo, quantas vezes "palavra" aparece na variável

"""

frase1 = "rato roeu a roupa do rei de Roma."

print(frase1.lower())
print(frase1.upper())
print(frase1.title())
print(frase1.strip("."))
print(frase1.split())
print(frase1.find("rato"))
print(frase1.replace("rato", "rã"))

"""
Juntar e centralizar

center(quantos caracteres você quer para centralizar, qual caracter vai completar) == centraliza a string
join(string) == a cada itém de uma string ele adiciona um caracter

"""
frase2 = "palavra"

print(frase2.center(10,"#"))
print(",".join(frase2))