# Nesse codigo, analisaremos a idade do usuario e falaremos 
#se ele é maior de idade ou não
nome = input ("Digite o seu nome: ")
idade = int(input ("Digite a sua idade: "))

print ("Olá, ",nome,"! A sua idade é ",idade)

# A estrutura de decisão analisa uma comparação e executa o codigo 
#com base na resposta. Para utilizarmos a estrutura de decisão, precisamos
# de comparadores, que são:

# - > maior
# - < menos
# - == igual
# - != diferente
# - >= maior ou igual
# - <= menor ou igual
# - ! não

# O comando de descisão é if
# A sintaxe é:
# if comparacao :
# E os itens a serem executados devem estar em um bloco identado
# if 20 > 30
#     print ("Algo de errado não está certo")

if idade >= 18:
    print ("você é maior de idade!")
    if idade >= 60:
        print ("você é idoso!")
        print ("já pode pegar a carteirinha de estacionamento")
else:
    print ("você é menor de idade!")
    print ("Não vai poder comprar cachaça!")