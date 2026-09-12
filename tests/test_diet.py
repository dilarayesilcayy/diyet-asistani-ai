import unittest

from diet import haftalik_plan


def ogunler(prefix, kaloriler):
    return [
        {"ad": f"{prefix} {index}", "kalori": kalori, "etiketler": []}
        for index, kalori in enumerate(kaloriler, start=1)
    ]


class HaftalikPlanTests(unittest.TestCase):
    def setUp(self):
        self.plan = haftalik_plan(
            ogunler("Kahvaltı", [300, 330, 360]),
            ogunler("Öğle", [450, 500, 550]),
            ogunler("Akşam", [500, 550, 600]),
            ogunler("Ara", [100, 150, 200]),
            1500,
        )

    def test_yedi_gun_olusturur(self):
        self.assertEqual(len(self.plan), 7)
        self.assertTrue(all(self.plan.values()))

    def test_gunluk_kombinasyonlar_farklidir(self):
        imzalar = {
            (
                gun["kahvalti"]["ad"],
                gun["ogle"]["ad"],
                gun["aksam"]["ad"],
                gun["ara"]["ad"],
            )
            for gun in self.plan.values()
        }
        self.assertEqual(len(imzalar), 7)

    def test_hedef_ve_toplam_korunur(self):
        for gun in self.plan.values():
            hesaplanan_toplam = sum(
                gun[ogun]["kalori"]
                for ogun in ("kahvalti", "ogle", "aksam", "ara")
            )
            self.assertEqual(gun["toplam"], hesaplanan_toplam)
            self.assertEqual(gun["hedef"], 1500)


if __name__ == "__main__":
    unittest.main()
