import json
import os

class DataManager:
    def __init__(self):
        self.dosya_yolu = "data/su_verisi.json"
        self._dosya_kontrol()

    def _dosya_kontrol(self):
        if not os.path.exists("data"):
            os.makedirs("data")
        if not os.path.exists(self.dosya_yolu):
            with open(self.dosya_yolu, "w") as file:
                json.dump({}, file)

    def veri_kaydet(self, isim, miktar):
        with open(self.dosya_yolu, "r") as file:
            veriler = json.load(file)
        
        # Verileri artık liste (array) olarak tutuyoruz
        if isim not in veriler:
            veriler[isim] = []
        veriler[isim].append(miktar)
            
        with open(self.dosya_yolu, "w") as file:
            json.dump(veriler, file)

    def veri_getir(self, isim):
        # Toplamı değil, liste geçmişini döndürür
        with open(self.dosya_yolu, "r") as file:
            veriler = json.load(file)
        return veriler.get(isim, [])

    def tekil_veri_sil(self, isim, index):
        # Sadece seçilen sıradaki veriyi siler
        with open(self.dosya_yolu, "r") as file:
            veriler = json.load(file)
        
        if isim in veriler and index < len(veriler[isim]):
            veriler[isim].pop(index)
            
        with open(self.dosya_yolu, "w") as file:
            json.dump(veriler, file)