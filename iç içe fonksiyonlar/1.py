def dis_fonk():
    print("Dış fonksiyon çalışıyor")

    def ic_fonk():
        print("İç fonksiyon çalışıyor")
    print("Dış fonksiyon sonlanıyor")
    ic_fonk()


# dis_fonk()


def hesaplamalar(x):
    def kare_al(a):
        return a**2

    def karekok_al(a):
        return a**0.5

    def faktoriyel(a):
        carpim = 1
        for i in range(1, a+1):
            carpim *= i
        return carpim
    kare = kare_al(x)
    karekok = karekok_al(x)
    fakt = faktoriyel(x)
    return f"Karesi: {kare} - Karekökü: {karekok} - Faktöriyeli: {fakt}"


print(hesaplamalar(6))


def toplam_carpim(*args):  # sayısı belirsiz parametre - args bir demet olarak depolanır
    def toplam(demet):
        return sum(demet)

    def carpma(demet):
        carpim = 1
        for i in demet:
            carpim *= i
        return carpim

    return f"Toplamları: {toplam(args)} - Çarpımları: {carpma(args)} "


print(toplam_carpim(2, 4, 5))


def project1():
    return


def project2():
    return


# project1()

# project2()
