a=input("string giriniz:")
liste=list(a)
liste1=[]
sözlük={}
for n in range(0,len(liste)):
    if liste[n] not in liste1:
        liste1.append(liste[n])
        for i in range (0,len(liste1)):
            harf=liste1[i]
            sayı=liste.count(liste1[i])
    sözlük[harf]=sayı
print(sözlük)
