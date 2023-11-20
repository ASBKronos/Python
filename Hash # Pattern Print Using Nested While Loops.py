x = int(input("How Many '#'s in one line?: "))
y = int(input("How Many lines/rows do you need to print?: "))
rows = 1

while rows <= y:
    columns = 1
    while columns<=x:
        print('#',end = " ")
        columns+=1
    rows+=1
    print()