count = 0

while True:

    number = int(input("Enter a number to check for prime: "))

    if number == 0 or number == 1:
        print("Number Not Prime")
        continue

    elif number < 0:
        print("Enter a Positive Number")
        continue

    else:
        for i in range(2, number):
            if (number % i) == 0:
                count += 1

    if count > 0:
        print("Not a Prime")
        continue
    else:
        print("Prime Number Found!")
        continue

