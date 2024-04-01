inventario=[]
resposta="S"
while resposta=="S":
    inventario.append(input("equipamento: "))
    inventario.append(float(input("valor: ")))
    inventario.append(int(input("numero de serial: ")))
    inventario.append(input("derpartamento: "))
    resposta=input("Digite \"S\" para continuar: ") .upper()
    
for elemento in inventario:
    print(elemento)
