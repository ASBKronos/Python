from numpy import *

r1 = int(input("Enter the number of rows you want in matrix 1: "))
c1 = int(input("Enter the number of columns you want in matrix 1: "))
arr1 = zeros((r1,c1))

r2 = int(input("Enter the number of rows you want in matrix 2: "))
c2 = int(input("Enter the number of columns you want in matrix 2: "))
arr2 = zeros((r2,c2))

if c1 != r2:
    print("Matrix multiplication not possible as columns in matrix 1 are not equal to rows in matrix 2")

else:
    for i in range(r1):
        for j in range(c1):
            x = int(input(f"Enter element {j+1} of row {i+1} in Matrix 1 "))
            arr1[i][j] = x

    for i in range(r2):
        for j in range(c2):
            x = int(input(f"Enter element {j+1} of row {i+1} in Matrix 2 "))
            arr2[i][j] = x

print(arr1)
print(arr2)
arr3 = zeros((r1,c2))
print("The Matrix Product is: ")

for i in range(r1):
    for j in range(c2):
        for k in range(c1):
            arr3[i][j] += arr1[i][k] * arr2[k][j]

print(arr3)
print("With using the MatMul function of NumPy: ")
print(matmul(arr1,arr2))
print("With using the Dot function of NumPy: ")
print(dot(arr1,arr2))