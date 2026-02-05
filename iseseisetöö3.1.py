fail = open("rebased.txt", encoding="UTF-8")

vastuvõetud = []

for rida in fail:
    vastuvõetud.append(int(rida))

fail.close()
aasta = int(input("sisesta aasta arv 2011-2019:"))
print(vastuvõetud[aasta-2011])
#2022 2012 2013