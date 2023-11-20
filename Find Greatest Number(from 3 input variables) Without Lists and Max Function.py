x = int(input("Enter a number: "))
y = int(input("Enter the second number: "))
z = int(input("Enter the third number: "))

if x > y and x > z:
    print(f"{x} is the greatest numbers")

elif y > x and y > z:
    print(f"{y} is the greatest numbers")

else:
    print(f"{z} is the greatest numbers")