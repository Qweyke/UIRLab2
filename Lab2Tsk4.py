n = int(input("Введите размер матрицы A\n"))
A = []
number = 1
for i in range(n):
    row = []
    for j in range(n):
        if i % 2 == 0:
            row.append(number)
            number += 1
        else:
            row.insert(0, number)
            number += 1
    A.append(row)

for i in range(n):
    for j in range(n):
        print(A[i][j], end=", ")
    print()
print()
B = []
for row in A:
    B.append(row + row[::-1])
for row in B:
    print(row)
print()
C = B + B[::-1]
for row in C:
    print(row)
