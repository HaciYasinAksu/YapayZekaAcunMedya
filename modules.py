import matematik as sx
# Alias takma isimdir.
import random
#package
from day2 import SayHello , Human 

from matematik import Topla
from matematik import Cikar
from matematik import Carp  
from matematik import Bol
#Bu şekilde de import edilebilir.Bunun sonucunda direkt fonksiyon adı yazılarak kullanılabilir.
#Bu şekilde import edildiğinde modül adı yazılmaz.
print(sx.Topla(3,4))
print(sx.Cikar(10,5))
print(sx.Carp(5,6))
print(sx.Bol(10,2))
# """Modüller fonksiyonları içerebilir . """
# """Modüller başka bir dosyadan import edilerek kullanılabilir . """  
# """Modüller import edildikten sonra içindeki fonksiyonlar kullanılabilir . """
# """Modüller import edilirken alias verilebilir . """
# """Modüller import edilirken sadece belirli fonksiyonları import etmek mümkündür . """
# """Modüller import edilirken * kullanarak tüm fonksiyonları import etmek mümkündür . """
# """Modüller import edilirken from kullanarak modül ismi yazmadan fonksiyonları kullanmak mümkündür . """

#package kullanımı pypi.org sitesinden indirilen paketlerdir.