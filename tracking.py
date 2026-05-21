# Günlük su, uyku, adım, egzersiz ve yemek takibi burada geliştirilecek.
def gunluk_puanla(hedef_kalori, alinan_kalori, su, uyku):
    fark = abs(hedef_kalori - alinan_kalori)

    puan = 0

    if fark <= 150:
        puan += 2
    elif fark <= 300:
        puan += 1

    if su >= 2:
        puan += 1

    if uyku >= 7:
        puan += 1

    if puan <= 0:
        return "Çok Kötü"
    elif puan == 1:
        return "Kötü"
    elif puan == 2:
        return "Orta"
    elif puan == 3:
        return "İyi"
    return "Çok İyi"


def su_uyarisi(su):
    if su < 1.5:
        return "Su tüketimin düşük. Daha fazla su iç."
    return "Su tüketimin fena değil."


def uyku_uyarisi(uyku):
    if uyku < 6:
        return "Uyku süren yetersiz. Daha fazla uyumaya çalış."
    return "Uyku süren fena değil."