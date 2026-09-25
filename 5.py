def manfiylar_son(sonlar):
    royxat  = []

    # Manfiy sonlardan iborat yangi ro'yxat tuzish
    for son in sonlar:
        if son < 0:
            royxat.append(son)
    return royxat


natija = manfiylar_son([3,-1,0,-7])
print(natija)