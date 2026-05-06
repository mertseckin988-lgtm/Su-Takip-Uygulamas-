import unittest
from src.modules.water_tracker import WaterTracker

class TestWaterTracker(unittest.TestCase):
    def test_su_ekleme_basarili(self):
        # Test 1: Doğru değer girilince çalışıyor mu?
        tracker = WaterTracker("TestKullanici")
        baslangic = tracker.tuketilen
        tracker.su_ekle(1.5)
        self.assertEqual(tracker.tuketilen, baslangic + 1.5)

    def test_su_ekleme_hatali(self):
        # Test 2: Negatif değer girilince engelliyor mu?
        tracker = WaterTracker("TestKullanici")
        sonuc = tracker.su_ekle(-5)
        self.assertFalse(sonuc) # Yanlış işlemde False dönmeli

if __name__ == '__main__':
    unittest.main()