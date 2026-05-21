# meals.py

def alerji_eslet(alerji_listesi):
    esleme = {
        "gluten": ["ekmek", "tost", "makarna", "bulgur", "wrap", "börek", "sandviç"],
        "laktoz": ["yoğurt", "ayran", "peynir", "lor", "kefir", "süt", "hellim", "cacık"],
        "sut": ["yoğurt", "ayran", "peynir", "lor", "kefir", "süt", "hellim", "cacık"],
        "süt": ["yoğurt", "ayran", "peynir", "lor", "kefir", "süt", "hellim", "cacık"],
        "yumurta": ["yumurta", "omlet", "menemen"],
        "fıstık": ["fıstık", "fıstık ezmesi"],
        "yer fıstığı": ["fıstık", "fıstık ezmesi"],
        "ceviz": ["ceviz"],
        "badem": ["badem"],
        "balık": ["balık", "somon", "ton balığı", "karides"],
        "deniz ürünü": ["balık", "somon", "ton balığı", "karides"],
        "ton balığı": ["ton balığı"],
        "avokado": ["avokado"]
    }

    genisletilmis = []

    for alerji in alerji_listesi:
        a = alerji.strip().lower()
        if a:
            genisletilmis.append(a)
            if a in esleme:
                genisletilmis.extend(esleme[a])

    return list(set(genisletilmis))


