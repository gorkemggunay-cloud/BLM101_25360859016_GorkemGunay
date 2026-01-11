# Veri Depolama ve Sıkıştırma Algoritmaları (RLE Projesi)

## Öğrenci Bilgileri
* **Ad Soyad:** Görkem GÜNAY
* **Öğrenci No:** 25360859016
* **Ders:** BLM101 - Bilgisayar Mühendisliğine Giriş

## Proje Konusu
Bu proje, **Run-Length Encoding (RLE)** algoritmasını kullanarak metin tabanlı verilerin sıkıştırılmasını ve tekrar çözülmesini amaçlamaktadır. Proje kapsamında Python dili kullanılarak encode (sıkıştırma) ve decode (çözme) fonksiyonları geliştirilmiştir.

## YouTube Sunum Videosu
Projenin çalışma mantığını ve kodların anlatımını içeren videoya aşağıdaki linkten ulaşabilirsiniz:
* **Video Linki:** https://www.youtube.com/watch?v=jvxYp5fuvME

## Proje Açıklaması ve Kullanım
Bu program üç temel fonksiyon içerir:
1. **rle_sikistir:** Ardışık tekrar eden karakterleri (örn: AAAA) sayı ve karakter çifti olarak (örn: 4A) sıkıştırır.
2. **rle_coz:** Sıkıştırılmış veriyi analiz ederek orijinal metne geri döndürür.
3. **oran_hesapla:** Orijinal veri ile sıkıştırılmış veri arasındaki boyut farkını analiz ederek sıkıştırma başarısını % cinsinden gösterir.

### Nasıl Çalıştırılır?
`src` klasörü altındaki `rle_proje.py` dosyası bir Python derleyicisi veya terminal üzerinden çalıştırılabilir. Program açıldığında kullanıcıdan bir metin girmesini bekler ve sonuçları ekrana yazdırır.
