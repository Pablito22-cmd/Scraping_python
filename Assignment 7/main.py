f = open("stringa.txt","r")

def vow(par):
    vocali = "aeèiou"
    res = 0
    for i in range(len(par)):
        if par[i] in vocali:
            res += 1
    return res


stringa = f.read()
f.close()

parole = stringa.strip().split()
diz = {x:vow(x) for x in parole}

f = open("output.txt","w")

for key in diz:
    stringa = str(key) + ": " + str(diz[key]) + "\n"
    f.write(stringa)

f.close()