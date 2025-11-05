             #   *
             #
             #  * *
             #
             # *   *
             #
             #  * *
             #
             #   *

t = 0
for i in range (1,6):

    if i % 2 ==0:
        print()

    else:
        t+=1
        # for j in range (4-t,0,-1):
        j = 4-t
        for k in range (1,7):
            if k == j or k == 6-j:
                print("*",end="")
            elif k != 6:
                print(end=" ")
            else:
                print("")
t=0

for i in range (6,10):
    if i % 2 ==0:
        print()

    else:
        t+=1
        j = 1+t
        for k in range (1,7):
            if k == j or k == 6-j:
                print("*",end="")
            elif k != 6:
                print(end=" ")
            else:
                print("")





