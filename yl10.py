import random

 

kõik_katsed = []

 

while True:

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

 

        if kasutaja_arv < arv:

            print("Pakutud arv on liiga väike. Proovi uuesti!")

        elif kasutaja_arv > arv:

            print("Pakutud arv on liiga suur. Proovi uuesti!")

        else:

            print(f"Õige! Arvasid arvu ära {katse_arv}. katsega.")

            break

    else:

        print("Kahjuks ei suutnud sa õiget arvu ära arvata. Õige arv oli:", arv)

 

    kõik_katsed.append(katse_arv)

 

    uuesti = input("Kas soovid uuesti mängida? (jah/ei): ").strip().lower()

    if uuesti != "jah":

        print("\nMängu tulemused:")

       for _ in enumerate (kõik_katsed):
            print(f"Mäng {i+1}: arvasid ära {kõik_katsed[i]}. katsega.")


        print("Aitäh mängimast!")

        break
        
