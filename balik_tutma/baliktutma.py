import random
import time


def balikTut():
    # burada boş bulunmasının sebebi boş değeri gelince ıska olarak görüp balık yakalamadığınızı dönecek.
    balikListe = {1: "Levrek",
         2: "Sardalya",
         3: "Hamsi",
         4: "Ton Balığı",
         5: "boş"
         }
    balik_miktari = 0
    cevap = input("Balık tutmak ister misiniz? : ")
    cevap = str(cevap.lower())
    if cevap == "evet":
        print("Olta atılıyor...")
        time.sleep(2)
        # Rastgele 1-5 arası sayıları çekiyorum. 5 değeri boş çekmeyi temsil ediyor.
        # Gelen değerler hangi balığın tutulduğunu gösteriyor.
        rastgele_deger = random.randint(1, 5)
        if rastgele_deger == int(rastgele_deger):
            # get fonksiyonu ile veride 1 2 3 4 5 şeklinde etiketlenen değerleri çekiyorum.
            bos_deger = balikListe.get(rastgele_deger)
            if bos_deger == "boş":
                print("Maalesef oltadaki yem ile balıkları beslediniz.")
                print("Balık Miktarı: ", balik_miktari)
            else:
                balik_miktari += 1
                print("Tebrikler! Yakaladığınız balık: ", bos_deger)
                print("Balık Miktarı: ", balik_miktari)

    elif cevap == 'hayır' or cevap == 'hayir':
        print("Bugün balık tutmak istemiyorsunuz. Tekrardan görüşmek üzere....")

    else:
        print("Hatalı değer girişi yaptınız. Lütfen evet/hayır cevabı verin.")


if __name__ == '__main__':
    balikTut()