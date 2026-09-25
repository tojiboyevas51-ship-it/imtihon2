def raqamlar_soni(matn):
    sum = 0

    # Matn ichidan raqamlar sonini topish
    for son in matn:
        if son.isdigit():       # isdigit() faqat raqamlarni oladi
             sum += 1
    return sum

natija = raqamlar_soni(("abc123"))
print(natija)