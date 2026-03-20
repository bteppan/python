import os
from datetime import date
print(f"Hello {os.getlogin()}")
print(f"Sinu kataloogitee: {os.getcwd()}")
today = date.today()
try:
    os.mkdir(str(today))
except:
    print("ära jama, juba olemas")
mitu = int(input("Mitu kataloogi tahad teha: "))
for i in range(mitu):
    os.mkdir(str(today)+"/"+str(i+1))
    print(f"Kataloogid 1-{mitu} tehtud")
kustuta = input(f"Kustuta valikust 1-{mitu}:")
path = os.getcwd()+'\\'+str(today)+'\\'+kustuta
if os.path.isdir(path):
    os.rmdir(path)