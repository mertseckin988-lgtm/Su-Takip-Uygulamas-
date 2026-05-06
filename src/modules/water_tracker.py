from src.core.base_user import BaseUser
from src.services.data_manager import DataManager

class WaterTracker(BaseUser):
    def __init__(self, isim, hedef_litre=2.5):
        super().__init__(isim)
        self.hedef = hedef_litre
        self.db = DataManager()
        # Kayıt listesini çekiyoruz
        self.kayitlar = self.db.veri_getir(self.get_isim())
        self.tuketilen = sum(self.kayitlar) # Listedekileri topluyoruz

    def su_ekle(self, miktar):
        try:
            miktar = float(miktar)
            if miktar <= 0:
                raise ValueError("Su miktarı 0'dan büyük olmalıdır!")
            
            self.db.veri_kaydet(self.get_isim(), miktar)
            self.kayitlar = self.db.veri_getir(self.get_isim())
            self.tuketilen = sum(self.kayitlar)
            return True
            
        except ValueError:
            return False

    def veri_sil(self, index):
        # Tekil veri silme emrini veritabanına iletir
        self.db.tekil_veri_sil(self.get_isim(), index)
        self.kayitlar = self.db.veri_getir(self.get_isim())
        self.tuketilen = sum(self.kayitlar)

    def profil_bilgisi(self):
        kalan = max(0, self.hedef - self.tuketilen)
        # 🎉 KONFETİ BURADA DEVREYE GİRİYOR!
        durum = "TEBRİKLER HEDEFİ GEÇTİNİZ! 🎉" if kalan == 0 else f"Kalan hedef: {kalan:.2f}L"
        return f"Sayın {self.get_isim()} | İçilen: {self.tuketilen:.2f}L | {durum}"