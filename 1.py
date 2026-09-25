def musbat_yigindisi(sonlar):
    yigindi = 0

    # Musbat sonlar yig'indisini hisoblash
    for son in sonlar:
        if son > 0:
            yigindi += son

    return yigindi

natija = musbat_yigindisi([1,-2,3,-4,5])
print(natija)