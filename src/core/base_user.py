class BaseUser:
    def __init__(self, isim):
        # Encapsulation (Kapsülleme): İsim değişkenini dışarıdan doğrudan erişime kapattık (__isim)
        self.__isim = isim 

    def get_isim(self):
        # Dışarıdan isme ulaşmak için güvenli bir kapı açtık.
        return self.__isim

    def profil_bilgisi(self):
        # Polymorphism (Çok Biçimlilik) için alt sınıfta ezeceğimiz (override) temel metod
        return f"Kullanıcı: {self.__isim}"