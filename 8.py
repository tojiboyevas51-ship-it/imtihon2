def absolyutlar(sonlar):
    royxat = []

    # Har bir sonning absolyut qiymatidan iborat yaangi ro'yxat qaytarish
    for son in sonlar:
        if son < 0:
            son *= -1
            royxat.append(son)

    return royxat

natija = absolyutlar([-3, -2, -1])
print(natija)