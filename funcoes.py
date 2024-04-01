def pergunta ():
    return input ("oque deseja realizar?\n"
            "<I> - para inserir um usuario\n"+
            "<P> - para Pesquisar um usuario\n"+
            "<E> - para Excluir um usuario\n"+
            "<L> - para Listar um usuario :").upper()

def inserir(dicionario):
    dicionario[input("Digite o logi:").upper()]=[input("Digite o nome:").upper(),
                                                   input("Digitesua ultima data de aceeso :"),
                                                   input("qual a ultima estacao acessada:").upper()]
