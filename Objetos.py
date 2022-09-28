# -*- coding: utf-8 -*-

"""
Objetos

concatenar == usar o sinal '+'
len == usar len(variável)
sequencia == usar variável[inicio:fim]

"""

var1 = "messi"
var2 = "+"
var3 = "10"

print(var1 + var2 + var3)
print(len(var1 + var2 + var3)) #Mostrar quantidade de caracteres da concatenação das 3 variáveis

Jog1 = "Messi"
Jog2 = "Suárez"
Jog3 = "Neymar"

print(Jog1[0] + Jog2[0] + Jog3[0]) #Mostrar primeira letra de cada nome
print(Jog3[0:3]) #Técnicamente o Py vai por quantidade e não por posição
print("P" + Jog1[1] + "p" + Jog1[3:5]) 

print(Jog1[2:]) #Tirar letras [Posição para tirar:vazio]