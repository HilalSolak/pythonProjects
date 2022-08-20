#hilal solak/ 190401020
import math
text=["duran duran sang wild boys in 1984","wild boys don't remain forever wild","who brought wild flowers","it was john krakauer who wrote in to the wild"]
N = len(text)
def benzersizkelime_olusturma(text):#benzersiz kelimelerin listelerini oluşturmaya yarayan fonksiyon
    liste = []
    for i in text:
        for j in i.split():
            if j not in liste:
                liste.append(j)
    return liste
def cumle_bol(text):
    list = []
    for i in text:
        list.append(i.split())
    return list
cumleler = cumle_bol(text)
benzersiz_terimler = benzersizkelime_olusturma(text)
print(benzersiz_terimler)#benzersiz terimleri içeren listemizi yazdırdık.
def gecencumle_sayisi(text, kelime):#terimin geçtiği cümle sayısını bulma
    sayac = 0
    for i in text:
       if kelime in i.split():
           sayac += 1
    return sayac
def idf_t(text, kelime):
    idf_t = math.log10(N/gecencumle_sayisi(text, kelime))
    return idf_t
for i in cumleler:
    tfidf_listesi = []
    for j in benzersiz_terimler:
        tf_idf = i.count(j)*idf_t(text,j)
        tfidf_listesi.append(round(tf_idf,3))
    print(tfidf_listesi)