


sayi = int(input("sayı giriniz: "))
def asal_mi (sayi):
    if sayi == 1 :
        print(str(sayi) + " asal değildir") 
    elif sayi == 2:
        print(str(sayi) + " asaldır") 
    else:
        for i in range(2,sayi):
            if sayi % i == 0:
                print(str(sayi) + " asal değildir") 
                break
            else :
                print(str(sayi) + " asaldır")
                break
asal_mi(sayi)

        
"""Burada sayının asal olma kurallarını oluşturmak için önce 1 olduğunu kontrol ettik çünkü 1 asal sayı olamayabilen en küçük sayırıdır"""
""""Daha sonra asal olan en küçük sayı olan 2 yi aldık ve 2 den başlayarak kalan sayıları mod operatorü ile kontrol ettik"""

print ("****************************************************************************************************")




print ("****************************************************************************************************")
print("İşlem yapmak istediğiniz sayıları giriniz  , sayı ekleme işlemini bitirdikten sonra bitti yazıp yapmak istediğiniz işlem türünü giriniz: ")
array_sayilar = []
array_sayilar2 = []
islem_tipi = (input("işlem tipi giriniz (Toplama için 1 , Çıkarma için 2  ,Bölme için 3,  Çarpma için 4 giriniz :) "))
islem_yapilacak_sayi = input("işlem yapılacak sayıları giriniz , eklemeyi bitirmek için bitti harfi gönderiniz: ")


def sayi_islem():
    if islem_tipi =="1":
        toplam = 0
        for i in array_sayilar:
            toplam += i
        print("Toplam: " + str(toplam))
    elif islem_tipi =="2":
        cikarma = 0
        for i in array_sayilar:
            cikarma -= i
        print("Çıkarma: " + str(cikarma))
    elif islem_tipi =="3":
        bolme = 0
        for i in array_sayilar:
            bolme /= i
        print("Bölme: " + str(bolme))
    elif islem_tipi =="4":
        carpma = 1
        for i in array_sayilar:
            carpma *= i
        print("Çarpma: " + str(carpma))
    else:
        print("Hatalı işlem tipi girdiniz")

def sayi_ekle():
    if islem_yapilacak_sayi != "bitti":
        array_sayilar.append(int(islem_yapilacak_sayi))
        islem_yapilacak_sayi = input("işlem yapılacak sayıları giriniz , eklemeyi bitirmek için bitti harfi gönderiniz: ")
    print("döngü bitti: ")


sayi_ekle()
sayi_islem()
