LetrasProposicionalesA =['A','A#','B','C','C#','D','D#','E','F','F#','G','G#','A!','A#!','B!','C!','C#!','D!','D#!','E!','F!','F#!','G!','G#!','A1','A1#','B1','C1','C1#','D1','D1#','E1','F1','F1#','G1','G1#','A2','A2#','B2','C2','C2#','D2','D2#','E2','F2','F2#','G2','G2#']
LetrasProposicionalesB =[]
A = "(A>((AYB)YC))"
for i in range(1,600):
    LetrasProposicionalesB.append("x"+str(i))

L = [] # Inicializamos lista de conjunciones
Pila = [] # Inicializamos Pila
I = -1 # Inicializamos contador de variables nuevas
S = A[0] # Inicializamos Simbolo de trabajo

while len(A) > 0:
    if len(Pila)>0 and S in LetrasProposicionalesA and Pila[-1] == '-':
        I += 1
        ATOMO = LetrasProposicionalesB[I]
        Pila = Pila[:-1]
        Pila.append(ATOMO)
        #K =[ATOMO,"=","-",S]
        L.append(ATOMO+"=-"+S)
        A = A[1:]
        if len(A)>0:
            S = A[0]
    elif S == ')':
        W = Pila[-1]
        O = Pila[-2]
        V = Pila[-3]
        Pila = Pila[:len(Pila)-4]
        I += 1
        ATOMO = LetrasProposicionalesB[I]
        #z = [ATOMO,"=",V,O,W]
        L.append(ATOMO+"="+V+O+W)
        S = ATOMO
    else:
        Pila.append(S)
        A = A[1:]
        if(len(A)>0):
            S = A[0]
B = ""
if I < 0:
    ATOMO = Pila[-1]
else:
    ATOMO = LetrasProposicionalesB[I]

print(L)
