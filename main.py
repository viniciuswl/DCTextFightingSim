import random
batmanHP = 100
supermanHP = 100
while True:

    r = int(input("Digite 1 para atacar e 2 para sair: \n"))
    if r == 1:
        number = random.randint(1,20)
        number2 = random.randint(1,20)
        if number >= 1 and number <= 5:
            batmanDamage = 5
            batmanHP = batmanHP - batmanDamage
            print("Seu super-sopro foi pouco efetivo.")
            print("Batman sofreu apenas 5 de dano.")
            print("HP do Batman" , batmanHP,". \n" )
            input()

        elif number >= 6 and number <= 10:
            batmanDamage = 10
            batmanHP = batmanHP - batmanDamage
            print("Sua visão de raio laser foi de efetividade média.")
            print("Batman sofreu 10 de dano.")
            print("HP do Batman" , batmanHP,".\n")
            input()
        elif number >= 11 and number <= 15:
            batmanDamage = 15
            batmanHP = batmanHP - batmanDamage
            print("Seu super soco foi bastante efetivo.")
            print("Batman sofreu 15 de dano.")
            print("HP do Batman" , batmanHP ,".\n")
            input()
        elif number >= 16 and number <= 20:
            batmanDamage = 20
            batmanHP = batmanHP - batmanDamage
            print("A visão de laser foi extremamente efetiva.")
            print("Batman sofreu 20 de dano.")
            print("HP do Batman" , batmanHP ,". \n")
            input()


        if number2 >= 1 and number2 <= 5:
            supermanDamage = 5
            supermanHP = supermanHP - supermanDamage
            print("O batarang do Batman foi pouco efetivo.")
            print("Você sofreu apenas 5 de dano.")
            print("HP do Superman (Jogador 1)" , supermanHP,".")
        elif number2 >= 6 and number2 <= 10:
            supermanDamage = 10
            supermanHP = supermanHP - supermanDamage
            print("o soco da armadura de metal do Batman foi de efetividade média.")
            print("Você sofreu 10 de dano.")
            print("HP do Superman (Jogador 1)" , supermanHP,".")
        elif number2 >= 11 and number2 <= 15:
            supermanDamage = 15
            supermanHP = supermanHP - supermanDamage
            print("O explosivo de kriptonita do Batman foi bastante efetivo.")
            print("Você sofreu 15 de dano.")
            print("HP do Superman (Jogador 1)" , supermanHP ,".")
        elif number2 >= 16 and number2 <= 20:
            supermanDamage = 20
            supermanHP = supermanHP - supermanDamage
            print("A bazuca de kriptonita do Batman foi bastante efetiva.")
            print("Você sofreu 20 de dano.")
            print("HP do Superman (Jogador 1)" , supermanHP ,".")
        if batmanHP <= 0:
            print("Superman Wins!")
            break
        if supermanHP <= 0:
            print("Batman Wins!")
            break
    elif r == 2:
        break
