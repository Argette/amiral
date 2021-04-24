import random
import os

harf = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
sayi = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
saha = []
sahakapali=[]
saha1=[]
saha1kapali=[]
isabet=0
isabet1=0

for i in range (0,100):
    sahakapali+=[0]
    saha1kapali+=[0]

#rastgele bir koordinat verir
def rast():
    a=random.randint(0,9)
    b=random.randint(1,10)
    return harf[a]+str(b)

#girilen listeyi sıfırlar
def sifirla(a=list):
    for i in range(0, 100):
        a += [1]

#girilen 100lük listeyi saha olarak yazar
def bas(am=list):
    print(" ", end=" ")
    for a in range(1, 11):
        print(a, end="  ")
    print("")
    for b in range(0, 10):
        print(harf[b], end=" ")
        for b1 in range(b * 10, (b + 1) * 10):
            print(am[b1], end="  ")

        print("")
    print("")

#koordinattaki satiri verir
def satir(a=str):
    for i in a:
        if i in harf:
            b=i
    return b

#koordinattaki sütunu verir
def sütun(a=str):
    if len(a) == 3:
        return 10
    else:
        for i in a :
            if i in harf:
                c=" "
            elif i in sayi:
                c=i
                break
        return c

#koordinatı indexe çeviriyor
def cev(a=str) :
        return harf.index(satir(a))*10+int(sütun(a))-1

#aynı sırada ve farklı mı diye kontrol ediyor
def kon(a=str,b=str):
    if (sütun(a)==sütun(b)) != (satir(a)==satir(b)):
        return True
    else:
        return False

#iki nokta arası uzaklik
def uzun(a=str,b=str):
    if kon(a,b):
        if satir(a)==satir(b):
            return abs(int(sütun(a)) - int(sütun(b)))+1
        elif sütun(a)==sütun(b):
            return abs(harf.index(satir(a)) - harf.index(satir(b)))+1

#iki aynı sıradaki nokta ve aralarında kalan noktaların indexlerini verir
def yerles01(b=str,c=str):
    a=[]
    if kon(b,c):
        if sütun(b)==sütun(c):
            if cev(b)<cev(c):
               for i in range(cev(b),cev(c)+1,10):
                   a+=[i]
               return a
            elif cev(c)<cev(b):
               for i in range(cev(c), cev(b) + 1, 10):
                   a+=[i]
               return a
        elif satir(b)==satir(c):
            if cev(b)<cev(c):
               for i in range(cev(b),cev(c)+1,1):
                   a+=[i]
               return a
            elif cev(c)<cev(b):
               for i in range(cev(c), cev(b) + 1, 1):
                   a+=[i]
               return a

#girilen iki koordinat arası boş mu diye bakar
def musait(d=list,a=str,b=str):
    c=yerles01(a,b)
    for i in c :
        if d[i]==2:
            return False
            break
    return True

#girilen yazının geçerli bir koordinat olup olmadığını söyler
def uygun(a=str):
    b=0
    c=0
    d=0
    if len(a)==2:
        for i in a:
            if i in harf:
                b+=1
            if i in sayi:
                c+=1
        if c==1 and b==1 and saha1kapali[cev(a)]==0:
            return True
    elif len(a)==3:
        for i in a:
            if i in harf:
                b+=1
            if i=="1":
                c+=1
            if i=="0":
                d+=1
        if c==1 and b==1 and d==1 and saha1kapali[cev(a)]==0:
            return True

#girilen listenin girilen noktalar ve aralarındaki noktalarını yerlestirir
def yerles(a=list,b=str,c=str):
    if kon(b,c):
        if musait(a,b,c):
            for i in yerles01(b,c):
                a[i]=2

#girilen koordinata daha önce atış yapılmamış , içeriği bilinmiyorsa atış yapar ve görünen sahaya yerleştirir
def atis(a=str):
    global isabet
    b=cev(a)
    if saha1kapali[b]==0:
        saha1kapali[b]=saha1[b]
        if saha1[b]==2:
            saha1[b]=3
            saha1kapali[b]=3
            isabet+=1
            print("Tebrikler isabetli")
        elif saha1[b]==1:
            print("Iskaladın")

