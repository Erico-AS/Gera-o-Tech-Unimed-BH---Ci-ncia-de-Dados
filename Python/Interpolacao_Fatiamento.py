"""

f -> interpolar strings dentro de uma string ou print

"""

nome = "Erico"
idade = 17
linguagem = "python"
instituicao = "dio"

print(f"Olá, meu nome é {nome}, tenho {idade} anos, estou aprendo {linguagem.title()} na {instituicao.upper()}")

# cm para m

cm = 100.00

print(f"O valor em cm é: {cm}. E em metros é: {cm:.0f}")


"""
Fatiamento

variavel[start,end,passo]
"""

nome = "Erico Augusto"

print(nome[0])
print(nome[0:5])
print(nome[0::2])
print(nome[::-1])

#MENU(apenas corpo)

print("""
		################ MENU ###################

		1 - Começar
		2 - Esperar
		3 - Encerrar

		#########################################

			Obrigado por usar nosso sistema!
""")