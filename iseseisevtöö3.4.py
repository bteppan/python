

valik = "jukebox.txt"
fail = open("rebased.txt", encoding="UTF-8")

for rida in fail:
    print(nr, rida, end="")
    nr += 1

fail.close()

nr = 1

fail = open("rebased.txt", encoding="UTF-8")

otsus = int(input("Millist laulu tahad?: "))

for rida in fail:
    if otsus == nr:
        print(nr, rida, end="")
    nr += 1

fail.close()