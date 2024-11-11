import random

def sayi_tahmin_oyunu(): 

    rastgele_sayi = random.randint(1, 100)
    deneme_sayisi = 0

    print("1 ile 100 arasında bir sayı tahmin edin!")
    while True:
        try:
            tahmin = int(input("Tahmininiz: "))
            deneme_sayisi += 1
        except ValueError:
            print("Lütfen geçerli bir sayı girin!")
            continue
        if tahmin < rastgele_sayi:
            print("Daha büyük bir sayı tahmin edin.")
        elif tahmin > rastgele_sayi:
            print("Daha küçük bir sayı tahmin edin.")
        else:
            print(f"Tebrikler! Doğru tahmin ettiniz. Toplam deneme sayınız: {deneme_sayisi}")
            break
sayi_tahmin_oyunu()
 