def rle_sikistir(metin):
    # Boş veri gelirse hata vermesin diye kontrol ediyoruz
    if not metin:
        return ""

    sonuc = ""
    sayac = 1

    # Metnin 2. harfinden başlayıp sonuna kadar gidiyoruz
    for i in range(1, len(metin)):
        # Eğer bu harf bir öncekiyle aynıysa sayacı arttır
        if metin[i] == metin[i-1]:
            sayac += 1
        else:
            # Farklı harfe geçince öncekini kaydet (Sayısı + Harf)
            sonuc += str(sayac) + metin[i-1]
            sayac = 1 # Sayacı sıfırla
            
    # Döngü bitince son kalan grubu da eklememiz lazım
    sonuc += str(sayac) + metin[-1]
    
    return sonuc

def rle_coz(sifreli_metin):
    cozulmus = ""
    i = 0
    
    # Tüm metni tarıyoruz
    while i < len(sifreli_metin):
        sayi_yazisi = ""
        
        # Sayı kısımlarını buluyoruz (mesela 12A ise 12 yi alması için)
        while i < len(sifreli_metin) and sifreli_metin[i].isdigit():
            sayi_yazisi += sifreli_metin[i]
            i += 1
            
        sayi = int(sayi_yazisi)
        harf = sifreli_metin[i]
        
        # Harfi sayı kadar çarpıp ekliyoruz
        cozulmus += harf * sayi
        i += 1
        
    return cozulmus

def oran_hesapla(orijinal, sikismis):
    # Boyutları alıyoruz
    ilk_boyut = len(orijinal)
    son_boyut = len(sikismis)
    
    if ilk_boyut == 0:
        return 0
    
    # Yüzde kaç küçüldüğünü hesaplayan formül
    yuzde = (1 - (son_boyut / ilk_boyut)) * 100
    return yuzde

# --- Test ---

print("--- RLE Projesi ---")
giris = input("Metni girin (Örn: AAAAABBB): ")

# Sıkıştırma yapıyoruz
sikismis_hali = rle_sikistir(giris)
print("Sıkışmış Hali:", sikismis_hali)

# Geri çözüyoruz
cozulmus_hali = rle_coz(sikismis_hali)
print("Geri Çözülmüş:", cozulmus_hali)

# Oran hesaplıyoruz
basari_orani = oran_hesapla(giris, sikismis_hali)
print(f"Sıkıştırma Oranı: %{basari_orani:.2f}")

# Doğru çalıştı mı kontrolü
if giris == cozulmus_hali:
    print("Durum: Başarılı, veri kaybı yok.")
else:
    print("Durum: Hata var.")
