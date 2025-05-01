
import os
import random
import string
import time

def temizle():
    os.system('cls' if os.name == 'nt' else 'clear')

def animasyonlu_yazi(metin):
    for harf in metin:
        print(harf, end='', flush=True)
        time.sleep(0.1)
    print()

def banner():
    temizle()
    print("""
\033[96m███████╗███████╗███████╗██╗     
\033[96m██╔════╝██╔════╝██╔════╝██║     
\033[96m███████╗█████╗  █████╗  ██║     
\033[96m╚════██║██╔══╝  ██╔══╝  ██║     
\033[96m███████║███████╗██║     ███████╗
\033[96m╚══════╝╚══════╝╚═╝     ╚══════╝
\033[92mEZEL V1 - Çok Amaçlı Araç
>> ezel \033[91m#ariva \033[92m<<
\033[95mig=ezel.501a\033[0m
""")

def ana_menu():
    while True:
        banner()
        print("""
\033[93m[1]\033[0m Tool'u Çalıştır
\033[93m[2]\033[0m Admin Yönlendirme
\033[93m[3]\033[0m Tool Hakkında Bilgi
\033[93m[4]\033[0m Sosyal Medya Hesaplarımız
\033[93m[5]\033[0m Tool'u Kapat
        """)
        secim = input("Seçiminizi yapınız >>> ")

        if secim == "1":
            tool_menu()
        elif secim == "2":
            input("Instagram: @ezel.501a (Enter ile devam)")
        elif secim == "3":
            input("EZEL V1: Çok Amaçlı bir siber güvenlik aracıdır. Enter ile devam.")
        elif secim == "4":
            input("Instagram: @ezel.501a  |  Telegram: @ezeltools  (Enter ile devam)")
        elif secim == "5":
            print("Çıkılıyor...")
            time.sleep(1)
            break
        else:
            input("Geçersiz seçim. Enter ile tekrar dene.")

def tool_menu():
    temizle()
    animasyonlu_yazi("\n\033[91m#  A  R  İ  V  A  !\033[0m\n")
    while True:
        banner()
        print("""
\033[94m[1]\033[0m IP Analizi
\033[94m[2]\033[0m Web Sitesi Flood (dummy)
\033[94m[3]\033[0m Parola Oluştur
\033[94m[4]\033[0m Telegram Analizi (yakında)
\033[94m[5]\033[0m Telefon Analizi (yakında)
\033[94m[6]\033[0m USB Killer Bilgilendirme
\033[94m[7]\033[0m Geçici E-posta (tarayıcı)
\033[94m[8]\033[0m Sahte Bilgi Oluştur
\033[94m[9]\033[0m ÖGE Şablonları
\033[94m[0]\033[0m Geri Dön
        """)
        sec = input("Seçiminizi yapınız >>> ")

        if sec == "1":
            os.system("curl ipinfo.io")
            input("Devam etmek için Enter...")
        elif sec == "2":
            input("Flood sistemi gelecekte eklenecek. Enter ile geri dön.")
        elif sec == "3":
            pwd = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
            print("Oluşturulan Parola:", pwd)
            input("Devam etmek için Enter...")
        elif sec == "4":
            input("Telegram analiz özelliği geliştiriliyor.")
        elif sec == "5":
            input("Telefon analiz özelliği geliştiriliyor.")
        elif sec == "6":
            input("USB Killer fiziksel bir cihazdır. Bu sadece bilgi içindir.")
        elif sec == "7":
            os.system("xdg-open https://temp-mail.org")
        elif sec == "8":
            print("İsim: Mert Yılmaz\nAdres: Ankara\nTC: 12345678900\nTel: 0555 000 00 00")
            input("Devam etmek için Enter...")
        elif sec == "9":
            print("OGE Şablonları: Türkçe, Matematik, Fizik. (Bu sadece görseldir.)")
            input("Devam etmek için Enter...")
        elif sec == "0":
            break
        else:
            input("Geçersiz seçim. Enter ile tekrar dene.")

ana_menu()
