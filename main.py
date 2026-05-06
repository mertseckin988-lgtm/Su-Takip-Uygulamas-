import tkinter as tk
from tkinter import messagebox
from src.modules.water_tracker import WaterTracker

# ================= KENDİ ÇİZDİĞİMİZ YUVARLAK BUTON (PillButton) =================
class PillButton(tk.Canvas):
    def __init__(self, parent, text, command, width=150, height=40, bg="black", fg="white"):
        super().__init__(parent, width=width, height=height, bg="white", highlightthickness=0)
        self.command = command
        self.create_oval(0, 0, height, height, fill=bg, outline=bg)
        self.create_oval(width-height, 0, width, height, fill=bg, outline=bg)
        self.create_rectangle(height/2, 0, width-(height/2), height, fill=bg, outline=bg)
        self.create_text(width/2, height/2, text=text, fill=fg, font=("Segoe UI", 11, "bold"))
        self.bind("<Button-1>", lambda e: self.command())
        self.bind("<Enter>", lambda e: self.config(cursor="hand2"))
        self.bind("<Leave>", lambda e: self.config(cursor=""))

# ================= NİHAİ ANA UYGULAMA (MENÜ + LİSTE + KONFETİ) =================
class ModernHealthApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sağlık Asistanı")
        self.root.geometry("900x650")
        self.root.configure(bg="white")

        self.isim = ""
        self.boy = 0
        self.kilo = 0
        self.yas = 0
        self.tracker = None

        self.font_baslik = ("Segoe UI", 24, "bold")
        self.font_normal = ("Segoe UI", 12)
        self.bg_color = "white"
        self.fg_color = "black"

        # TIRT TERCİHİN OLAN İMZA (Ters slash ile)
        tk.Label(self.root, text="Mert Seçkin \ Ostim Tech Unıversty", 
                 font=("Segoe UI", 9, "bold"), bg=self.bg_color, fg="gray").pack(side="bottom", pady=10)

        self.container = tk.Frame(self.root, bg=self.bg_color)
        self.container.pack(expand=True, fill="both", pady=20)

        self.sayfa_giris_olustur()

    # ================= 1. SAYFA: GİRİŞ =================
    def sayfa_giris_olustur(self):
        self.frame_giris = tk.Frame(self.container, bg=self.bg_color)
        self.frame_giris.pack(expand=True)

        tk.Label(self.frame_giris, text="Su Takip Programı", font=self.font_baslik, bg=self.bg_color, fg=self.fg_color).pack(pady=20)
        tk.Label(self.frame_giris, text="Ad \ Soyad:", font=self.font_normal, bg=self.bg_color, fg=self.fg_color).pack()
        
        self.entry_isim = tk.Entry(self.frame_giris, font=self.font_normal, justify="center", width=25, bg="#f0f0f0", relief="flat")
        self.entry_isim.pack(pady=10)

        self.lbl_hata = tk.Label(self.frame_giris, text="", font=("Segoe UI", 10, "italic"), bg=self.bg_color, fg="red")
        self.lbl_hata.pack()

        buton_frame = tk.Frame(self.frame_giris, bg=self.bg_color)
        buton_frame.pack(pady=20)
        PillButton(buton_frame, text="Devam Et", command=self.giris_kontrol, width=150, height=40).pack()

    def giris_kontrol(self):
        tam_isim = self.entry_isim.get().strip()
        if len(tam_isim.split()) < 2:
            self.lbl_hata.config(text="Lütfen tam adınızı giriniz!")
        else:
            self.isim = tam_isim
            self.frame_giris.destroy()
            self.sayfa_profil_olustur()

    # ================= 2. SAYFA: PROFİL =================
    def sayfa_profil_olustur(self):
        self.frame_profil = tk.Frame(self.container, bg=self.bg_color)
        self.frame_profil.pack(expand=True)

        tk.Label(self.frame_profil, text=f"Hoş geldin, {self.isim.split()[0]}!", font=self.font_baslik, bg=self.bg_color, fg=self.fg_color).pack(pady=20)

        self.entry_boy = self.girdi_alani(self.frame_profil, "Boy (cm):")
        self.entry_kilo = self.girdi_alani(self.frame_profil, "Kilo (kg):")
        self.entry_yas = self.girdi_alani(self.frame_profil, "Yaş:")

        buton_frame = tk.Frame(self.frame_profil, bg=self.bg_color)
        buton_frame.pack(pady=30)
        PillButton(buton_frame, text="Profili Oluştur", command=self.profil_kaydet, width=180, height=40).pack()

    def girdi_alani(self, parent, metin):
        frame = tk.Frame(parent, bg=self.bg_color)
        frame.pack(pady=5)
        tk.Label(frame, text=metin, font=self.font_normal, bg=self.bg_color, fg=self.fg_color, width=10, anchor="e").pack(side="left", padx=10)
        entry = tk.Entry(frame, font=self.font_normal, justify="center", width=15, bg="#f0f0f0", relief="flat")
        entry.pack(side="left")
        return entry

    def profil_kaydet(self):
        try:
            self.boy = int(self.entry_boy.get())
            self.kilo = float(self.entry_kilo.get())
            self.yas = int(self.entry_yas.get())
            if self.boy <= 0 or self.kilo <= 0 or self.yas <= 0: raise ValueError
            
            su_hedefi = round(self.kilo * 0.033, 2)
            self.tracker = WaterTracker(self.isim, hedef_litre=su_hedefi)
            
            self.frame_profil.destroy()
            self.sayfa_dashboard_olustur()
        except ValueError:
            messagebox.showerror("Hata", "Lütfen pozitif sayılar girin!")

    # ================= 3. SAYFA: DASHBOARD (MENÜ + İÇERİK) =================
    def sayfa_dashboard_olustur(self):
        # O ÇOK İSTEDİĞİN SOL MENÜ (SİDEBAR) GERİ GELDİ!
        self.sidebar = tk.Frame(self.container, bg=self.bg_color, width=220, highlightbackground="black", highlightthickness=2)
        self.sidebar.pack(side="left", fill="y", padx=10)

        tk.Label(self.sidebar, text="SAĞLIK MENÜSÜ", font=("Segoe UI", 16, "bold"), bg=self.bg_color, fg=self.fg_color).pack(pady=20)

        menuler = [
            ("💧 Su Takibi", self.goster_su),
            ("📊 Vücut Kitle İndeksi", self.hesapla_bmi),
            ("⚖️ İdeal Kilo", self.hesapla_ideal_kilo),
            ("🔥 Kalori İhtiyacı", self.hesapla_kalori),
            ("🥓 Yağ Oranı", self.hesapla_yag)
        ]

        for text, komut in menuler:
            tk.Button(self.sidebar, text=text, command=komut, bg=self.bg_color, fg=self.fg_color, 
                      font=self.font_normal, relief="flat", anchor="w", padx=20, cursor="hand2", 
                      activebackground="black", activeforeground="white").pack(fill="x", pady=5)

        # SAĞ İÇERİK ALANI
        self.icerik = tk.Frame(self.container, bg=self.bg_color)
        self.icerik.pack(side="right", expand=True, fill="both", padx=20)

        self.goster_su()

    def icerigi_temizle(self):
        for widget in self.icerik.winfo_children(): widget.destroy()

    # --- HESAPLAMA FONKSİYONLARI ---
    def hesapla_bmi(self):
        self.icerigi_temizle()
        bmi = self.kilo / ((self.boy / 100) ** 2)
        durum = "Zayıf" if bmi < 18.5 else "Normal" if bmi < 25 else "Fazla Kilolu" if bmi < 30 else "Obez"
        tk.Label(self.icerik, text="Vücut Kitle İndeksi", font=self.font_baslik, bg=self.bg_color).pack(pady=30)
        tk.Label(self.icerik, text=f"BMI: {bmi:.2f}", font=("Segoe UI", 20, "bold"), bg=self.bg_color).pack(pady=10)
        tk.Label(self.icerik, text=f"Durum: {durum}", font=("Segoe UI", 16, "italic"), fg="gray", bg=self.bg_color).pack()

    def hesapla_ideal_kilo(self):
        self.icerigi_temizle()
        ideal = 50 + 2.3 * ((self.boy / 2.54) - 60)
        tk.Label(self.icerik, text="İdeal Kilo", font=self.font_baslik, bg=self.bg_color).pack(pady=30)
        tk.Label(self.icerik, text=f"{ideal:.1f} kg", font=("Segoe UI", 20, "bold"), bg=self.bg_color).pack(pady=10)

    def hesapla_kalori(self):
        self.icerigi_temizle()
        kalori = self.kilo * 24 * 1.2 
        tk.Label(self.icerik, text="Kalori İhtiyacı", font=self.font_baslik, bg=self.bg_color).pack(pady=30)
        tk.Label(self.icerik, text=f"{kalori:.0f} kcal / gün", font=("Segoe UI", 20, "bold"), bg=self.bg_color).pack(pady=10)

    def hesapla_yag(self):
        self.icerigi_temizle()
        bmi = self.kilo / ((self.boy / 100) ** 2)
        yag = (1.20 * bmi) + (0.23 * self.yas) - 16.2
        tk.Label(self.icerik, text="Vücut Yağ Oranı", font=self.font_baslik, bg=self.bg_color).pack(pady=30)
        tk.Label(self.icerik, text=f"% {yag:.1f}", font=("Segoe UI", 20, "bold"), bg=self.bg_color).pack(pady=10)

    # --- ANA SU TAKİBİ FONKSİYONLARI ---
    def goster_su(self):
        self.icerigi_temizle()
        
        tk.Label(self.icerik, text="Günlük Su Takibi", font=self.font_baslik, bg=self.bg_color).pack(pady=10)
        self.lbl_su_durum = tk.Label(self.icerik, text=self.tracker.profil_bilgisi(), font=("Segoe UI", 16), bg=self.bg_color)
        self.lbl_su_durum.pack(pady=5)

        self.lbl_kirmizi_veri = tk.Label(self.icerik, text="", font=("Segoe UI", 18, "bold"), bg=self.bg_color, fg="red")
        self.lbl_kirmizi_veri.pack(pady=5)
        self.guncelle_kirmizi_yazi()

        girdi_frame = tk.Frame(self.icerik, bg=self.bg_color)
        girdi_frame.pack(pady=10)
        tk.Label(girdi_frame, text="Su (Litre):", font=self.font_normal, bg=self.bg_color).pack(side="left")
        self.entry_su = tk.Entry(girdi_frame, font=("Segoe UI", 16), justify="center", width=8, bg="#f0f0f0", relief="flat")
        self.entry_su.pack(side="left", padx=10)
        
        PillButton(girdi_frame, text="Ekle", command=self.btn_su_ekle, width=100, height=35).pack(side="left")

        tk.Label(self.icerik, text="Eklenen Veriler (Silmek için listeden seçin):", font=("Segoe UI", 10, "italic"), bg=self.bg_color, fg="gray").pack(pady=(15, 0))
        self.liste_veriler = tk.Listbox(self.icerik, font=("Segoe UI", 12), width=35, height=6, relief="solid", bd=1)
        self.liste_veriler.pack(pady=5)
        
        sil_frame = tk.Frame(self.icerik, bg=self.bg_color)
        sil_frame.pack(pady=5)
        PillButton(sil_frame, text="Seçili Olanı Sil", command=self.btn_secili_sil, width=150, height=35).pack()

        self.liste_guncelle()

    def guncelle_kirmizi_yazi(self):
        self.lbl_kirmizi_veri.config(text=f"TOPLAM KAYITLI VERİ: {self.tracker.tuketilen:.2f} LİTRE")

    def liste_guncelle(self):
        self.liste_veriler.delete(0, tk.END)
        for i, miktar in enumerate(self.tracker.kayitlar):
            self.liste_veriler.insert(tk.END, f"Kayıt {i+1} ----> {miktar} Litre")

    def btn_su_ekle(self):
        miktar = self.entry_su.get()
        if self.tracker.su_ekle(miktar):
            self.entry_su.delete(0, tk.END)
            self.lbl_su_durum.config(text=self.tracker.profil_bilgisi())
            self.guncelle_kirmizi_yazi()
            self.liste_guncelle()
        else:
            messagebox.showwarning("Hata", "Lütfen geçerli bir sayı girin!")

    def btn_secili_sil(self):
        secim = self.liste_veriler.curselection()
        if not secim:
            messagebox.showwarning("Uyarı", "Lütfen silmek istediğiniz kaydı tıklayarak seçin!")
            return
        
        index = secim[0]
        self.tracker.veri_sil(index)
        self.lbl_su_durum.config(text=self.tracker.profil_bilgisi())
        self.guncelle_kirmizi_yazi()
        self.liste_guncelle()

if __name__ == "__main__":
    root = tk.Tk()
    app = ModernHealthApp(root)
    root.mainloop()