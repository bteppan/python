<<<<<<< HEAD
# Ülesanne 10.2
# 13.01.2026
import random

def mangi_yht_mangu():
    
    arv = random.randint(1, 10)
    katse_arv = 0
    oigesti_arvatud = False

    print("Tere! Proovi ära arvata arv vahemikus 1 ja 10.")

    for _ in range(10): 
        kasutaja_arv = int(input("Sisesta oma arv: "))
        katse_arv += 1

=======
import random

kõik_katsed = []

for i in range(True):
    arv = random.randint(1, 10)
    katse_arv = 0

    print("Tere! Proovi ära arvata arv vahemikus 1 ja 10.")

    for _ in range(10):
        try:
            kasutaja_arv = int(input("Sisesta oma arv: "))
        except ValueError:
            print("Palun sisesta täisarv!")
            continue

        katse_arv += 1
>>>>>>> 8b2edab573f6975c90fb67c40ae96f29c9a36add

        if kasutaja_arv < arv:
            print("Pakutud arv on liiga väike. Proovi uuesti!")
        elif kasutaja_arv > arv:
            print("Pakutud arv on liiga suur. Proovi uuesti!")
<<<<<<< HEAD
        elif kasutaja_arv == arv:
            print(f"Õige! Arvasite arvu ära {katse_arv}. katsega.")
            break
    
    else:
        print("Kahjuks ei suutnud sa õiget arvu ära arvata. Proovi uuesti!")

    return katse_arv

def mangu_algus():
    koik_katsed = []  

    for i in range(10):  
        katse_arv = mangi_yht_mangu()
        koik_katsed.append(katse_arv)

        uuesti = input("Kas soovid uuesti mängida? (jah/ei): ").strip().lower()
        if uuesti != "jah":
            print("\Mängu tulemused:")
            for j, katse in enumerate(kõik_katsed, 1):
                print(f"Mäng {j}: Arvasite ära {katse}. katsega.")
            print("Aitäh mängimast!")
            break

    print()  
mangu_algus()
=======
        else:
            print(f"Õige! Arvasid arvu ära {katse_arv}. katsega.")
            break
    else:
        print("Kahjuks ei suutnud sa õiget arvu ära arvata. Õige arv oli:", arv)

    kõik_katsed.append(katse_arv)

    uuesti = input("Kas soovid uuesti mängida? (jah/ei): ").strip().lower()
    if uuesti != "jah":
        print("\nMängu tulemused:")

        for i in range(len(kõik_katsed)):
            print(f"Mäng {i+1}: arvasid ära {kõik_katsed[i]}. katsega.")

        print("Aitäh mängimast!")
        break
>>>>>>> 8b2edab573f6975c90fb67c40ae96f29c9a36add
