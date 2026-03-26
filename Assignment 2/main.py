file = open("utenti.txt","r")

azioni = []

n = int(file.readline())
for i in range(n):
    line = file.readline().strip()
    trans = line.split(" ")
    azioni.append(trans)

utentiView = list({x[0] for x in azioni if x[1] == "view"})

utentiLogOut = {x[0] for x in azioni if x[1] == "logout"}
noLogOut = list({x[0] for x in azioni if x[0] not in utentiLogOut})

print(noLogOut)

file.close()