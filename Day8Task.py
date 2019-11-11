# bikin half pyramid
def bintang(x):
    star = ''
    for i in range(x):
        star += ' * '
        print(star)

bintang(5)

# bikin inverted half pyramid
def rStar(x):
    star = ''
    for i in range(x):
        star = ' * ' * (x - i)
        print(star)

rStar(5)

# bikin half pyramid tapi angka
def pirAng (x):
    angka = ''
    for i in range(x):
        angka += str(i+1) + ' '
        print(angka)

pirAng(5)

# bikin inverted half pyramid angka
def rPirAng(x):
    k = x
    angka = ''
    angku = angka
    for i in range(x):
        for j in range(k):
            if j == (x-i):
                break
            angka += str(j+1)
        print(angka)
        angka = angku

rPirAng(7)

# bikin half pyramid angka berulang
def pirAngUl (x):
    angka = ''
    for i in range(x):
        angka = str(i+1) * (i+1)
        print(angka)

pirAngUl(5)

# bikin inverted half pyramid angka berulang
def rPirAngUl (x):
    angka = ''
    for i in range(x):
        angka = str(i+1) * (x - i)
        print(angka)

rPirAngUl(5)

# bikin half pyramid inverted angka
def PirRAng (x):
    angka = ''
    for i in range(x):
        angka += str(x - i) + ' '
        print(angka)

PirRAng(5)

# bikin inverted half pyramid inverted angka
def rPirRAng(x):
    k = x
    angka = ''
    angku = angka
    for i in range(x):
        for j in range(k):
            if j == (x-i):
                break
            angka += str(x - j)
        print(angka)
        angka = angku

rPirRAng(5)