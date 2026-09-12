import heapq
from collections import Counter

from meals import alerji_eslet, ogun_onerisi


def bmi_hesapla(kilo, boy):
    # boy cm geliyor, metreye çeviriyoruz
    boy_m = boy / 100
    return round(kilo / (boy_m ** 2), 2)


def bmi_durumu(bmi):
    if bmi < 18.5:
        return "Zayıf"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Fazla Kilolu"
    return "Obez"


def kalori_hesapla(cinsiyet, kilo, boy, yas, aktivite, hedef):
    # BMR hesabı
    if cinsiyet == "Erkek":
        bmr = 10 * kilo + 6.25 * boy - 5 * yas + 5
    else:
        bmr = 10 * kilo + 6.25 * boy - 5 * yas - 161

    # günlük hareket katsayısı
    katsayi = {
        "Çok Düşük": 1.2,
        "Düşük": 1.375,
        "Orta": 1.55,
        "Yüksek": 1.725
    }

    kalori = bmr * katsayi[aktivite]

    # hedefe göre kalori ayarı
    if hedef == "Kilo Vermek":
        kalori -= 400
    elif hedef == "Kilo Almak":
        kalori += 300

    return round(kalori)


def makro_stratejisi(hedef):
    if hedef == "Kilo Vermek":
        return {
            "tip": "Düşük-Orta Carb",
            "protein": "%35",
            "karbonhidrat": "%35",
            "yag": "%30"
        }
    elif hedef == "Kilo Almak":
        return {
            "tip": "Yüksek Carb",
            "protein": "%25",
            "karbonhidrat": "%50",
            "yag": "%25"
        }
    else:
        return {
            "tip": "Dengeli",
            "protein": "%30",
            "karbonhidrat": "%40",
            "yag": "%30"
        }


def filtrele_ogunler(ogunler, alerjiler, sevilmeyenler):
    # boşlukları temizle
    alerjiler = [x.strip().lower() for x in alerjiler if x.strip()]
    sevilmeyenler = [x.strip().lower() for x in sevilmeyenler if x.strip()]

    # örn: gluten -> ekmek, makarna vs genişlet
    genis_alerjiler = alerji_eslet(alerjiler)

    sonuc = []

    for item in ogunler:
        ad = item["ad"].lower()
        etiketler = [e.lower() for e in item.get("etiketler", [])]

        uygun = True

        # alerji kontrolü
        for alerji in genis_alerjiler:
            if alerji in ad or alerji in etiketler:
                uygun = False
                break

        # sevilmeyen kontrolü
        if uygun:
            for sevmedigi in sevilmeyenler:
                if sevmedigi in ad or sevmedigi in etiketler:
                    uygun = False
                    break

        if uygun:
            sonuc.append(item)

    return sonuc


def _kombinasyonlar(kahvalti, ogle, aksam, ara, hedef_kalori):
    """Öğün kombinasyonlarını kalori farklarıyla birlikte üret."""
    for k in kahvalti:
        for o in ogle:
            for a in aksam:
                for ar in ara:
                    toplam = (
                        k["kalori"]
                        + o["kalori"]
                        + a["kalori"]
                        + ar["kalori"]
                    )
                    yield {
                        "kahvalti": k,
                        "ogle": o,
                        "aksam": a,
                        "ara": ar,
                        "toplam": toplam,
                        "hedef": hedef_kalori,
                        "_fark": abs(toplam - hedef_kalori),
                    }


def _imza(kombinasyon):
    return tuple(
        kombinasyon[ogun]["ad"]
        for ogun in ("kahvalti", "ogle", "aksam", "ara")
    )


def haftalik_plan(kahvalti, ogle, aksam, ara, hedef_kalori):
    gunler = [
        "Pazartesi",
        "Salı",
        "Çarşamba",
        "Perşembe",
        "Cuma",
        "Cumartesi",
        "Pazar"
    ]

    if not all((kahvalti, ogle, aksam, ara)):
        return {gun: None for gun in gunler}

    # Tüm seçenekleri belleğe almak yerine kalori hedefine en yakın
    # sınırlı sayıdaki adayı tut.
    adaylar = heapq.nsmallest(
        100,
        _kombinasyonlar(kahvalti, ogle, aksam, ara, hedef_kalori),
        key=lambda secenek: secenek["_fark"],
    )

    kullanim = {
        "kahvalti": Counter(),
        "ogle": Counter(),
        "aksam": Counter(),
        "ara": Counter(),
    }
    kullanilan_kombinasyonlar = set()
    plan = {}

    for gun in gunler:
        benzersiz_adaylar = [
            aday for aday in adaylar
            if _imza(aday) not in kullanilan_kombinasyonlar
        ]
        secim_havuzu = benzersiz_adaylar or adaylar

        def cesitlilik_puani(aday):
            tekrar_sayisi = sum(
                kullanim[ogun][aday[ogun]["ad"]]
                for ogun in ("kahvalti", "ogle", "aksam", "ara")
            )
            # Yaklaşık 50 kcal fark pahasına tekrar eden bir öğün yerine
            # yeni bir öğünü tercih et.
            return aday["_fark"] + (tekrar_sayisi * 50)

        secilen = min(secim_havuzu, key=cesitlilik_puani)
        kullanilan_kombinasyonlar.add(_imza(secilen))

        for ogun in ("kahvalti", "ogle", "aksam", "ara"):
            kullanim[ogun][secilen[ogun]["ad"]] += 1

        # İç hesaplama alanını arayüze göndermiyoruz.
        plan[gun] = {
            anahtar: deger
            for anahtar, deger in secilen.items()
            if anahtar != "_fark"
        }

    return plan
