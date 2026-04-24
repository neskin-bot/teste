# Pedir 3 notas e armazenar em variáveis
turma = input ("Digite a sua turma: ")
nome = input ("Digite o seu nome: ")

nota_portugues = int(input ("digite a sua nota em português: "))
nota_matematica = int(input ("digite a sua nota em matematica: "))
nota_ciencias = int(input ("digite a sua nota em ciencias: "))

soma = nota_portugues + nota_matematica + nota_ciencias
media = soma/3

print("A média das notas é",media)

if media >=7:
    print ("parabéns",nome,"do",turma,",você foi aprovado")
else:
    print (nome,"do",turma,",você foi reprovado")