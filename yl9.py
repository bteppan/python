#BT 15.12.2025
# Ülesanded 9
import random

    print(random.randint(1,99))
    
#kuva arvud 1-42
for i in range(1,43):
    if i%3==0 and i%5==0:
       print("TIKTOK")
    elif i%3==0: 
       print("TAK")
    elif i%5==0:
      print("TAK")
        
nimed = ['Martin', 'Tõnu', 'Andres', 'Tõnu', 'Andres', 'Andres', 'Andres', 'Tõnu', 'Marko', 'Mari', 'Jüri', 'Liis', 'Marko', 'Piret', 'Anu']
puhas = []
for nimi in nimed:
    if nimi not in puhas:
        puhas.append(nimi)
        
print(puhas)