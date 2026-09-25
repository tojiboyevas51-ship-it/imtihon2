def qiymatlar_yigindisi(lugat):
    sum = 0

    # Dictionaryda barcha qiymatlar yigindisini hisoblash
    for kalit, qiymat in lugat.items():
        sum = sum + qiymat

    return sum

natija = qiymatlar_yigindisi({"a": 1, "b": 2, "c": 3})
print(natija)