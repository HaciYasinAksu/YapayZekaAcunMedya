print("KodlamaiO")
baslik = "Taşıt Kredisi"
print(baslik)
"""String metinsel ifadeleri tutar . """
baslik = "İhtiyaç Kredisi"
"""int , integer => tam sayıları tutar ."""
vade = 36
vade = "36"

aylikodeme = 200.50
"""float, decimal,double bunların arasında değer range farkı vardır . Ondalık sayı tutarlar ."""

"""boll , doğru mu yanlış mı karar verdirir."""
yukselistemi = True
yukselistemi = False

"""matematiksel operatöreler + - * / % """
toplam = 100 + 200  # 300
fark = 200 - 100  # 100          
carpim = 100 * 200  # 20000
bolum = 200 / 100  # 2
mod = 200 % 100  # 0

print(toplam)
print(fark)
print(carpim)
print(bolum)
print(mod)

"""Operatörler bir işlemi yapmamızı sağlayan sembollerdir . """ 
"""Matematiksel operatörler + - * / % """
"""Arttırma ve azaltma operatörleri ++ -- """
"""Atama operatörleri = += -= *= /= %= """
"""Karşılaştırma operatörleri == != > < >= <= """

print(1 == 1)  # True
print(1 != 1)  # False
print(1 > 2)  # False
print(1 < 2)  # True
print(1 >= 1)  # True
print(1 <= 1)  # True

"""Mantıksal operatörler and or not """
print(1 == 1 and 1 > 2)  # False
print(1 == 1 or 1 > 2)  # True
print(not 1 == 1)  # False
"""or veya and ve not değil anlamına gelir . """
"""Önce not sonra and sonra or işlemi yapılır . Parantez içindeki işlem ise en önce yapılır . """


"""Koşullu durumlar if else elif """
"""if koşul: """
"""    yapılacak işlem """
"""elif koşul: """
"""    yapılacak işlem """
"""else: """
"""    yapılacak işlem """
"""if else elif bloklarının içine başka if else elif blokları yazılabilir . """

puan = 50
if puan >= 50:
    print("Geçtiniz")
else:
    print("Kaldınız")

sayi1 = 10
sayi2 = 15
if sayi1 > sayi2:
    print("Birinci sayı büyük")
elif sayi1 < sayi2:
    print("İkinci sayı büyük")
print("Koşul dışı")
""""Tekrardan if yazdığımız anda yeni bir blok oluşturmuş oluruz . """

"""indentation girinti demektir . Python'da kod bloklarını belirlemek için girinti kullanılır . """
"""Python'da girinti boşluklarla yapılır . """
"""Python'da girinti miktarı 4 boşluktur . """  
"""Python'da girinti miktarı aynı olmalıdır . """
