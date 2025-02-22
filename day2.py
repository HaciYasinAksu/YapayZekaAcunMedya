faiz = 1.59
vade = "36"
krediAdi  = "İhtiyaç Kredisi"
vade = int(vade)
print(vade)
print(vade +12)

# Python'da veri tipi dönüşümü (type conversion) yapmak için çeşitli yerleşik fonksiyonlar kullanabilirsiniz. İşte bazı yaygın dönüşüm fonksiyonları ve örnek kullanımları:

# int(): Bir değeri tam sayıya dönüştürür.
# float(): Bir değeri ondalık sayıya dönüştürür.
# str(): Bir değeri string'e dönüştürür.
# bool(): Bir değeri boolean'a dönüştürür.
# Örneğin, day2.py dosyanızdaki vade değişkenini string'den tam sayıya dönüştürmek için int() fonksiyonunu kullanabilirsiniz:

vade = 45 #input("Vadeyi giriniz: ")
vade = int(vade)
print(vade) 
print(type(vade))  # <class 'int'>
# Bu kod, kullanıcıdan bir vade girmesini ister ve bu değeri int() fonksiyonuyla tam sayıya dönüştürür. Ardından, vade değişkeninin türünü kontrol etmek için type() fonksiyonunu kullanırız. Bu kodu çalıştırdığınızda, vade değişkeninin int türünde olduğunu göreceksiniz.   

#string interpolation
# String interpolation, bir string içinde değişkenleri veya ifadeleri yerleştirmek için kullanılan bir tekniktir. Python'da string interpolation yapmanın birkaç yolu vardır. İşte bunlardan bazıları:
#format() metodu ile string interpolation yapmak için süslü parantezler {} kullanabilirsiniz. Örneğin:
# vade = "36" 
# print("Vade : {}".format(vade))
# Bu kod, vade değişkenini süslü parantezler {} içine yerleştirir ve format() metoduyla string interpolation yapar. Bu kodu çalıştırdığınızda, "Vade : 36" çıktısını göreceksiniz.

isim  = "Halit"
metin = "Merhaba {name}".format(name=isim)
print(metin)
# Bu kod, format() metoduyla string interpolation yapar. Bu kodu çalıştırdığınızda, "Merhaba Halit" çıktısını göreceksiniz.

#f-string ile string interpolation yapmak için süslü parantezler {} kullanabilirsiniz. Örneğin:
isim = "Halit"
metin = f"Merhaba {isim}"
print(metin)
# Bu kod, f-string ile string interpolation yapar. Bu kodu çalıştırdığınızda, "Merhaba Halit" çıktısını göreceksiniz.

print(f"Vade : {vade}") # python 3.6 ve sonrasında gelmiştir.
print("Vade : {}".format(vade))
print("Vade : " + str(vade))
print("Vade : %s" % vade) #eski tip kullanım
# Bu kodlar, f-string, format() metodu ve string concatenation ile string interpolation yapar. Bu kodları çalıştırdığınızda, "Vade : 36" çıktısını göreceksiniz.
print("-----------------")
#listeler  => list 
#Listeler, birden çok değeri tek bir değişken içinde saklamak için kullanılır. Python'da listeler köşeli parantez [] içinde tanımlanır. İşte bir liste örneği:
krediler = ["Taşıt Kredisi", "Konut Kredisi", "İhtiyaç Kredisi"]
print(krediler)
print(krediler[0])  # Taşıt Kredisi
print(krediler[1])  # Konut Kredisi
print(type(krediler))  # <class 'list'> 
print(len(krediler))  # 3
# Bu kod, krediler adında bir liste tanımlar ve bu listenin elemanlarına erişir. Bu kodu çalıştırdığınızda, listenin elemanlarını ve türünü göreceksiniz. Ayrıca, len() fonksiyonunu kullanarak listenin eleman sayısını da görebilirsiniz. 

dizi = [1, "Merhaba", 23.4, True, 5]
print(dizi)
#liste elemanları farklı türde olabilir.
# Bu kod, farklı türdeki elemanları olan bir liste tanımlar. Bu kodu çalıştırdığınızda, listenin elemanlarını göreceksiniz.
krediler.append("Özel Kredi")
print(krediler)

krediler.pop()
krediler.pop()
#pop metodu listenin son elemanını siler. Eğer bir parametre verilirse, o indeksteki elemanı siler. 
print(krediler)

#extend metodu ile listeye eleman eklemek bir diziyi diziye eklemek için kullanılır.
krediler.extend(["Özel Kredi", "Tatil Kredisi"])
print(krediler) 

