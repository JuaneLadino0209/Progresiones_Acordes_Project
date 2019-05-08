LetrasProposicionalesA =['p','q','r']
LetrasProposicionalesB =[]
A = "((pYq)>-r)"
for i in range(1,101):
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
        L.append(ATOMO + '=-' + S)
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
        L.append(ATOMO +"="+V+O+W)
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
