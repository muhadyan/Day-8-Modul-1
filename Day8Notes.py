'''
# looping list di dalem list menggunakan
x = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for i in x:
    for j in i:
        print(j)

for i in range(5):
    for j in range(7,9):
        print(i, 'dan', j)

# bikin function pangkat
def pangkat(x, y):
    k = x
    for i in range(y-1):
        x *= k
    print(x)

pangkat(12, 2)

# bikin function factorial
def faktorial(x):
    angka = 1
    for i in range(1, x+1):
        angka *= i
    print(angka)

faktorial(3)



# REKURSIF FUNCTION
def faktorial2(x):
    if x <= 2:
        return x
    else:
        return x * faktorial2(x-1)      # fungsinya memanggil diri sendiri

print(faktorial2(4))
'''