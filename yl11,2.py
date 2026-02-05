# ülesanne 11
#Birgita Teppan
import turtle

def pikim_sona(list):
    pikimArv = 0
    pikimNimi = ""
    for i in list:
        if len(i) > pikimArv:
            pikimArv = len(i)
            pikimNimi = i
    return pikimNimi
    
def kolm_pikimat_sona(list):
    if len(list) > 2:
        list.sort(key=len, reverse=True)
        return list[0:3]
    
def viisnurk(k):
    for i in range(5):
        turtle.fd(k)
        turtle.rt(144)

def ring(r):
    pass

def ruut(k):
    pass
    
def suvaline():
    pass





nimed = ["Joosepcerwecw", "Joonas", "Mario", "Kiva"]
print(pikim_sona(nimed))
print(kolm_pikimat_sona(nimed))

viisnurk(100)

turtle.done()