import random
number = str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))
if number[0] == number[1] or number[1] == number[2] or number[0]==number[2]:
    number = str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))

print(number)
    #print(number)

print("Let's see if you can guss my 3 digit code. \nCode has been generated, please guess a 3 digit code")

while True:
    gs = input("Please enter your guess here: ")
    jeden=gs[0]
    dwa=gs[1]
    trzy=gs[2]
    w=0
    n=0

    if gs==number :
        print(("that's right the number was {},\nyou won!").format(number))
        break

    if jeden==number[0]:
        print("Match")
        n+=1
    elif jeden == number[1] or jeden == number[2]:
        print("Close")
        n+=1

    if dwa==number[1]:
        print("Match")
        n+=1
    elif dwa == number[0] or dwa == number[2]:
        print("Close")
        n+=1

    if trzy==number[2]:
        print("Match")
        n+=1
    elif trzy == number[1] or trzy == number[0]:
        print("Close")
        n+=1
    if n== 0:
        print("None")
