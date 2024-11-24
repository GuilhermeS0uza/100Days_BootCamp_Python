print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Bem vindo a Caça de tesouro!")
print("Sua missão é encontrar o tesouro\n")
escolha1 = input('Você está em uma encruzilhada. Para onde você quer ir?\n'
                'Escreva "Esquerda" ou "Direita".\n').lower()
if escolha1 == 'esquerda':
    escolha2 = input('Você chegou a um lago.. '
                    'Há uma ilha no meio do lago.\n '
                    'Digite "esperar" para esperar por um barco. '
                    'Digite "nadar" para atravessar o lago nadando. \n').lower()
    if escolha2 == 'esperar':
        escolha3 = input('Você chegou a ilha inleso '
                    'Ai você avista uma casa com 3 portas para entrar na casa você precisa escolher em qual porta você vai entrar.\n '
                    'Tem uma porta vermelha, amarela e azul.\n'
                    'Em qual porta você ira entrar? Vermelha, amarela ou azul? \n').lower()
        if escolha3 == 'vermelha':
            print("Você foi passar pela porta vermelha e acabou caindo em uma armadilha. Game Over")
        elif escolha3 == 'azul':
            print("Você caiu em uma sala cheia de tubarões. Game Over")
        elif escolha3 == 'amarela':
            print("Você encontrou o tesouro. Good Job!")
        else:
            print("Você escolheu uma porta que não existe. Game Over")
    else:
        print("Você foi atacado por crocodilos. Game Over")
else:
    print("Você caiu em um buraco. Game Over.")