#bilgisayar atış yapar
def atis1():
    abc = None
    komsu = []
    global isabet1
    for i in range(0, 100):
        if sahakapali[i] == 3:
            if (i % 10 != 0 and sahakapali[i - 1] == 0) or ((i - 9) % 10 != 0 and sahakapali[i + 1] == 0) or (
                    i + 10 <= 100 and sahakapali[i + 10] == 0) or (i - 10 >= 0 and sahakapali[i - 10] == 0):
                abc = True

    if abc == True:
        for i in range(0, 100):
            if sahakapali[i] == 3:
                if (i % 10 != 0 and sahakapali[i - 1] == 0) or ((i - 9) % 10 != 0 and sahakapali[i + 1] == 0) or (
                        i + 10 <= 100 and sahakapali[i + 10] == 0) or (i - 10 >= 0 and sahakapali[i - 10] == 0):
                    break
        if i % 10 != 0 and sahakapali[i - 1] == 0:
            komsu += [i - 1]
        if (i - 9) % 10 != 0 and sahakapali[i + 1] == 0:
            komsu += [i + 1]
        if i + 10 <= 100 and sahakapali[i + 10] == 0:
            komsu += [i + 10]
        if i - 10 >= 0 and sahakapali[i - 10] == 0:
            komsu += [i - 10]
        a = komsu[0]
        sahakapali[a] = saha[a]
        if saha[a] == 2:
            saha[a] = 3
            sahakapali[a] = 3
            isabet1 += 1
            print("Ben vurdum")
        elif saha[a] == 1:
            print("Iskaladım")

    else:

        while True:
            b = cev(rast())
            if sahakapali[b] == 0:
                sahakapali[b] = saha[b]
                break

        if saha[b] == 2:
            saha[b] = 3
            sahakapali[b] = 3
            isabet1 += 1
            print("Ben vurdum")
        elif saha[b] == 1:
            print("Iskaladım")

#oyuncudan koordinatlar istenip sahasına  gemilerini yerleştirir
def basla():
    sifirla(saha)
    bas(saha)
    while True:
        a =str(input("2 karelik bir gemi için ilk koordinatı giriniz"))
        while True:
            if uygun(a):
                break
            else:
                a = input("hatalı giriş,lütfen uygun bir koordinat giriniz ")
        b =str(input("2 karelik bir gemi için ikinci koordinatı giriniz"))
        while True:
            if uygun(b):
                break
            else:
                b = input("hatalı giriş,lütfen uygun bir koordinat giriniz ")
        if kon(a,b):
            if uzun(a,b)==2:
                if musait(saha,a,b):
                    yerles(saha,a,b)
                    break

        print("hatalı lütfen tekrar")
    os.system("cls")
    bas(saha)
    while True:
        a =str(input("3 karelik bir gemi için ilk koordinatı giriniz"))
        while True:
            if uygun(a):
                break
            else:
                a = input("hatalı giriş,lütfen uygun bir koordinat giriniz ")
        b =str(input("3 karelik bir gemi için ikinci koordinatı giriniz"))
        while True:
            if uygun(b):
                break
            else:
                b = input("hatalı giriş,lütfen uygun bir koordinat giriniz ")
        if kon(a,b):
            if uzun(a,b)==3:
                if musait(saha,a,b):
                    yerles(saha,a,b)
                    break

        print("hatalı lütfen tekrar")
    os.system("cls")
    bas(saha)

    while True:
        a =str(input("3 karelik bir gemi için ilk koordinatı giriniz"))
        while True:
            if uygun(a):
                break
            else:
                a = input("hatalı giriş,lütfen uygun bir koordinat giriniz ")
        b =str(input("3 karelik bir gemi için ikinci koordinatı giriniz"))
        while True:
            if uygun(b):
                break
            else:
                b = input("hatalı giriş,lütfen uygun bir koordinat giriniz ")
        if kon(a,b):
            if uzun(a,b)==3:
                if musait(saha,a,b):
                    yerles(saha,a,b)
                    break

        print("hatalı lütfen tekrar")
    os.system("cls")
    bas(saha)

    while True:
        a =str(input("4 karelik bir gemi için ilk koordinatı giriniz"))
        while True:
            if uygun(a):
                break
            else:
                a = input("hatalı giriş,lütfen uygun bir koordinat giriniz ")
        b =str(input("4 karelik bir gemi için ikinci koordinatı giriniz"))
        while True:
            if uygun(b):
                break
            else:
                b = input("hatalı giriş,lütfen uygun bir koordinat giriniz ")
        if kon(a,b):
            if uzun(a,b)==4:
                if musait(saha,a,b):
                    yerles(saha,a,b)
                    break

        print("hatalı lütfen tekrar")
    os.system("cls")
    bas(saha)


    while True:
        a = str(input("5 karelik bir gemi için ilk koordinatı giriniz"))
        while True:
            if uygun(a):
                break
            else:
                a = input("hatalı giriş,lütfen uygun bir koordinat giriniz ")
        b = str(input("5 karelik bir gemi için ikinci koordinatı giriniz"))
        while True:
            if uygun(b):
                break
            else:
                b = input("hatalı giriş,lütfen uygun bir koordinat giriniz ")
        if kon(a, b):
            if uzun(a, b) ==5:
                if musait(saha, a, b):
                    yerles(saha, a, b)
                    break

        print("hatalı lütfen tekrar")
    os.system("cls")

