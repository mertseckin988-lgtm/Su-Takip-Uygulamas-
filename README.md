# BGT 132 Final Projesi: Günlük Su Tüketim Takipçisi (Water Tracker)

## Proje Adı
Günlük Su Tüketim Takipçisi Uygulaması (OOP & Modüler Mimari)

## Proje Amacı
Kullanıcıların sağlıklı bir yaşam sürebilmeleri için günlük olarak tüketmeleri gereken su miktarını takip eden, kaydeden ve hedefe olan uzaklıklarını raporlayan interaktif bir terminal uygulaması geliştirmek. Bu proje, BGT 132 Yazılım Geliştirme Teknolojileri dersi kapsamında Nesne Yönelimli Programlama (OOP) ve modüler mimari prensipleri kullanılarak tasarlanmıştır.

## Proje Demosu: Kurulum ve Çalıştırma Talimatları
Uygulama herhangi bir harici kütüphane gerektirmez (Standart Python kütüphaneleri kullanılmıştır).

1. Proje dosyalarını bilgisayarınıza indirin veya Git üzerinden klonlayın.
2. Bilgisayarınızda **Python 3.x** sürümünün yüklü olduğundan emin olun.
3. Terminali veya Komut İstemini (CMD) açın ve proje ana dizinine (`SuTakipProjesi`) gidin.
4. Uygulamayı başlatmak için terminale aşağıdaki komutu girin:
   ```bash
   python main.py
   Ekranda beliren menü yönergelerini takip ederek su tüketiminizi kaydedin ve raporlarınızı alın.

## Mimari ve OOP (Nesne Yönelimli Programlama) Kullanımı
Proje tek bir dosyaya yığılmamış, SRP (Single Responsibility Principle - Tek Sorumluluk Prensibi) gözetilerek modüllere ayrılmıştır.

## Encapsulation (Kapsülleme): BaseUser sınıfında kullanıcı isimleri (__isim) dışarıdan doğrudan erişime kapatılarak veri güvenliği sağlanmıştır. Veriye sadece get_isim() metodu ile ulaşılabilir.

## Inheritance (Kalıtım): WaterTracker sınıfı, temel kullanıcı verilerini barındıran BaseUser sınıfından miras alarak (inherit) oluşturulmuştur.

## Polymorphism (Çok Biçimlilik): BaseUser içindeki profil_bilgisi() metodu, alt sınıf olan WaterTracker içerisinde ezilerek (override) kendi ihtiyacına göre yeniden şekillendirilmiştir.

## Klasör Yapısı
Proje, istenilen standart klasör hiyerarşisine uygun olarak tasarlanmıştır:

Plaintext
SuTakipProjesi/
├── docs/                 # Gereksinim analizi ve UML diyagramları (PDF)
├── src/                  # Ana kaynak kodlar
│   ├── core/             # Temel iş mantığı (BaseUser sınıfı)
│   ├── modules/          # Ana özellikler (WaterTracker sınıfı)
│   └── services/         # Veri erişim katmanı (DataManager sınıfı)
├── data/                 # JSON formatında dinamik kullanıcı verileri
├── main.py               # Uygulamayı başlatan ana dosya
└── README.md             # Proje dokümantasyonu
## Hata Yönetimi (Try-Catch)
Kullanıcının sisteme yanlış veri (örneğin harf veya negatif sayı) girmesini engellemek amacıyla try-except blokları kullanılmıştır. Hatalı girişlerde program çökmez, kullanıcıya anlamlı bir hata mesajı döndürür.

## Veri Kalıcılığı (Data Persistence)
Kullanıcıların girdikleri su verileri anlık olarak silinmez. DataManager sınıfı aracılığıyla data/su_verisi.json dosyasına kaydedilir. Program kapatılıp açıldığında dahi kullanıcı verileri kaldığı yerden devam eder.
