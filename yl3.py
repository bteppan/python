import turtle

#Birgita Teppan
#Ülesanne 03
# Ülesanne 3.1: Tervitus
# Loo muutuja nimi, mis sisaldab kasutaja nime (string)
# Loo muutuja vanus, mis sisaldab kasutaja vanust (integer)
# Loo muutuja keskmine_hinne, mis sisaldab kasutaja keskmist hinnet (float)
# Trüki välja lause, mis ühendab kõik kolm muutujat, nt: “Karin , 18 aastat vana ja keskmine hinne on 4.7”
# Kasuta väljatrükkimisel ainult komasid (,)
name = "Imre"
age = 18
keskmine_hinne = 4.7
print(name,",",age,"aastat vana ja keskmine hinne on",keskmine_hinne)

# Ülesanne 3.3: Reisiplaan
# Loo muutuja sihtkoht, mis sisaldab reisi sihtkohta (string)
# Loo muutuja paevade_arv, mis näitab, mitu päeva reis kestab (integer)
# Loo muutuja oobimise_hind, mis näitab ühe öö hinna (float)
# Trüki välja lause, mis ühendab need andmed, nt: “Soome reis kestab 5 päeva ja üks öö maksab 30.50 eurot.”
# Kasuta väljatrükkimisel ainult komasid (,)

raamatu_pealkiri = "Sipsik"
raamatu_autor = "Eno Raud"
raamat = raamatu_pealkiri+" "+raamatu_autor
lehekylgede_arv = 16 
hindamisskoor = 7.0 
print("Minu lemmikraamat on "+raamat+",mis on "+str(lehekylgede_arv)+" pikk ja mille ma hindan "+str(hindamisskoor)+" punktiga ")

# Ülesanne 3.7: Python Turtle kolmnurk
# Loo muutuja kylje_pikkus, mis määrab kujundi külje pikkuse (täisarv)
# Loo muutuja nurk, mis määrab kujundi nurga (täisarv)
# Loo muutuja kujundi_varv, mis määrab kujundi joonevärvi (string)
# Kasutades Turtle’i, joonista kõrvuti 3 värvilist kolmnurka, mis kasutab loodud muutujaid
# Iga kolmnurk on järgmisest 1,5 korda eemal
# Testi: muuda külje pikkust ning kolmnurgad on kenasti teineteisest eemal

kylje_pikkus = 20
nurk = 120
kujundi_varv = "pink"
kordaja = 3
nihe = 1.5
turtle.color(kujundi_varv)
for i in range(kordaja):
    for i in range(kordaja):
        turtle.fd(kylje_pikkus)
        turtle.lt(nurk)
    turtle.penup()
    turtle.fd(kylje_pikkus*nihe)
    turtle.pendown()


turtle.done()