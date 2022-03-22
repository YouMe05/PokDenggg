import random

numstar = random.randint(1,4)
numstar2 = random.randint(1,4)
num = random.randint(1,12)
num2 = random.randint(1,12)

numbot = random.randint(1,12)
numbot2 = random.randint(1,12)

if numstar == 1:
    star= "♠"
elif numstar == 2:
    star= "♥"
elif numstar == 3:
    star= "♣"
elif numstar == 4:
    star= "♦"
if numstar2 == 1:
    star2= "♠"
elif numstar2 == 2:
    star2= "♥"
elif numstar2 == 3:
    star2= "♣"
elif numstar2 == 4:
    star2= "♦"


if num == 10:
    numR = "J"
    num = 0
elif num == 11:
    numR = "Q"
    num = 0
elif num == 12:
    numR = "K"
    num = 0

if num2 == 10:
    num2R = "J"
    num2 = 0
elif num2 == 11:
    num2R = "Q"
    num2 = 0
elif num2 == 12:
    num2R = "K"
    num2 = 0


if numbot == 10:
    botR = "J"
    numbot = 0
elif numbot == 11:
    botR = "Q"
    numbot = 0
elif numbot == 12:
    botR = "K"
    numbot = 0

if numbot2 == 10:
    bot2R = "J"
    numbot2 = 0
elif numbot2 == 11:
    bot2R = "Q"
    numbot2 = 0
elif numbot2 == 12:
    bot2R = "K"
    numbot2 = 0

Mypoin = num + num2
Botpoin = numbot + numbot2

if 0 <numbot < 10  and 0 < numbot2 < 10 :
    BotpoinN = Botpoin
    if BotpoinN >= 10:
        BotpoinN = BotpoinN - 10
elif 0 < numbot < 10 and (bot2R == "J" or bot2R == "Q" or bot2R == "K"):
    BotpoinN = Botpoin
    if BotpoinN >= 10:
        BotpoinN = BotpoinN - 10
elif 0 < numbot2 < 10 and (botR == "J" or botR == "Q" or botR == "K"):
    BotpoinN = Botpoin
    if BotpoinN >= 10:
        BotpoinN = Botpoin - 10
elif botR == "J" and bot2R == "J":
    BotpoinN = Botpoin
    if BotpoinN >= 10:
        BotpoinN = BotpoinN - 10
elif botR == "J" and bot2R == "Q":
    BotpoinN = Botpoin
    if BotpoinN >= 10:
        BotpoinN = BotpoinN - 10
elif botR == "J" and bot2R == "K":
    BotpoinN = Botpoin
    if BotpoinN >= 10:
        BotpoinN = BotpoinN - 10

if 0 < num < 10 and 0 < num2 < 10 :
    print ("Your card is:", num, star)
    print ("Your card is:", num2, star2)
    Mypoin = Mypoin
    if Mypoin >= 10:
        Mypoin = Mypoin - 10
        print ("Your point is:", Mypoin)
    else:
        print ("Your point is:", Mypoin)
elif 0 < num < 10 and (num2R == "J" or num2R == "Q" or num2R == "K"):
    print ("Your card is:", num, star)
    print ("Your card is:", num2R)
    Mypoin = Mypoin
    if Mypoin >= 10:
        Mypoin = Mypoin - 10
        print ("Your point is:", Mypoin)
    else:
        print ("Your point is:", Mypoin)
elif 0 < num2 < 10 and (numR == "J" or numR == "Q" or numR == "K"):
    print ("Your card is:", numR, star)
    print ("Your card is:", numR)
    Mypoin = Mypoin
    if Mypoin >= 10:
        Mypoin = Mypoin - 10
        print ("Your point is:", Mypoin)
    else:
        print ("Your point is:", Mypoin)
elif numR == "J" and num2R == "J":
    print ("Your card is:", numR)
    print ("Your card is:", num2R)
    Mypoin = Mypoin
    if Mypoin >= 10:
        Mypoin = Mypoin - 10
        print ("Your point is:", Mypoin)
    else:
        print ("Your point is:", Mypoin)
elif numR == "J" and num2R == "Q":
    print ("Your card is:", numR)
    print ("Your card is:", num2R)
    Mypoin = Mypoin
    if Mypoin >= 10:
        Mypoin = Mypoin - 10
        print ("Your point is:", Mypoin)
    else:
        print ("Your point is:", Mypoin)
elif numR == "J" and num2R == "K":
    print ("Your card is:", numR)
    print ("Your card is:", num2R)
    Mypoin = Mypoin
    if Mypoin >= 10:
        Mypoin = Mypoin - 10
        print ("Your point is:", Mypoin)
    else:
        print ("Your point is:", Mypoin)
Question = input("Do you want to continue? (y/n)")
if Question == "y":
    J = random.randint(1,12)
    J2 = random.randint(1,4)
    if J2 == 1:
        JE= "♠"
    elif J2 == 2:
        JE= "♥"
    elif J2 == 3:
        JE= "♣"
    elif J2 == 4:
        JE= "♦"
    if J == 10:
        J1E = "J"
        J = 0
    elif J == 11:
        J1E = "Q"
        J = 0
    elif J == 12:
        J1E = "K"
        J = 0
    if 0 < J < 10 :
        print ("Your card is:", J, JE)
        Mypoin = Mypoin + J
        if Mypoin >= 10:
            Mypoin = Mypoin - 10
            if Mypoin > BotpoinN:
                print ("Your point is:", Mypoin)
                if Mypoin > BotpoinN:
                    print("You win!")
                elif Mypoin < BotpoinN:
                    print("You lose!")
                else:
                    print("Draw!")
        else:
            print ("Your point is:", Mypoin)
            if Mypoin > BotpoinN:
                print("You win!")
            elif Mypoin < BotpoinN:
                print("You lose!")
            else:
                print("Draw!")
    elif J1E == "J" or J1E == "Q" or J1E == "K":
        print ("Your card is:", J1E)
        Mypoin = Mypoin + J
        if Mypoin >= 10:
            Mypoin = Mypoin - 10
            print ("Your point is:", Mypoin)
            if Mypoin > BotpoinN:
                print("You win!")
            elif Mypoin < BotpoinN:
                print("You lose!")
            else:
                print("Draw!")
        else:
            print ("Your point is:", Mypoin)
            if Mypoin > BotpoinN:
                print("You win!")
            elif Mypoin < BotpoinN:
                print("You lose!")
            else:
                print("Draw!")
elif Question == "n":
    if Mypoin > BotpoinN:
        print("You win!")
    elif Mypoin < BotpoinN:
        print("You lose!")
    else:
        print("Draw!")
print("Bot point is:", BotpoinN)
