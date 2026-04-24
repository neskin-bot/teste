# Isso é um comentário.

# Agora, nós nescrevemos na tela usando o camando print.
# O comando print, serve para escrevermos alguma coisa.

print ("olá, mundo!")
print ("esse é o curso de lógica de programação.")

# O comando input () serve para receber uma entrada
# do teclado, sendo que o usuario irá digitar

# A sintaxe do comando é input ("mensagem")
nome = input("digite o seu nome: ")
idade = int(input("digite a sua idade: "))

print ("Olá, ",nome, "você tem ",idade, "anos")
# O comando type () analisa o tipo da informação que está entre os parênteses
print ("O tipo da variável nome é" ,type(nome))
print ("O tipo da variável idade é" ,type(idade))

if idade >= 18:
    print ("você é maior de idade.")
else:
    print ("você é menor de idade")