# Egzersiz öneri ve aktivite hesaplama modülü burada geliştirilecek.
def egzersiz_onerisi(gelir, spor_gecmisi, egzersiz_tercihi, egzersiz_hedefi):
    if gelir == "Düşük":
        ortam = "Ev / Açık Alan"
        ana_oneriler = [
            "30 dk tempolu yürüyüş",
            "20 dk ev egzersizi",
            "15 dk squat + lunge + plank",
            "YouTube üzerinden ücretsiz pilates"
        ]
    elif gelir == "Orta":
        ortam = "Ev + Spor Salonu"
        ana_oneriler = [
            "40 dk fitness",
            "30 dk koşu bandı + ağırlık",
            "Pilates veya grup dersi",
            "Yürüyüş + salon kombinasyonu"
        ]
    else:
        ortam = "Premium / Özel Spor Seçenekleri"
        ana_oneriler = [
            "Yüzme",
            "Tenis",
            "Reformer pilates",
            "Kişisel antrenör eşliğinde fitness"
        ]

    if egzersiz_hedefi == "Yağ Kaybı":
        sure = "30-45 dk"
    elif egzersiz_hedefi == "Sıkılaşma":
        sure = "30-50 dk"
    elif egzersiz_hedefi == "Kondisyon":
        sure = "25-40 dk"
    else:
        sure = "45-60 dk"

    if spor_gecmisi == "Hiç Yok":
        seviye_notu = "Başlangıç seviyesi önerilir. Düşük yoğunlukla başla."
    elif spor_gecmisi == "Başlangıç":
        seviye_notu = "Orta-düşük yoğunluk uygun."
    elif spor_gecmisi == "Orta":
        seviye_notu = "Orta yoğunluk uygun."
    else:
        seviye_notu = "Daha yoğun antrenmanlar yapılabilir."

    ogun_sonrasi = {
        "Kahvaltı": "Kahvaltıdan 30-60 dk sonra 10-20 dk yürüyüş iyi gider.",
        "Öğle": "Öğleden sonra 10-15 dk hafif yürüyüş önerilir.",
        "Akşam": "Akşam yemeğinden sonra hafif yürüyüş veya esneme yap.",
        "Ana Antrenman": "Ana antrenmanı yemekten en az 1.5-2 saat sonra yap."
    }

    return {
        "ortam": ortam,
        "oneriler": ana_oneriler,
        "sure": sure,
        "seviye_notu": seviye_notu,
        "ogun_sonrasi": ogun_sonrasi
    }


def adim_kalorisi(adim):
    return round(adim * 0.04)