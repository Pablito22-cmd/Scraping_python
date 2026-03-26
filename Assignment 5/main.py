f = open("anag.txt","r")

n = int(f.readline())
anagrafe = []

for i in range(n):
    id = f.readline().split()
    anagrafe.append({"Nome":id[0], "Età":int(id[1])})

anagrafe2 = [{**p, "Mesi":p["Età"]*12} for p in anagrafe if p["Età"] > 20]

print(anagrafe2)

f.close()