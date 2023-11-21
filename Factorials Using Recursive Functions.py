def fibo(n):
    if n == 1 or n == 0:
        return 1
    elif n < 0:
        print("Enter a positive number")
    else:
        return n * fibo(n-1)


while True:

    num = int(input("Enter the number who's factorial you require: "))
    x = fibo(num)
    print(f"The factorial of {num} is : {x}")
    choice = str.lower(input("Do you want to enter another number (y/n)?"))[0]

    if choice == 'y':
        continue
    else:
        print("Thank You! Bye!")
        break
