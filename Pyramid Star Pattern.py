rows = int(input("How many rows do you want in the pyramid?"))


for i in range(0,rows):
    for j in range(rows,i,-1):
        print(" ",end='')
    print('* '*((i+1)),end="")
    for k in range(rows,i,-1):
        print(" ",end="")
    print()