#insert metodu ile listeye eleman eklemek
krediler.insert(0, "Eğitim Kredisi")
print(krediler)

#remove metodu ile listeye eleman silmek
krediler.remove("Eğitim Kredisi")
print(krediler)

#clear metodu ile listeyi temizlemek
krediler.clear()
print(krediler)

#copy metodu ile listeyi kopyalamak
krediler = ["Taşıt Kredisi", "Konut Kredisi", "İhtiyaç Kredisi"]
krediler2 = krediler.copy()
print(krediler2)

#count metodu ile listede kaç tane belirli bir eleman olduğunu bulmak
print(krediler.count("Taşıt Kredisi"))

#index metodu ile belirli bir elemanın indeksini bulmak
print(krediler.index("Konut Kredisi"))

#sort metodu ile listeyi sıralamak
krediler.sort()
print(krediler)

#reverse metodu ile listeyi ters çevirmek
krediler.reverse()
print(krediler)

#format metodu ile listeyi biçimlendirmek
print("Krediler : {}".format(krediler)) 

#list comprehension
#List comprehension, bir liste oluşturmak için kullanılan kısayol bir tekniktir. List comprehension kullanarak, bir döngü kullanmadan bir liste oluşturabilirsiniz. İşte bir list comprehension örneği:
sayilar = [1, 2, 3, 4, 5]
kareler = [sayi ** 2 for sayi in sayilar]
print(kareler)
# Bu kod, sayilar adında bir liste tanımlar ve bu listenin elemanlarının karelerini alarak yeni bir liste oluşturur. Bu kodu çalıştırdığınızda, kareler listesini göreceksiniz.

#range fonksiyonu
#range() fonksiyonu, belirli bir aralıktaki sayıları içeren bir liste oluşturmak için kullanılır. İşte range() fonksiyonunun kullanımı:
sayilar = list(range(1, 6))
print(sayilar)
# Bu kod, 1 ile 6 arasındaki sayıları içeren bir liste oluşturur. Bu kodu çalıştırdığınızda, sayilar listesini göreceksiniz.

#tuple
#Tuple, listelere benzer ancak değiştirilemez (immutable) bir veri yapısıdır. Tuple'lar, normal parantez () içinde tanımlanır. İşte bir tuple örneği:
kredilerTuple = ("Taşıt Kredisi", "Konut Kredisi", "İhtiyaç Kredisi")
print(kredilerTuple)

#qey: tuple'lar değiştirilemez olduğu için, tuple'lar üzerinde append(), insert(), remove(), pop(), clear(), sort(), reverse() gibi değiştirme işlemleri yapamazsınız.
 
#for döngüsü
#For döngüsü, bir dizi veya liste üzerinde döngü yapmak için kullanılır. İşte bir for döngüsü örneği:
for kredi in krediler:
    print(kredi)

for sayi in range(1, 6):
    print(sayi)
# Bu kod, 1 ile 6 arasındaki sayıları ekrana yazdırır. Bu kodu çalıştırdığınızda, 1, 2, 3, 4 ve 5 sayılarını göreceksiniz.

for i in range(0, 10, 2):
    print(i)
# Bu kod, 0 ile 10 arasındaki sayıları 2'şer 2'şer artırarak ekrana yazdırır. Bu kodu çalıştırdığınızda, 0, 2, 4, 6 ve 8 sayılarını göreceksiniz. 
i = 0
while i < 10:
    print("x")
    i += 1

print("Döngü bitti")
while True:
    print("Merhaba")
    break

# Bu kod, sonsuz bir döngü oluşturur ve "Merhaba" yazısını ekrana yazdırır. Bu kodu çalıştırdığınızda, ekranda "Merhaba" yazısını göreceksiniz. 
i = 0
while i < len(krediler):
    print(krediler[i])
    i += 1
    if krediler[i] == "Konut Kredisi":
        break
# Bu kod, krediler listesindeki elemanları ekrana yazdırır. Bu kodu çalıştırdığınızda, krediler listesindeki elemanları göreceksiniz. 

#continue anahtar kelimesi, döngüde bir sonraki adıma geçmek için kullanılır. 

#fonksiyonlar
#Fonksiyonlar, belirli bir işlevi yerine getirmek için kullanılan bloklardır. Python'da fonksiyonlar def anahtar kelimesiyle tanımlanır. İşte bir fonksiyon örneği:

fiyat = 100
indirim = 20
#definition define etmek anlamına gelir. 
def calculateWithParams(fiyat,indirim):
    return fiyat - indirim
print(calculateWithParams(fiyat,indirim))

def SayHello(isim):
    print(f"Hello {isim}")
SayHello("Halit")

