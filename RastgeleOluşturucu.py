import random

def isim_olustur():
    ad=["Halil","Emrah","Mustafa"]
    soyad=["BERK","ÖZ","YILDIZ"]

    return "{} {} ".format(random.choice(ad),random.choice(soyad))

print("-"*30)

for i in range(10):
    print(isim_olustur())
print("-"*30)