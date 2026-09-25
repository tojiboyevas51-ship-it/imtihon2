def ikkilantir(sonlar):
    natija = []
    
    # Har bir elementni 2 ga ko'paytirish
    for son in sonlar:
        natija.append(son * 2)
    return natija


javob = ikkilantir([1,2,3])
print(javob)
