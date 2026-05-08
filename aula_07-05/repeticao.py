import time
import random

print("### Jogo da advinhação ###")
print()
print("Estou pensando em um número. . .")

time.sleep(2)

numero = random.randint(0, 10)

print("Pensei!")
print("Você poderá tentar advinhar ele")
print()

# para i em um intervalo de 1 até 4, ou seja, o usuário terá 3 tentativas para advinhar o número

#for i in range(1,4):
#    print(f"Essa é a sua {i} tentativa")
#   tentativa =int(input("Digite um valor de 0 a 10: "))
#
#    if tentativa == numero:
#        print("Parabéns, você acertou")
#    else:
#        print("Você errou!")

acertou = False
num_tentativa = 0
# enquanto acertou for false. . .
while acertou == False:
    num_tentativa += 1 # mesma coisa que num_tentativa = num_tentativa + 1
    print(f"Essa é a sua {num_tentativa} tentativa")
    tentativa =int(input("Digite um valor de 0 a 10: "))

    if tentativa == numero:
        print("Parabéns, você acertou")
        acertou = True
    else:
        print("Você errou!")
        if num_tentativa == 10:
            print("Se é burro né man?")