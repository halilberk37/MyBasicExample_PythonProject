def cevir(metin,sayi=[]):
    for i in range(len(metin)-1,-1,-1):
        sayi.append(metin[i])
    return "".join(sayi)

cumle=input("Bir cümle giriniz: ")
print("Tersi: {}".format(cevir(cumle)))