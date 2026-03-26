import re 

f = open("listaOrdini.txt", "r")

num = int(f.readline())
list = []

for i in range(0,num):
    result = re.findall(r'\[([^\]]+)\]', f.readline())
    list.append(result)

f.close()

result = [x for x in list if x[1] == "Express"]

for i in range(0,len(result)):
    print(result[i])