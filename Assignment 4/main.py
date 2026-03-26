import re

f = open("logFile.txt","r")
list = []

for i in range(0,10):
    result = re.findall(r'\[([^\]]+)\]',f.readline())
    list.append(result)
    print(i+1, ") ", list[i])

view = set()
view = {x[0] for x in list if x[1] == "View"}
viewList = [x for x in view]

print("Id con View: ", viewList)

siLogOut = {x[0] for x in list if x[1] == "LogOut"}
noLogOut = {x[0] for x in list if not (x[0] in siLogOut)}

print("Id senza LogOut: ", noLogOut)

alfa = {}

for id in list:
    if id[0] in alfa:
        alfa[id[0]] += 1
    else:
        alfa[id[0]] = 1

sortDict = dict(sorted(alfa.items()))
print(*(x for x in sortDict if alfa[x] > 1))

f.close()