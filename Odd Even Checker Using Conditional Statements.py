#To Check if a given number is even or odd

while True:

    x = int(input("Enter a number: "))
    if x < 0:
        print("Enter a positive value")
    elif x%2 ==0:
        print("Number is Even")
    else:
        print("number is Odd")
    choice = str.lower(input("Do you want to enter another number(y/n): ")[0])
    if choice == 'n':
        break
    else:
        continue