#bilgisayarın sahasına gemiler yerleştirilir
def basla1():
    sifirla(saha1)
    while True:
        a=rast()
        b=rast()
        if kon(a,b):
            if uzun(a,b)==2:
                if musait(saha1,a,b):
                    yerles(saha1,a,b)
                    break


    while True:
        a=rast()
        b=rast()
        if kon(a,b):
            if uzun(a,b)==3:
                if musait(saha1,a,b):
                    yerles(saha1,a,b)
                    break


    while True:
        a=rast()
        b=rast()
        if kon(a,b):
            if uzun(a,b)==3:
                if musait(saha1,a,b):
                    yerles(saha1,a,b)
                    break


    while True:
        a=rast()
        b=rast()
        if kon(a,b):
            if uzun(a,b)==4:
                if musait(saha1,a,b):
                    yerles(saha1,a,b)
                    break


    while True:
        a=rast()
        b=rast()
        if kon(a,b):
            if uzun(a,b)==5:
                if musait(saha1,a,b):
                    yerles(saha1,a,b)
                    break
    #bas(saha1)

#atış yapma hakkı için matematik işlemi sorar
def soru(a=int):
    s="dsadad"
    if a==1:
        b=random.randint(1,4)
        if b==1:
            c=random.randint(11,99)
            d=random.randint(11,99)
            t = "{}+{}=?".format(c, d)
            while s.isnumeric()!=True:
                s=input(t)
            if int(s)==c+d:
                return True
        elif b==2:
            c = random.randint(11, 70)
            d = random.randint(c, 99)
            t = "{}-{}=?".format(d,c)
            while s.isnumeric()!=True:
                s=input(t)
            if int(s)==d-c:
                return True
        elif b==3:
            c = random.randint(2,10)
            d = random.randint(2,10)
            t = "{}x{}=?".format(c, d)
            while s.isnumeric()!=True:
                s=input(t)
            if int(s)==c*d:
                return True


        elif b==4:
            c = random.randint(2, 10)
            d = random.randint(2, 10)*c
            t = "{}/{}=?".format(d,c)
            while s.isnumeric()!=True:
                s=input(t)
            if int(s) == d/c:
                return True
    elif a==2:
        b = random.randint(1, 4)
        if b == 1:
            c = random.randint(111, 999)
            d = random.randint(111, 999)
            t = "{}+{}=?".format(c, d)
            while s.isnumeric()!=True:
                s=input(t)
            if int(s) == c + d:
                return True
        elif b == 2:
            c = random.randint(111, 700)
            d = random.randint(c, 990)
            t = "{}-{}=?".format(d, c)
            while s.isnumeric()!=True:
                s=input(t)
            if int(s) == d - c:
                return True
        elif b == 3:
            c = random.randint(12,40)
            d = random.randint(12,40)
            t = "{}x{}=?".format(c,d)
            while s.isnumeric()!=True:
                s=input(t)
            if int(s) == c * d:
                return True
        elif b == 4:
            c = random.randint(10,30)
            d = random.randint(12, 30) * c
            t = "{}/{}=?".format(d, c)
            while s.isnumeric()!=True:
                s=input(t)
            if int(s) == d / c:
                return True
    elif a==3:
        b = random.randint(1, 6)
        if b == 1:
            c = random.randint(1111, 9999)
            d = random.randint(1111, 9999)
            t = "{}+{}=?".format(c, d)
            while s.isnumeric()!=True:
                s=input(t)
            if int(s) == c + d:
                return True
        elif b == 2:
            c = random.randint(1111, 7000)
            d = random.randint(c, 9909)
            t = "{}-{}=?".format(d, c)
            while s.isnumeric()!=True:
                s=input(t)
            if int(s) == d - c:
                return True
        elif b == 3:
            c = random.randint(20,100)
            d = random.randint(20,100)
            t = "{}x{}=?".format(c, d)
            while s.isnumeric()!=True:
                s=input(t)
            if int(s) == c * d:
                return True
        elif b == 4:
            c = random.randint(20, 70)
            d = random.randint(20, 70) * c
            t = "{}/{}=?".format(d, c)
            while s.isnumeric()!=True:
                s=input(t)
            if int(s) == d / c:
                return True
        elif b == 5:
            c = random.randint(5,50)
            d = random.randint(c,1000)
            t = "{}%{}=?".format(d, c)
            while s.isnumeric()!=True:
                s=input(t)
            if int(s) == d%c:
                return True
        elif b == 6:
            c = random.randint(3,4)
            d = random.randint(5,10)
            t = "{}^{}=?".format(d,c)
            while s.isnumeric()!=True:
                s=input(t)
            if int(s)==d**c:
                return True


