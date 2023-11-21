def fibo(n):
    if n < 0:
        print("Enter a positive number")
    elif n == 1:
        print(0)
    elif n == 2:
        print(0)
        print(1)
    else:
        first = 0
        print(first)
        second = 1
        print(second)
        for i in range(n-2):
            third = first + second
            first = second
            second = third
            print(third)




while True:

    num = int(input("Enter the number of digits in the fibonacci sequence you need to display: "))
    fibo(num)
    choice = str.lower(input("Do you want to enter another number (y/n)?"))[0]

    if choice == 'y':
        continue
    else:
        print("Thank You! Bye!")
        break
