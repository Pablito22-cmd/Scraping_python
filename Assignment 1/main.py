file = open("ordini.txt","r")

orders = []

n = int(file.readline())
for i in range(n):
    line = file.readline().strip()
    tokens = line.split(" ")
    orders.append(tokens)

onlyExp = [x for x in orders if x[1] == "EXPRESS" if len(x[2:]) >= 2]

articles = {x for order in orders for x in order[2:]}

file.close()