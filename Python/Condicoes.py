# -*- coding: utf-8 -*-

"""
Condições:

	if 'condição':
		codigo

	else:
		codigo 
"""

x = 5
y = 3

if x > 3:
	print("X é maior")

else: 
	print("Y é maior")

#Indentação influencia no encadeamento

x = -2
y = -1

if y > x:
	if y < 0:
		print("Num negativo")

	else:
		print("y maior")
else:
	print("X maior")


"""
'elif' = else com condição
"""

if y == x:
	print("iguais")

elif y > x:
	print("y maior")

else: 
	print("x maior")

#---------------------------------------------------------------------