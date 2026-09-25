try:
    a = int(input())
    b = int(input())

    c = a / b

except ZeroDivisionError:
    print("Nolga bo'lish mumkin emas!")

except:
    print("Xatolik: Boshqa xatolik yuz berdi!")