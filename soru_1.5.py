barcelona_oyuncu=[]
for x in range(1,6):
    isim=input("İsim:")
    soy_isim=input("Soy İsim:")
    takım=input("Takımı:")
    if takım=="barcelona" or takım=="Barcelona":
        barcelona_oyuncu.append([isim,soy_isim,takım])
print(barcelona_oyuncu)
    
