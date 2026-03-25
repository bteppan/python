import json
import requests


#Leia ametikoht, mida esineb kõige rohkem.
#Leia kõige kõrgema ja kõige madalama palgaga töötaja.
#Arvuta ettevõtte keskmine töötajate palk.
#Loetle töötajad, kes töötavad IT-osakonnas.
#Leia kõik töötajad, kelle nimi algab tähega "M".


url = f"https://metshein.com/kordamine/json/tootajad.json"
response = requests.get(url)

