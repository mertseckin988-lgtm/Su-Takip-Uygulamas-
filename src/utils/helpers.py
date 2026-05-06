import os

# Terminal için ANSI Renk Kodları
RENK_LACIVERT_ARKA = '\033[44m'
RENK_BEYAZ_YAZI = '\033[97m'
RENK_SIFIRLA = '\033[0m'

def ekrani_hazirla():
    # 1. Önce ekranı temizle
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # 2. Tüm terminalin rengini Lacivert Arka Plan ve Beyaz Yazı yap
    # Not: Bu komut yazdırılan metinlerin rengini değiştirir.
    print(RENK_LACIVERT_ARKA + RENK_BEYAZ_YAZI, end="")

def imza_yazdir():
    # Sayfanın en altına eklenecek profesyonel imza bloğu
    print("\n" + "="*50)
    print("        mert seçkin / ostim tech university        ")
    print("="*50 + RENK_SIFIRLA + "\n")