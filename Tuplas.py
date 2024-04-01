usuario=()
email =["wwww@xyt.com", "aaaa@xty.co"]

tupla = list(enumerate(email))

for chave in range(0, len(tupla)):
    print("email:", tupla[chave][1])
    usuario[tupla[chave]]=[input("Digite o nome "), input("Digite o nivel")]
    
for chave, dado in  usuario.item():
    print("usuario...:",chave[0])
    print("email...:",chave[1])
    print("nome...:",chave[0])
    print("nivel...:",chave[1])