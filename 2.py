def kopaytma(sonlar):
    kopaytma = 1

    # Barcha sonlarning kopaytmasini hisoblash
    for son in sonlar:
        kopaytma = kopaytma * son
    
    return kopaytma

natija = kopaytma([1,2,3,4])
print(natija)