def calculateAndReturn(price ,discount):
    return price - discount

#Her fonksiyonun bir geri dönüş değeri olmayabilir. Geri dönüş değeri olmayan fonksiyonlar None döner.
#Her fonksiyon kendine ait bir scope'a sahiptir. Yani fonksiyon içinde tanımlanan değişkenler fonksiyon dışında erişilemez.
#Fonksiyonlar, başka bir fonksiyon içinde tanımlanabilir. Bu tür fonksiyonlara iç içe fonksiyonlar denir.
#Fonksiyonlar, bir değişken olarak atanabilir. Bu tür fonksiyonlara lambda fonksiyonlar denir.  
yenifiyat = calculateAndReturn(200,50)
print(yenifiyat)

#class
#Sınıflar, nesne tabanlı programlamada kullanılan bir yapıdır. Sınıflar, bir nesnenin özelliklerini (attributes) ve davranışlarını (methods) tanımlar. Python'da sınıflar class anahtar kelimesiyle tanımlanır. 

#Moduller ve paketler
#Modüller, Python'da kodunuzu organize etmek ve tekrar kullanılabilirliği artırmak için kullanılan bir yapıdır. Modüller, bir veya daha fazla fonksiyon, sınıf veya değişken içerebilir. Python'da modüller .py uzantılı dosyalarda tanımlanır. Modüller, başka bir Python dosyasında import anahtar kelimesiyle içe aktarılabilir. 

#Paketler, modüllerin bir araya getirilmesiyle oluşturulan bir yapıdır. Paketler, bir veya daha fazla modül içerebilir. Python'da paketler, bir dizin içinde __init__.py dosyası oluşturularak tanımlanır. Paketler, başka bir Python dosyasında import anahtar kelimesiyle içe aktarılabilir.

class Human:
    name = "Halit"
    #built-in fonksiyonlar 
    def __init__(self,name):
        self.name = name
        print("Constructor çalıştı")
    #Yapıcı metot, bir sınıfın örneğini oluşturduğunuzda otomatik olarak çalışan bir metottur. Yapıcı metot, __init__() adıyla tanımlanır. Bu metot, sınıfın özelliklerini başlatmak için kullanılır.i

    def  __str__(self) -> str:
        return self.name
    #__str__() metodu, bir nesnenin dize temsilini döndürmek için kullanılır. Bu metot, bir nesnenin print() fonksiyonuyla yazdırıldığında çağrılır. Bu metot, nesnenin dize temsilini döndürmelidir.
        pass
    def talk(self,sentence):
        print(f"Talking: {sentence}")
    def walk(self,sentence):
        print(f"Walking: {sentence}")
    def fonk1(self):
        print(f"{self.name}")
#Rezerve parametre self, sınıfın kendisini temsil eder. Bu parametre, sınıfın özelliklerine ve metotlarına erişmek için kullanılır.
#Self anahtar kelimesi, bir sınıfın metotlarında kullanılan bir parametredir. Self anahtar kelimesi, bir sınıfın özelliklerine ve metotlarına erişmek için kullanılır.
#Metotlarına erişmek demek bizim yazdığımız fonksiyonun içindeki fonksiyonlara erişmek için gereklidir . Diğer dillerde this anahtar kelimesi kullanılır.
#Bu kod, Human adında bir sınıf tanımlar ve bu sınıfın talk() ve walk() adında iki metodu vardır. Bu kodu çalıştırdığınızda, sınıfın özelliklerini ve davranışlarını göreceksiniz.
#instance oluşturmak , sınıfın bir örneğini oluşturmak anlamına gelir.
human1 = Human("Ayhan") #instance  burda newlemiş oluyoruz.
human1.talk("Merhaba")
human1.fonk1()
human1.name = "Ali"
human1.fonk1()
print(human1) # __str__ metodu çalışır. 
#Built-in fonksiyonlar içinde konfigürasyonlar yapılabilir. 

#Modüller, Python'da kodunuzu organize etmek ve tekrar kullanılabilirliği artırmak için kullanılan bir yapıdır. Modüller, bir veya daha fazla fonksiyon, sınıf veya değişken içerebilir. Python'da modüller .py uzantılı dosyalarda tanımlanır. Modüller, başka bir Python dosyasında import anahtar kelimesiyle içe aktarılabilir.
#Paketler, modüllerin bir araya getirilmesiyle oluşturulan bir yapıdır. Paketler, bir veya daha fazla modül içerebilir. Python'da paketler, bir dizin içinde __init__.py dosyası oluşturularak tanımlanır. Paketler, başka bir Python dosyasında import anahtar kelimesiyle içe aktarılabilir.

