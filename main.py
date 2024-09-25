#  we will be implimanting 

import random

#         1 for snake
#         -1 for water
#         0 for gut 

computer = random.choice([1,-1,0])

youstr = input("Enter your choice : ")

youDic ={"s":1, "w":-1,"g": 0}
reverseDic = {1 : "snake",-1: "water",0 :"gun"}

you = youDic[youstr]


print(f"you chose {reverseDic[you]}\n Computer chose {reverseDic[computer]}")


if (computer == you):
    print("its a draw")

else:
        if (computer == -1 and you == 1):
            print("you win")

        elif (computer == -1 and you == 0):
            print("you lose ")


        elif (computer == 1 and you == -1):
            print("you lose")

        elif (computer == 1 and you == 0):
            print("you win ")

        elif (computer == 0 and you == -1):
            print("you win")

        elif (computer == 0  and you == 1):
            print("you lose ")
        else:
            print("somting went wrong")



