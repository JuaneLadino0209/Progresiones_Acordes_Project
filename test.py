letrasProposicionales = ["A","a","B","C","c","D","d","E","F","f","G","g"]
inter = ["-A","-B","C","-D","E","-F","G"]
tru = []
for i in inter:
    if(i[0] in letrasProposicionales):
        tru.append(i);

print(tru)
