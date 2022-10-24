valores = input().split()
hora = int(valores[0])
vel = int(valores[1])
litros = (hora * vel) / 12

print(f"{litros:.3f}" )