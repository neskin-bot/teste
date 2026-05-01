print("|---------------------|")
print("|     Calculadora     |")
print("|---------------------|")
print()
print(" Essa calculadora, faz todas as operações")
print("a partir da dois numeros que você informar")
print()

print("Digite o valor correspondente ao calculo")
print("que você quer fazer")
print()
print("1 - As 4 operações")
print("2 - Média de 3 valores")
print("3 - Fórmula de Bháskara")
print()

opcao = int(input("Digite a opção: "))

match opcao: 
    case 1:
        first_num = float(input("Digite o primeiro numero: "))
        second_num = float(input("Digite o segundo numero: "))

        adicao = first_num + second_num
        subtracao = first_num - second_num
        multi = first_num * second_num

        print()
        print("A adição resulta em:" ,adicao)
        print("A subtração resulta em:",subtracao)
        print("A multiplicação resulta em:",multi)

        if second_num != 0:
            divisao = first_num / second_num
            print(f"A divisão resulta em {divisao}")
        else:
            print("A divisão não pode ser feita")
        print()

        print("4 operações")
    case 2:
        media1 = float(input("Digite a primeiro numero: "))
        media2 = float(input("Digite a segundo numero: "))
        media3 = float(input("Digite a terceiro numero: "))

        media = (media1+media2+media3)/3
        print(f"A média é {media}")

        print("Média de 3 valores")
    case 3:
        print("Fórmula de Bhaáskara")