def ogun_onerisi(beslenme_tipi, gelir):
    if beslenme_tipi == "Vegan":
        kahvalti = [
            {"ad": "Yulaf + bitkisel süt + muz", "kalori": 350, "etiketler": ["yulaf", "muz"]},
            {"ad": "Avokadolu tam buğday tost", "kalori": 380, "etiketler": ["avokado", "ekmek"]},
            {"ad": "Fıstık ezmeli yulaf kasesi", "kalori": 400, "etiketler": ["fıstık", "yulaf"]},
            {"ad": "Chia puding + meyve", "kalori": 320, "etiketler": ["chia", "meyve"]},
            {"ad": "Humuslu sandviç", "kalori": 360, "etiketler": ["humus", "ekmek"]},
            {"ad": "Meyveli granola bowl", "kalori": 390, "etiketler": ["meyve", "granola"]},
            {"ad": "Tofulu sebzeli tost", "kalori": 370, "etiketler": ["tofu", "sebze", "ekmek"]},
            {"ad": "Muzlu smoothie bowl", "kalori": 340, "etiketler": ["muz", "meyve"]},
            {"ad": "Tahinli yulaf lapası", "kalori": 360, "etiketler": ["tahin", "yulaf"]},
            {"ad": "Nohut unlu omlet", "kalori": 330, "etiketler": ["nohut"]},
            {"ad": "Avokado + domates tabağı", "kalori": 300, "etiketler": ["avokado", "domates"]},
            {"ad": "Kuru meyveli yulaf", "kalori": 370, "etiketler": ["yulaf", "meyve"]},
            {"ad": "Bitkisel yoğurt + çilek", "kalori": 290, "etiketler": ["yoğurt", "çilek"]},
            {"ad": "Sebzeli tofu scramble", "kalori": 350, "etiketler": ["tofu", "sebze"]},
            {"ad": "Elmalı tarçınlı yulaf", "kalori": 340, "etiketler": ["elma", "yulaf"]},
            {"ad": "Humus + salatalık tabağı", "kalori": 280, "etiketler": ["humus", "salatalık"]},
            {"ad": "Bitkisel sütlü granola", "kalori": 360, "etiketler": ["süt", "granola"]},
            {"ad": "Meyveli chia bowl", "kalori": 310, "etiketler": ["chia", "meyve"]}
        ]

        ogle = [
            {"ad": "Mercimek yemeği + salata", "kalori": 500, "etiketler": ["mercimek", "salata"]},
            {"ad": "Nohutlu sebze yemeği", "kalori": 520, "etiketler": ["nohut", "sebze"]},
            {"ad": "Kinoalı salata", "kalori": 480, "etiketler": ["kinoa", "salata"]},
            {"ad": "Sebzeli wrap", "kalori": 510, "etiketler": ["sebze", "wrap"]},
            {"ad": "Fırın sebze + humus", "kalori": 470, "etiketler": ["sebze", "humus"]},
            {"ad": "Bulgurlu nohut tabağı", "kalori": 530, "etiketler": ["bulgur", "nohut"]},
            {"ad": "Tofulu sebze bowl", "kalori": 500, "etiketler": ["tofu", "sebze"]},
            {"ad": "Mercimek çorbası + avokado salata", "kalori": 450, "etiketler": ["mercimek", "avokado", "salata"]},
            {"ad": "Kinoa + nohut bowl", "kalori": 490, "etiketler": ["kinoa", "nohut"]},
            {"ad": "Sebzeli pirinç noodle", "kalori": 500, "etiketler": ["pirinç", "sebze"]},
            {"ad": "Falafel + salata", "kalori": 520, "etiketler": ["falafel", "salata"]},
            {"ad": "Humuslu kinoa tabağı", "kalori": 470, "etiketler": ["humus", "kinoa"]},
            {"ad": "Barbunya + salata", "kalori": 460, "etiketler": ["barbunya", "salata"]},
            {"ad": "Zeytinyağlı sebze tabağı", "kalori": 430, "etiketler": ["sebze"]},
            {"ad": "Patatesli nohut sote", "kalori": 510, "etiketler": ["patates", "nohut"]},
            {"ad": "Mercimek köftesi + yeşillik", "kalori": 450, "etiketler": ["mercimek", "salata"]},
            {"ad": "Kinoalı sebze bowl", "kalori": 480, "etiketler": ["kinoa", "sebze"]},
            {"ad": "Tofulu mantarlı sote", "kalori": 490, "etiketler": ["tofu", "mantar"]}
        ]

        aksam = [
            {"ad": "Sebze çorbası + bakliyat salatası", "kalori": 450, "etiketler": ["sebze", "bakliyat"]},
            {"ad": "Kinoa + ızgara sebze", "kalori": 470, "etiketler": ["kinoa", "sebze"]},
            {"ad": "Mercimek köftesi + salata", "kalori": 430, "etiketler": ["mercimek", "salata"]},
            {"ad": "Zeytinyağlı sebze tabağı", "kalori": 440, "etiketler": ["sebze"]},
            {"ad": "Tofulu sote", "kalori": 480, "etiketler": ["tofu", "sebze"]},
            {"ad": "Domatesli tam buğday makarna", "kalori": 490, "etiketler": ["makarna", "domates"]},
            {"ad": "Sebzeli pirinç noodle", "kalori": 500, "etiketler": ["pirinç", "sebze"]},
            {"ad": "Mantar sote + salata", "kalori": 390, "etiketler": ["mantar", "salata"]},
            {"ad": "Nohutlu salata", "kalori": 420, "etiketler": ["nohut", "salata"]},
            {"ad": "Patatesli sebze fırın", "kalori": 460, "etiketler": ["patates", "sebze"]},
            {"ad": "Humus + köz sebze", "kalori": 410, "etiketler": ["humus", "sebze"]},
            {"ad": "Avokadolu salata bowl", "kalori": 430, "etiketler": ["avokado", "salata"]},
            {"ad": "Mercimek çorbası + salata", "kalori": 380, "etiketler": ["mercimek", "salata"]},
            {"ad": "Kinoalı mantar sote", "kalori": 470, "etiketler": ["kinoa", "mantar"]},
            {"ad": "Sebzeli karabuğday tabağı", "kalori": 450, "etiketler": ["sebze", "karabuğday"]},
            {"ad": "Tofulu brokoli sote", "kalori": 460, "etiketler": ["tofu", "brokoli"]},
            {"ad": "Bakliyat çorbası + salata", "kalori": 400, "etiketler": ["bakliyat", "salata"]},
            {"ad": "Kabızsız sebze bowl", "kalori": 420, "etiketler": ["sebze"]}
        ]

        ara = [
            {"ad": "1 elma + 10 badem", "kalori": 180, "etiketler": ["elma", "badem"]},
            {"ad": "Muz", "kalori": 100, "etiketler": ["muz"]},
            {"ad": "Bitkisel yoğurt", "kalori": 140, "etiketler": ["yoğurt"]},
            {"ad": "Havuç + humus", "kalori": 160, "etiketler": ["havuç", "humus"]},
            {"ad": "Karışık kuruyemiş", "kalori": 190, "etiketler": ["kuruyemiş"]},
            {"ad": "Portakal", "kalori": 90, "etiketler": ["portakal"]},
            {"ad": "2 hurma + ceviz", "kalori": 170, "etiketler": ["hurma", "ceviz"]},
            {"ad": "Elma", "kalori": 80, "etiketler": ["elma"]},
            {"ad": "Mandalina", "kalori": 75, "etiketler": ["mandalina"]},
            {"ad": "Salatalık + limon", "kalori": 40, "etiketler": ["salatalık"]},
            {"ad": "Meyve salatası", "kalori": 120, "etiketler": ["meyve"]},
            {"ad": "Badem", "kalori": 90, "etiketler": ["badem"]},
            {"ad": "Ceviz", "kalori": 100, "etiketler": ["ceviz"]},
            {"ad": "Kuru kayısı", "kalori": 110, "etiketler": ["kayısı"]},
            {"ad": "Bitkisel sütlü smoothie", "kalori": 150, "etiketler": ["süt", "meyve"]},
            {"ad": "Armut", "kalori": 95, "etiketler": ["armut"]},
            {"ad": "Çilek", "kalori": 50, "etiketler": ["çilek"]},
            {"ad": "Muz + tahin", "kalori": 170, "etiketler": ["muz", "tahin"]}
        ]

    elif beslenme_tipi == "Vejetaryen":
        kahvalti = [
            {"ad": "2 haşlanmış yumurta + peynir + domates", "kalori": 360, "etiketler": ["yumurta", "peynir", "domates"]},
            {"ad": "Yulaf + yoğurt + meyve", "kalori": 340, "etiketler": ["yulaf", "yoğurt", "meyve"]},
            {"ad": "Omlet + tam buğday ekmek", "kalori": 390, "etiketler": ["yumurta", "ekmek"]},
            {"ad": "Lor peynirli tost", "kalori": 350, "etiketler": ["lor", "ekmek"]},
            {"ad": "Menemen + ekmek", "kalori": 370, "etiketler": ["yumurta", "domates", "ekmek"]},
            {"ad": "Yoğurtlu granola bowl", "kalori": 380, "etiketler": ["yoğurt", "granola"]},
            {"ad": "Peynirli sandviç", "kalori": 360, "etiketler": ["peynir", "ekmek"]},
            {"ad": "Haşlanmış yumurta + avokado", "kalori": 400, "etiketler": ["yumurta", "avokado"]},
            {"ad": "Muzlu yulaf lapası", "kalori": 350, "etiketler": ["muz", "yulaf"]},
            {"ad": "Kefir + çilek", "kalori": 300, "etiketler": ["kefir", "çilek"]},
            {"ad": "Patatesli omlet", "kalori": 410, "etiketler": ["patates", "yumurta"]},
            {"ad": "Peynir + zeytin tabağı", "kalori": 330, "etiketler": ["peynir", "zeytin"]},
            {"ad": "Yoğurt + muz + badem", "kalori": 340, "etiketler": ["yoğurt", "muz", "badem"]},
            {"ad": "Lor peynirli omlet", "kalori": 370, "etiketler": ["lor", "yumurta"]},
            {"ad": "Ayran + haşlanmış yumurta", "kalori": 280, "etiketler": ["ayran", "yumurta"]},
            {"ad": "Peynirli salata tabağı", "kalori": 300, "etiketler": ["peynir", "salata"]},
            {"ad": "Meyveli yoğurt kasesi", "kalori": 320, "etiketler": ["meyve", "yoğurt"]},
            {"ad": "Sebzeli omlet", "kalori": 360, "etiketler": ["sebze", "yumurta"]}
        ]

        ogle = [
            {"ad": "Mercimek çorbası + salata", "kalori": 430, "etiketler": ["mercimek", "salata"]},
            {"ad": "Omlet + yoğurt", "kalori": 450, "etiketler": ["yumurta", "yoğurt"]},
            {"ad": "Sebzeli makarna", "kalori": 500, "etiketler": ["sebze", "makarna"]},
            {"ad": "Nohut yemeği + cacık", "kalori": 490, "etiketler": ["nohut", "yoğurt"]},
            {"ad": "Peynirli salata + çorba", "kalori": 420, "etiketler": ["peynir", "salata"]},
            {"ad": "Kısır + ayran", "kalori": 470, "etiketler": ["bulgur", "ayran"]},
            {"ad": "Sebzeli börek + yoğurt", "kalori": 520, "etiketler": ["sebze", "yoğurt"]},
            {"ad": "Mercimek köftesi + salata", "kalori": 450, "etiketler": ["mercimek", "salata"]},
            {"ad": "Patatesli omlet + ayran", "kalori": 480, "etiketler": ["patates", "yumurta", "ayran"]},
            {"ad": "Yoğurtlu kabak mücveri", "kalori": 440, "etiketler": ["yoğurt", "kabak"]},
            {"ad": "Peynirli makarna", "kalori": 510, "etiketler": ["peynir", "makarna"]},
            {"ad": "Fırın sebze + yoğurt", "kalori": 430, "etiketler": ["sebze", "yoğurt"]},
            {"ad": "Hellim salata", "kalori": 420, "etiketler": ["hellim", "salata"]},
            {"ad": "Mercimek yemeği + ayran", "kalori": 460, "etiketler": ["mercimek", "ayran"]},
            {"ad": "Nohutlu salata", "kalori": 430, "etiketler": ["nohut", "salata"]},
            {"ad": "Peynirli omlet + salata", "kalori": 440, "etiketler": ["peynir", "yumurta", "salata"]},
            {"ad": "Sebzeli krep + yoğurt", "kalori": 470, "etiketler": ["sebze", "yoğurt"]},
            {"ad": "Ayran + patatesli sebze tabağı", "kalori": 450, "etiketler": ["ayran", "patates", "sebze"]}
        ]

        aksam = [
            {"ad": "Sebze yemeği + yoğurt", "kalori": 420, "etiketler": ["sebze", "yoğurt"]},
            {"ad": "Makarna + ayran", "kalori": 480, "etiketler": ["makarna", "ayran"]},
            {"ad": "Peynirli salata + çorba", "kalori": 410, "etiketler": ["peynir", "salata"]},
            {"ad": "Patatesli omlet + salata", "kalori": 460, "etiketler": ["patates", "yumurta", "salata"]},
            {"ad": "Fırın sebze + yoğurt", "kalori": 430, "etiketler": ["sebze", "yoğurt"]},
            {"ad": "Mercimek köftesi + cacık", "kalori": 440, "etiketler": ["mercimek", "yoğurt"]},
            {"ad": "Izgara hellim + salata", "kalori": 470, "etiketler": ["hellim", "salata"]},
            {"ad": "Mercimek çorbası + salata", "kalori": 350, "etiketler": ["mercimek", "salata"]},
            {"ad": "Yoğurtlu kabak yemeği", "kalori": 390, "etiketler": ["yoğurt", "kabak"]},
            {"ad": "Omlet + sebze tabağı", "kalori": 410, "etiketler": ["yumurta", "sebze"]},
            {"ad": "Peynirli sebze fırın", "kalori": 430, "etiketler": ["peynir", "sebze"]},
            {"ad": "Ayran + nohutlu salata", "kalori": 420, "etiketler": ["ayran", "nohut", "salata"]},
            {"ad": "Mücver + yoğurt", "kalori": 400, "etiketler": ["kabak", "yoğurt"]},
            {"ad": "Fırın patates + salata", "kalori": 430, "etiketler": ["patates", "salata"]},
            {"ad": "Sebzeli yumurta scramble", "kalori": 390, "etiketler": ["yumurta", "sebze"]},
            {"ad": "Kinoalı salata", "kalori": 420, "etiketler": ["kinoa", "salata"]},
            {"ad": "Peynir tabağı + salata", "kalori": 380, "etiketler": ["peynir", "salata"]},
            {"ad": "Mercimek yemeği + yoğurt", "kalori": 430, "etiketler": ["mercimek", "yoğurt"]}
        ]

        ara = [
            {"ad": "Yoğurt", "kalori": 120, "etiketler": ["yoğurt"]},
            {"ad": "Meyve", "kalori": 90, "etiketler": ["meyve"]},
            {"ad": "10 badem", "kalori": 70, "etiketler": ["badem"]},
            {"ad": "Kefir", "kalori": 110, "etiketler": ["kefir"]},
            {"ad": "1 muz", "kalori": 100, "etiketler": ["muz"]},
            {"ad": "2 ceviz + 1 mandalina", "kalori": 130, "etiketler": ["ceviz", "mandalina"]},
            {"ad": "Ayran", "kalori": 85, "etiketler": ["ayran"]},
            {"ad": "Elma", "kalori": 80, "etiketler": ["elma"]},
            {"ad": "Çilek + yoğurt", "kalori": 130, "etiketler": ["çilek", "yoğurt"]},
            {"ad": "Leblebi", "kalori": 110, "etiketler": ["leblebi"]},
            {"ad": "Salatalık + yoğurt", "kalori": 90, "etiketler": ["salatalık", "yoğurt"]},
            {"ad": "Muz + badem", "kalori": 140, "etiketler": ["muz", "badem"]},
            {"ad": "Armut", "kalori": 95, "etiketler": ["armut"]},
            {"ad": "Kefir + yaban mersini", "kalori": 125, "etiketler": ["kefir", "meyve"]},
            {"ad": "Peynirli mini atıştırmalık", "kalori": 150, "etiketler": ["peynir"]},
            {"ad": "Yoğurt + chia", "kalori": 140, "etiketler": ["yoğurt", "chia"]},
            {"ad": "Mandalina", "kalori": 75, "etiketler": ["mandalina"]},
            {"ad": "Ceviz", "kalori": 100, "etiketler": ["ceviz"]}
        ]

    else:
        if gelir == "Düşük":
            kahvalti = [
                {"ad": "2 haşlanmış yumurta + ekmek", "kalori": 330, "etiketler": ["yumurta", "ekmek"]},
                {"ad": "Peynir + domates + zeytin", "kalori": 340, "etiketler": ["peynir", "domates", "zeytin"]},
                {"ad": "Yulaf + yoğurt", "kalori": 310, "etiketler": ["yulaf", "yoğurt"]},
                {"ad": "Menemen + ekmek", "kalori": 360, "etiketler": ["yumurta", "domates", "ekmek"]},
                {"ad": "Lor peynirli tost", "kalori": 350, "etiketler": ["lor", "ekmek"]},
                {"ad": "Haşlanmış yumurta + ayran", "kalori": 300, "etiketler": ["yumurta", "ayran"]},
                {"ad": "Peynirli sandviç", "kalori": 340, "etiketler": ["peynir", "ekmek"]},
                {"ad": "Yoğurt + muz", "kalori": 280, "etiketler": ["yoğurt", "muz"]},
                {"ad": "Peynir tabağı", "kalori": 290, "etiketler": ["peynir"]},
                {"ad": "Yumurta + domates tabağı", "kalori": 270, "etiketler": ["yumurta", "domates"]},
                {"ad": "Ayran + haşlanmış yumurta", "kalori": 280, "etiketler": ["ayran", "yumurta"]},
                {"ad": "Yulaf lapası", "kalori": 300, "etiketler": ["yulaf"]},
                {"ad": "Yoğurt + elma", "kalori": 260, "etiketler": ["yoğurt", "elma"]},
                {"ad": "Menemen tabağı", "kalori": 310, "etiketler": ["yumurta", "domates"]},
                {"ad": "Lor + salatalık", "kalori": 250, "etiketler": ["lor", "salatalık"]},
                {"ad": "Peynir + zeytin", "kalori": 270, "etiketler": ["peynir", "zeytin"]},
                {"ad": "Muzlu yoğurt", "kalori": 290, "etiketler": ["muz", "yoğurt"]},
                {"ad": "Domatesli yumurta", "kalori": 300, "etiketler": ["domates", "yumurta"]}
            ]

            ogle = [
                {"ad": "Tavuk + bulgur pilavı", "kalori": 520, "etiketler": ["tavuk", "bulgur"]},
                {"ad": "Mercimek yemeği + yoğurt", "kalori": 470, "etiketler": ["mercimek", "yoğurt"]},
                {"ad": "Ton balıklı sandviç", "kalori": 450, "etiketler": ["ton balığı", "ekmek"]},
                {"ad": "Nohut + pilav", "kalori": 530, "etiketler": ["nohut", "pilav"]},
                {"ad": "Kuru fasulye + cacık", "kalori": 500, "etiketler": ["kuru fasulye", "yoğurt"]},
                {"ad": "Tavuklu makarna", "kalori": 550, "etiketler": ["tavuk", "makarna"]},
                {"ad": "Patatesli tavuk sote", "kalori": 540, "etiketler": ["patates", "tavuk"]},
                {"ad": "Mercimek çorbası + salata", "kalori": 380, "etiketler": ["mercimek", "salata"]},
                {"ad": "Ton balıklı salata", "kalori": 410, "etiketler": ["ton balığı", "salata"]},
                {"ad": "Tavuklu salata", "kalori": 420, "etiketler": ["tavuk", "salata"]},
                {"ad": "Nohutlu sebze yemeği", "kalori": 460, "etiketler": ["nohut", "sebze"]},
                {"ad": "Fırın patates + yoğurt", "kalori": 430, "etiketler": ["patates", "yoğurt"]},
                {"ad": "Kuru fasulye + salata", "kalori": 470, "etiketler": ["kuru fasulye", "salata"]},
                {"ad": "Tavuk + salata", "kalori": 400, "etiketler": ["tavuk", "salata"]},
                {"ad": "Mercimek köftesi + ayran", "kalori": 430, "etiketler": ["mercimek", "ayran"]},
                {"ad": "Tavuk haşlama + sebze", "kalori": 410, "etiketler": ["tavuk", "sebze"]},
                {"ad": "Nohut + yoğurt", "kalori": 440, "etiketler": ["nohut", "yoğurt"]},
                {"ad": "Ton balıklı marul salatası", "kalori": 380, "etiketler": ["ton balığı", "salata"]}
            ]

            aksam = [
                {"ad": "Sebze yemeği + yoğurt", "kalori": 390, "etiketler": ["sebze", "yoğurt"]},
                {"ad": "Ton balıklı salata", "kalori": 360, "etiketler": ["ton balığı", "salata"]},
                {"ad": "Çorba + haşlanmış yumurta", "kalori": 320, "etiketler": ["çorba", "yumurta"]},
                {"ad": "Tavuklu salata", "kalori": 400, "etiketler": ["tavuk", "salata"]},
                {"ad": "Menemen + yoğurt", "kalori": 350, "etiketler": ["yumurta", "domates", "yoğurt"]},
                {"ad": "Mercimek çorbası + salata", "kalori": 330, "etiketler": ["mercimek", "salata"]},
                {"ad": "Fırın sebze + ayran", "kalori": 370, "etiketler": ["sebze", "ayran"]},
                {"ad": "Yoğurtlu kabak", "kalori": 340, "etiketler": ["yoğurt", "kabak"]},
                {"ad": "Tavuk haşlama", "kalori": 380, "etiketler": ["tavuk"]},
                {"ad": "Kuru fasulye + salata", "kalori": 410, "etiketler": ["kuru fasulye", "salata"]},
                {"ad": "Sebze çorbası + yoğurt", "kalori": 310, "etiketler": ["sebze", "yoğurt"]},
                {"ad": "Ton balıklı marul salatası", "kalori": 350, "etiketler": ["ton balığı", "salata"]},
                {"ad": "Patatesli sebze fırın", "kalori": 390, "etiketler": ["patates", "sebze"]},
                {"ad": "Mercimek yemeği + ayran", "kalori": 400, "etiketler": ["mercimek", "ayran"]},
                {"ad": "Tavuk + haşlanmış sebze", "kalori": 390, "etiketler": ["tavuk", "sebze"]},
                {"ad": "Nohutlu salata", "kalori": 360, "etiketler": ["nohut", "salata"]},
                {"ad": "Çorba + yoğurt", "kalori": 280, "etiketler": ["çorba", "yoğurt"]},
                {"ad": "Yumurtalı salata", "kalori": 340, "etiketler": ["yumurta", "salata"]}
            ]

            ara = [
                {"ad": "Elma", "kalori": 80, "etiketler": ["elma"]},
                {"ad": "Ayran", "kalori": 85, "etiketler": ["ayran"]},
                {"ad": "1 avuç leblebi", "kalori": 120, "etiketler": ["leblebi"]},
                {"ad": "Muz", "kalori": 100, "etiketler": ["muz"]},
                {"ad": "Yoğurt", "kalori": 110, "etiketler": ["yoğurt"]},
                {"ad": "1 mandalina + 5 badem", "kalori": 95, "etiketler": ["mandalina", "badem"]},
                {"ad": "Salatalık + ayran", "kalori": 70, "etiketler": ["salatalık", "ayran"]},
                {"ad": "Armut", "kalori": 95, "etiketler": ["armut"]},
                {"ad": "Ceviz", "kalori": 100, "etiketler": ["ceviz"]},
                {"ad": "Mandalina", "kalori": 75, "etiketler": ["mandalina"]},
                {"ad": "Elma + yoğurt", "kalori": 140, "etiketler": ["elma", "yoğurt"]},
                {"ad": "Muz + ayran", "kalori": 160, "etiketler": ["muz", "ayran"]},
                {"ad": "Leblebi + çay", "kalori": 110, "etiketler": ["leblebi"]},
                {"ad": "Salatalık", "kalori": 30, "etiketler": ["salatalık"]},
                {"ad": "Yoğurt + tarçın", "kalori": 120, "etiketler": ["yoğurt"]},
                {"ad": "1 portakal", "kalori": 90, "etiketler": ["portakal"]},
                {"ad": "Kefir", "kalori": 110, "etiketler": ["kefir"]},
                {"ad": "5 badem", "kalori": 60, "etiketler": ["badem"]}
            ]

        elif gelir == "Orta":
            kahvalti = [
                {"ad": "Omlet + tam buğday ekmek", "kalori": 380, "etiketler": ["yumurta", "ekmek"]},
                {"ad": "Yulaf + yoğurt + meyve", "kalori": 360, "etiketler": ["yulaf", "yoğurt", "meyve"]},
                {"ad": "Peynirli tost + domates", "kalori": 370, "etiketler": ["peynir", "ekmek", "domates"]},
                {"ad": "Menemen + ekmek", "kalori": 390, "etiketler": ["yumurta", "domates", "ekmek"]},
                {"ad": "Haşlanmış yumurta + avokado", "kalori": 400, "etiketler": ["yumurta", "avokado"]},
                {"ad": "Lor peynirli bowl", "kalori": 350, "etiketler": ["lor"]},
                {"ad": "Yoğurtlu granola bowl", "kalori": 390, "etiketler": ["yoğurt", "granola"]},
                {"ad": "Yumurta + zeytin + salatalık", "kalori": 340, "etiketler": ["yumurta", "zeytin", "salatalık"]},
                {"ad": "Muzlu yulaf lapası", "kalori": 350, "etiketler": ["muz", "yulaf"]},
                {"ad": "Peynir + ceviz + domates tabağı", "kalori": 360, "etiketler": ["peynir", "ceviz", "domates"]},
                {"ad": "Kefir + yulaf + çilek", "kalori": 330, "etiketler": ["kefir", "yulaf", "çilek"]},
                {"ad": "Patatesli omlet", "kalori": 410, "etiketler": ["patates", "yumurta"]},
                {"ad": "Lor peynirli omlet", "kalori": 370, "etiketler": ["lor", "yumurta"]},
                {"ad": "Avokadolu yumurta tabağı", "kalori": 390, "etiketler": ["avokado", "yumurta"]},
                {"ad": "Yoğurt + muz + badem", "kalori": 340, "etiketler": ["yoğurt", "muz", "badem"]},
                {"ad": "Ayran + haşlanmış yumurta", "kalori": 280, "etiketler": ["ayran", "yumurta"]},
                {"ad": "Peynirli salata tabağı", "kalori": 310, "etiketler": ["peynir", "salata"]},
                {"ad": "Menemen tabağı", "kalori": 320, "etiketler": ["yumurta", "domates"]}
            ]

            ogle = [
                {"ad": "Izgara tavuk + salata", "kalori": 480, "etiketler": ["tavuk", "salata"]},
                {"ad": "Ton balığı + haşlanmış patates", "kalori": 460, "etiketler": ["ton balığı", "patates"]},
                {"ad": "Köfte + yoğurt", "kalori": 520, "etiketler": ["köfte", "yoğurt"]},
                {"ad": "Tavuklu wrap", "kalori": 500, "etiketler": ["tavuk", "wrap"]},
                {"ad": "Etli sebze yemeği", "kalori": 510, "etiketler": ["et", "sebze"]},
                {"ad": "Bulgurlu tavuk bowl", "kalori": 495, "etiketler": ["bulgur", "tavuk"]},
                {"ad": "Izgara hindi + salata", "kalori": 470, "etiketler": ["hindi", "salata"]},
                {"ad": "Tavuklu nohut salatası", "kalori": 450, "etiketler": ["tavuk", "nohut", "salata"]},
                {"ad": "Mercimek çorbası + yoğurt", "kalori": 420, "etiketler": ["mercimek", "yoğurt"]},
                {"ad": "Fırın tavuk + patates", "kalori": 530, "etiketler": ["tavuk", "patates"]},
                {"ad": "Hindi füme sandviç", "kalori": 440, "etiketler": ["hindi", "ekmek"]},
                {"ad": "Ton balıklı salata", "kalori": 410, "etiketler": ["ton balığı", "salata"]},
                {"ad": "Tavuklu makarna", "kalori": 540, "etiketler": ["tavuk", "makarna"]},
                {"ad": "Nohutlu sebze yemeği + cacık", "kalori": 480, "etiketler": ["nohut", "sebze", "yoğurt"]},
                {"ad": "Köfteli salata", "kalori": 460, "etiketler": ["köfte", "salata"]},
                {"ad": "Tavuk + sebze tabağı", "kalori": 430, "etiketler": ["tavuk", "sebze"]},
                {"ad": "Balık + haşlanmış sebze", "kalori": 420, "etiketler": ["balık", "sebze"]},
                {"ad": "Mercimek yemeği + ayran", "kalori": 440, "etiketler": ["mercimek", "ayran"]}
            ]

            aksam = [
                {"ad": "Etli sebze yemeği", "kalori": 450, "etiketler": ["et", "sebze"]},
                {"ad": "Balık + salata", "kalori": 420, "etiketler": ["balık", "salata"]},
                {"ad": "Tavuklu sebze sote", "kalori": 430, "etiketler": ["tavuk", "sebze"]},
                {"ad": "Çorba + ton balıklı salata", "kalori": 380, "etiketler": ["çorba", "ton balığı", "salata"]},
                {"ad": "Köfteli salata", "kalori": 440, "etiketler": ["köfte", "salata"]},
                {"ad": "Zeytinyağlı sebze + yoğurt + tavuk", "kalori": 460, "etiketler": ["sebze", "yoğurt", "tavuk"]},
                {"ad": "Fırın tavuk + yoğurt", "kalori": 470, "etiketler": ["tavuk", "yoğurt"]},
                {"ad": "Mercimek çorbası + salata", "kalori": 350, "etiketler": ["mercimek", "salata"]},
                {"ad": "Sebzeli omlet + yoğurt", "kalori": 390, "etiketler": ["sebze", "yumurta", "yoğurt"]},
                {"ad": "Izgara köfte + sebze", "kalori": 470, "etiketler": ["köfte", "sebze"]},
                {"ad": "Ton balıklı marul salatası", "kalori": 360, "etiketler": ["ton balığı", "salata"]},
                {"ad": "Hindi sote + sebze", "kalori": 430, "etiketler": ["hindi", "sebze"]},
                {"ad": "Fırın kabak + yoğurt + tavuk", "kalori": 410, "etiketler": ["kabak", "yoğurt", "tavuk"]},
                {"ad": "Balık + haşlanmış sebze", "kalori": 400, "etiketler": ["balık", "sebze"]},
                {"ad": "Tavuk şiş + salata", "kalori": 440, "etiketler": ["tavuk", "salata"]},
                {"ad": "Yoğurtlu kabak", "kalori": 370, "etiketler": ["yoğurt", "kabak"]},
                {"ad": "Mercimek yemeği + ayran", "kalori": 400, "etiketler": ["mercimek", "ayran"]},
                {"ad": "Et + salata", "kalori": 430, "etiketler": ["et", "salata"]}
            ]

            ara = [
                {"ad": "Kefir", "kalori": 110, "etiketler": ["kefir"]},
                {"ad": "Muz", "kalori": 100, "etiketler": ["muz"]},
                {"ad": "10 badem", "kalori": 70, "etiketler": ["badem"]},
                {"ad": "1 elma + fıstık ezmesi", "kalori": 150, "etiketler": ["elma", "fıstık"]},
                {"ad": "Yoğurt", "kalori": 120, "etiketler": ["yoğurt"]},
                {"ad": "Protein sütü", "kalori": 140, "etiketler": ["süt"]},
                {"ad": "Çilek + yoğurt", "kalori": 130, "etiketler": ["çilek", "yoğurt"]},
                {"ad": "1 armut", "kalori": 95, "etiketler": ["armut"]},
                {"ad": "2 ceviz + 1 mandalina", "kalori": 130, "etiketler": ["ceviz", "mandalina"]},
                {"ad": "Ayran", "kalori": 85, "etiketler": ["ayran"]},
                {"ad": "Salatalık + yoğurt", "kalori": 90, "etiketler": ["salatalık", "yoğurt"]},
                {"ad": "1 muz + 5 badem", "kalori": 140, "etiketler": ["muz", "badem"]},
                {"ad": "1 elma", "kalori": 80, "etiketler": ["elma"]},
                {"ad": "Leblebi", "kalori": 110, "etiketler": ["leblebi"]},
                {"ad": "Kefir + çilek", "kalori": 125, "etiketler": ["kefir", "çilek"]},
                {"ad": "Mandalina", "kalori": 75, "etiketler": ["mandalina"]},
                {"ad": "Ceviz", "kalori": 100, "etiketler": ["ceviz"]},
                {"ad": "Yoğurt + chia", "kalori": 140, "etiketler": ["yoğurt", "chia"]}
            ]

        else:
            kahvalti = [
                {"ad": "Avokadolu yumurta tabağı", "kalori": 420, "etiketler": ["avokado", "yumurta"]},
                {"ad": "Yulaf + yoğurt + çilek + ceviz", "kalori": 410, "etiketler": ["yulaf", "yoğurt", "çilek", "ceviz"]},
                {"ad": "Protein ağırlıklı kahvaltı tabağı", "kalori": 430, "etiketler": ["yumurta", "peynir"]},
                {"ad": "Omlet + avokado + peynir", "kalori": 440, "etiketler": ["yumurta", "avokado", "peynir"]},
                {"ad": "Somonlu tost", "kalori": 400, "etiketler": ["somon", "ekmek"]},
                {"ad": "Granola bowl", "kalori": 390, "etiketler": ["granola"]},
                {"ad": "Lor + meyve + kuruyemiş tabağı", "kalori": 380, "etiketler": ["lor", "meyve", "kuruyemiş"]},
                {"ad": "Yoğurt + muz + chia", "kalori": 360, "etiketler": ["yoğurt", "muz", "chia"]},
                {"ad": "Avokado + haşlanmış yumurta", "kalori": 390, "etiketler": ["avokado", "yumurta"]},
                {"ad": "Kefir + granola + çilek", "kalori": 370, "etiketler": ["kefir", "granola", "çilek"]},
                {"ad": "Hindi füme kahvaltı tabağı", "kalori": 410, "etiketler": ["hindi", "peynir"]},
                {"ad": "Peynir + ceviz + avokado", "kalori": 400, "etiketler": ["peynir", "ceviz", "avokado"]},
                {"ad": "Somonlu salata tabağı", "kalori": 380, "etiketler": ["somon", "salata"]},
                {"ad": "Yumurta + zeytin + peynir", "kalori": 360, "etiketler": ["yumurta", "zeytin", "peynir"]},
                {"ad": "Meyveli protein yoğurdu", "kalori": 350, "etiketler": ["yoğurt", "meyve"]},
                {"ad": "Omlet + sebze tabağı", "kalori": 390, "etiketler": ["yumurta", "sebze"]},
                {"ad": "Lor + badem + meyve", "kalori": 360, "etiketler": ["lor", "badem", "meyve"]},
                {"ad": "Avokadolu smoothie bowl", "kalori": 400, "etiketler": ["avokado", "meyve"]}
            ]

            ogle = [
                {"ad": "Somon + sebze", "kalori": 540, "etiketler": ["somon", "sebze"]},
                {"ad": "Izgara et + salata", "kalori": 560, "etiketler": ["et", "salata"]},
                {"ad": "Tavuklu bowl", "kalori": 510, "etiketler": ["tavuk"]},
                {"ad": "Hindi füme wrap", "kalori": 500, "etiketler": ["hindi", "wrap"]},
                {"ad": "Ton balıklı avokadolu salata", "kalori": 490, "etiketler": ["ton balığı", "avokado", "salata"]},
                {"ad": "Izgara köfte + sebze", "kalori": 550, "etiketler": ["köfte", "sebze"]},
                {"ad": "Tavuk + kinoalı salata", "kalori": 520, "etiketler": ["tavuk", "kinoa", "salata"]},
                {"ad": "Karides + salata", "kalori": 500, "etiketler": ["karides", "salata"]},
                {"ad": "Fırın somon + brokoli", "kalori": 530, "etiketler": ["somon", "brokoli"]},
                {"ad": "Hindi köfte + salata", "kalori": 490, "etiketler": ["hindi", "salata"]},
                {"ad": "Ton balıklı marul bowl", "kalori": 470, "etiketler": ["ton balığı", "salata"]},
                {"ad": "Izgara tavuk + avokado", "kalori": 500, "etiketler": ["tavuk", "avokado"]},
                {"ad": "Et + haşlanmış sebze", "kalori": 520, "etiketler": ["et", "sebze"]},
                {"ad": "Somon + salata", "kalori": 510, "etiketler": ["somon", "salata"]},
                {"ad": "Hindi + kinoalı salata", "kalori": 500, "etiketler": ["hindi", "kinoa", "salata"]},
                {"ad": "Tavuk + fırın kabak", "kalori": 480, "etiketler": ["tavuk", "kabak"]},
                {"ad": "Izgara köfte + yoğurt", "kalori": 530, "etiketler": ["köfte", "yoğurt"]},
                {"ad": "Balık + zeytinyağlı sebze", "kalori": 500, "etiketler": ["balık", "sebze"]}
            ]

            aksam = [
                {"ad": "Balık + zeytinyağlı sebze", "kalori": 470, "etiketler": ["balık", "sebze"]},
                {"ad": "Izgara tavuk + avokadolu salata", "kalori": 450, "etiketler": ["tavuk", "avokado", "salata"]},
                {"ad": "Et + sebze garnitür", "kalori": 500, "etiketler": ["et", "sebze"]},
                {"ad": "Karidesli salata", "kalori": 430, "etiketler": ["karides", "salata"]},
                {"ad": "Kabak spagetti + tavuk", "kalori": 420, "etiketler": ["kabak", "tavuk"]},
                {"ad": "Fırın somon + brokoli", "kalori": 480, "etiketler": ["somon", "brokoli"]},
                {"ad": "Hindi köfte + salata", "kalori": 440, "etiketler": ["hindi", "salata"]},
                {"ad": "Ton balıklı yeşil salata", "kalori": 390, "etiketler": ["ton balığı", "salata"]},
                {"ad": "Izgara et + sebze", "kalori": 470, "etiketler": ["et", "sebze"]},
                {"ad": "Tavuk + yoğurtlu kabak", "kalori": 430, "etiketler": ["tavuk", "yoğurt", "kabak"]},
                {"ad": "Balık + salata", "kalori": 410, "etiketler": ["balık", "salata"]},
                {"ad": "Hindi sote + sebze", "kalori": 430, "etiketler": ["hindi", "sebze"]},
                {"ad": "Somon + salata", "kalori": 450, "etiketler": ["somon", "salata"]},
                {"ad": "Et + yoğurtlu sebze", "kalori": 460, "etiketler": ["et", "yoğurt", "sebze"]},
                {"ad": "Tavuk + haşlanmış sebze", "kalori": 400, "etiketler": ["tavuk", "sebze"]},
                {"ad": "Karides + avokado salata", "kalori": 440, "etiketler": ["karides", "avokado", "salata"]},
                {"ad": "Hindi + salata bowl", "kalori": 420, "etiketler": ["hindi", "salata"]},
                {"ad": "Somon + kuşkonmaz", "kalori": 470, "etiketler": ["somon", "sebze"]}
            ]

            ara = [
                {"ad": "Protein yoğurdu", "kalori": 150, "etiketler": ["yoğurt"]},
                {"ad": "Karışık kuruyemiş", "kalori": 180, "etiketler": ["kuruyemiş"]},
                {"ad": "Meyve", "kalori": 90, "etiketler": ["meyve"]},
                {"ad": "Kefir", "kalori": 110, "etiketler": ["kefir"]},
                {"ad": "Protein bar", "kalori": 190, "etiketler": ["protein bar"]},
                {"ad": "Yoğurt + chia", "kalori": 160, "etiketler": ["yoğurt", "chia"]},
                {"ad": "1 muz + fıstık ezmesi", "kalori": 170, "etiketler": ["muz", "fıstık"]},
                {"ad": "Badem", "kalori": 90, "etiketler": ["badem"]},
                {"ad": "Ceviz", "kalori": 100, "etiketler": ["ceviz"]},
                {"ad": "Mandalina", "kalori": 75, "etiketler": ["mandalina"]},
                {"ad": "Çilek + yoğurt", "kalori": 130, "etiketler": ["çilek", "yoğurt"]},
                {"ad": "Elma + badem", "kalori": 150, "etiketler": ["elma", "badem"]},
                {"ad": "Kefir + muz", "kalori": 170, "etiketler": ["kefir", "muz"]},
                {"ad": "Protein sütü", "kalori": 140, "etiketler": ["süt"]},
                {"ad": "Yoğurt + meyve", "kalori": 150, "etiketler": ["yoğurt", "meyve"]},
                {"ad": "Armut", "kalori": 95, "etiketler": ["armut"]},
                {"ad": "Leblebi", "kalori": 110, "etiketler": ["leblebi"]},
                {"ad": "Meyve + kuruyemiş", "kalori": 170, "etiketler": ["meyve", "kuruyemiş"]}
            ]

    return kahvalti, ogle, aksam, ara