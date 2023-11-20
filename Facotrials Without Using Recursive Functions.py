number = int(input("Enter the number: "))
factorial = 1

for i in range(number,1,-1):
    factorial = factorial * number
    number-=1

print(f"The factorial of {number} is {factorial}")