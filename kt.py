
import requests

url = f"https://dummyjson.com/todos"

#Kuva ülesanded ja staatus (todo, completed) 
#Loenda tehtud ülesanded 
#Leia todopäevade koguarv
#Arvuta tehtud ülesannete protsent

def todo():
    response = requests.get(url)
    data = response.json()
    list = data["todos"]
    tehtud = 0
    kokku = len(list)
    print("Ülesanded:")


    for f in list:
        if f["completed"] == True:
            print(f["todo"], "- tehtud")
            tehtud += 1
            
        else:
            print(f"{f['todo']} - tegemata")

        print("Tehtud ülesannete arv:", tehtud)
        print("Koguarv:", kokku)
        protsent = (tehtud / kokku) * 100
        print(f"Tehtud ülesannete protsent: {protsent:.2f}%")

todo()