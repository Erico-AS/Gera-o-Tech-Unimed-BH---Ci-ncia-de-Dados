print("Bem vindo!", end="\n")

while 1 == 1:		
	
		processo = input("Selecione [1] para sacar, [2] para depositar ou [3] para sair: ",)
		print("")

		if processo == "1":		
	
			def sacar(valor):

				saldo = 1000
				
				if saldo >= valor:
					print("\nSaque realizado com sucesso! \n")
					
					saldo -= valor
					print("O valor retirado foi: ", valor)
					print("Seu saldo é de: ", saldo, end="\n")

				else:
					print("Não foi possível realizar o saque", end="\n")
					print(sacar(float(input("Digite um valor: ")))) 
				
			sacar(float(input("Digite um valor: ")))
			print("") 

		elif processo == "2":
			
			def depositar(valor):

				saldo += valor
				
				status = f"Seu saldo é de: {saldo}" if valor > 0 else "Valor negativo" 
				print(status)
			
			depositar(float(input("Escreva o valor: "))) 
		
		elif processo != "1" or processo != "2" or processo != "3":	
			print("Você escolheu um número inválido ou digitou algo fora das opções \n")
			print(processo)

		else:
			print("Obrigado pela preferência")	