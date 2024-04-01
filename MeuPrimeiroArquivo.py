with  open("Primeiro_Arquivo.txt",  "r") as arquivo:
    for linha in arquivo.readlines():
        print(linha)
