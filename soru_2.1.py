demet=(1,1,1,2,2,3,3,"ali","ali",3.14,3.14)
liste=[]
for x in range(0,len(demet)):
    if demet[x] not in liste:
        liste.append(demet[x])
print(liste)
