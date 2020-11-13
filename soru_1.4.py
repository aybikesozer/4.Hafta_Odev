liste=[1,2,3,4,5,6,7,8,9,10]
tek=[]
çift=[]
for x in range(0,len(liste)):
    if  int(liste[x])%2==0:
        çift.append(liste[x])

    else:
        tek.append(liste[x])

print([çift,tek])
        
