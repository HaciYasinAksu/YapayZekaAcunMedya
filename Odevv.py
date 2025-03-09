# Dosya adı
dosya_adi = "kullanici_verileri.txt"

# Kullanıcıdan 5 satır veri al
veriler = []
print("Lütfen 5 satır veri girin:")
for i in range(5):
    satir = input(f"{i + 1}. satır: ")
    veriler.append(satir)

# Verileri dosyaya yaz
with open(dosya_adi, "w", encoding="utf-8") as dosya:
    for satir in veriler:
        dosya.write(satir + "\n")

print(f"\nVeriler '{dosya_adi}' dosyasına kaydedildi.")

# Dosyayı okuyarak içeriği ekrana yazdır
print(f"\n'{dosya_adi}' dosyasının içeriği:")
with open(dosya_adi, "r", encoding="utf-8") as dosya:
    for satir in dosya:
        print(satir.strip())