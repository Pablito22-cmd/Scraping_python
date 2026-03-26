f = open("famiglia.txt","r")

n = int(f.readline())
famiglia = {}

for i in range(n):
    line = f.readline()
    gen,fig = line.split("Figli:")
    gen1 = gen.split(":")[1].strip()
    figli = fig.strip().split()
    famiglia[gen1] = figli

nipoti = [figlio for figli in famiglia.values() for figlio in figli]

print(nipoti)

f.close()