os.system("cls")
print("Merhaba 10x10 sahada 1 adet 2 birim 2 adet 3 birim 1 adet 4 birim ve 1 adet 5 birim uzunluktaki gemilerle oynayacağız")
print("")
print("0 henüz atış yapmadığın için içeriğini bilmediğin ,1 boş ,2 dolu ,3 ise isabet ettirilmiş karelerdir ")
print("")
abc=input("hazırsan bas ve  başlayalım")
print("")
c=input("zorluk seçiniz 1 kolay ; 2 orta ; 3 zor:")
basla1()
basla()


while isabet<17 and isabet1<17:
    print("Senin Sahan")
    bas(saha)
    print("")
    print("kalan gemi karesi sayısı={}".format(17-isabet1))
    print("")
    print("Benim Saham")
    bas(saha1kapali)
    print("")
    print("kalan gemi karesi sayısı={}".format(17 - isabet))
    print("")
    print("atış yapabilmek için bu soruyu doğru cevapla")
    print("")
    if soru(int(c)):
        X = input("atış yapmak için koordinat giriniz:")
        while True:
            if uygun(X):
                break
            else:
                X = input("hatalı giriş,lütfen uygun bir koordinat giriniz ")

        os.system("cls")
        atis(X)
    else:
        os.system("cls")

    atis1()
    print("")


os.system("cls")
if isabet1==17:
    print("Ben Kazandım ")

elif isabet==17:
    print("Tebrikler Kazandın!!! ")

bos=input()