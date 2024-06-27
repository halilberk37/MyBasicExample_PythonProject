def bubble_sort(array):
    for i in range(1,len(array)):
        for a in range(len(array)-i):
            if array[a]>array[a+1]:
                b=array[a]
                array[a]=array[a+1]
                array[a+1]=b
    return array

adet = int(input("Kaç adet sayı girmek istiyorusunuz: "))
sayilar=[]

for x in range(adet):
    sayilar.append(int(input("Sayı Giriniz: ")))

print("Girdiğiniz sayilar: ",sayilar)
print("Küçükten büyüğe sıralanmış hali: ")
print("{}".format(bubble_sort(sayilar)))