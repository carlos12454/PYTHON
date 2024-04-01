nome=input("digite seu nome ")
idade=int(input("digite sua idade "))
doenca_infectocontagiosa=input ("suspeita de doenca infectocontagiosa?")
if idade>= 60:
    print("o paciente "+ nome + "possui atendimento prioritario")
elif doenca_infectocontagiosa=="sim":
    print("o paciente "+ nome + "deve ser direcionado parasala de espera reservada")
else:
    print("o paciente " + nome + " não possui atendimento prioritario")
