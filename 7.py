def faktorial(n):
    kopaytma = 1

    # Faktorialni hisoblash
    for i in range(1, n + 1):
        kopaytma = kopaytma * i

    return kopaytma 

natija = faktorial((5))
print(natija)