class Tree(object):
    def __init__(self, r, iz, der):
        self.left = iz
        self.right = der
        self.label = r
MD1 = ['1','2','3','4','5','6','7','8','9','0','!','¡'] # Mano Derecha
MD2 = ['A','a','B','C','c','D','d','E','F','f','G','g']
MI1 = ['I','J','K','L','M','N','Z','P','Q','R','S','T'] # Mano Izquierda
MI2 = ['i','j','k','l','m','n','z','p','q','r','s','t'] # Mano Izquierda2
LetrasProposicionalesA = ['1','2','3','4','5','6','7','8','9','0','!','¡','A','a','B','C','c','D','d','E','F','f','G','g','I','J','K','L','M','N','Z','P','Q','R','S','T','i','j','k','l','m','n','z','p','q','r','s','t']
REGLA_1 = []
REGLA_2 = []
PRE_RULE = []
FINAL_RULE = []
conectivos=['Y','O','-','>']

niveles = []
def ClaUnitaria(U):
	flag=False
	posicion=-1
	for a in range(len(U)):
		if(len(U[a])==0): return (True,False,posicion)
		elif(len(U[a])==1):
			flag=True
			posicion=a
	return (False,flag,posicion)

def ClaUnit(S):
	for i in S:
		if(len(i) == 1): return True
	return False

def Complemento(L):
	if(L[0] == '-'):
		return L.replace('-','')
	else:
		return '-' + L

def removeCl(S ,l):
	S.remove(l)
	if(len(l)>=1):
		if(l[0] == '-'): L = l.replace('-','')
		else: L = l[0]
		for i in S:
			if(L in i): S.remove(i)

	return S

def removeComp(S,L):
	if(len(L)>=1):
		l = L[0]
		l = Complemento(l)
		for i in S:
			if(l in i):
				i.remove(l)
	return S

def unitPropagate(S,I):
	vacia,unitaria,posicion=ClaUnitaria(S)
	while(vacia==False and ClaUnit(S)):
		for i in S:
			S=removeCl(S,i)
			S=removeComp(S,i)
			if(len(i)==0): return 'Error',I
			if(i[0] == '-'):
				I[Complemento(i[0])] = 0
			else:
				I[i[0]] = 1
	return S, I

def literalDicc(D):
	I = D.copy()
	for i in I:
		if(i[0] == '-'):
			I.pop(i)
			i = Complemento(i)
			if(I.get(i) == 0):
				I[i[0]] = 1
			else:
				I[i[0]] = 0
	return I

def DPLL(S,I):
	S,I=unitPropagate(S,I)
	if(S == 'Error'): return 'Insatisfacible' , '{}'
	if(len(S) == 0):
		return 'Satisfacible' , literalDicc(I)
	for i in S:
		if(len(i) == 0):
			return 'Insatisfacible' , '{}'
	L = S[0]
	L = Complemento(Complemento(L[0]))
	IP = I.copy()
	if(L[0] == '-'):
		IP[Complemento(L[0])] = 0
	else:
		IP[L[0]] = 1
	SLOCO = S.copy()
	SLOCO.append(L[0])

	sati,i=DPLL(SLOCO,IP)
	if(sati == 'Satisfacible'):
		return 'Satisfacible' , literalDicc(IP)
	else:
		STAMAL = S.copy()
		STAMAL.append(Complemento(L[0]))
		IPP = I.copy()
		if(L[0] == '-'):
			IPP[Complemento(L[0])] = 1
		else:
			IPP[L[0]] = 0
	return DPLL(STAMAL,IPP)

def main(formula):
        if(len(formula)>1):
                contador = 0
                for a in range(0,len(formula)):
                        if(formula[a]=='('): contador += 1
                        elif(formula[a]==')'): contador -= 1
                        niveles.append(contador)

                for b in range(0, len(niveles)):
                        if((niveles[b]==0) and (formula[b] in conectivos)):
                                if((formula[b]=='-')):
                                        if(not(formula[b+1]=='(')): continue
                                        else:
                                                niveles.clear()
                                                return b
                                else:
                                        niveles.clear()
                                        return b

                for c in range(0, len(formula)):
                        if(formula[c] in conectivos):
                                niveles.clear()
                                return c
        return 0

def polaco(formula):
    if(len(formula)<=2): return formula
    elif(not(main(formula))):
        derecha = ""
        for b in range(2, len(formula)-1):
                derecha+=formula[b]

        return formula[main(formula)] + polaco(derecha)

    else:
            izquierda = ""
            derecha = ""

            for a in range(0, main(formula)):
                izquierda+=formula[a]

            for b in range(main(formula)+1, len(formula)):
                derecha+=formula[b]

            izquierda_nueva = izquierda
            derecha_nueva = derecha

            if(izquierda[0]=='(' and izquierda[len(izquierda)-1]==')'):
                izquierda_nueva = ""
                for a in range(1, len(izquierda)-1):
                    izquierda_nueva+=izquierda[a]

            if(derecha[0]=='(' and derecha[len(derecha)-1]==')'):
                derecha_nueva = ""
                for b in range(1, len(derecha)-1):
                    derecha_nueva+=derecha[b]

            print("izquierda: " + izquierda_nueva)
            print("derecha: " + derecha_nueva)

            return formula[main(formula)] + polaco(izquierda_nueva) + polaco(derecha_nueva)

def polacoInverso(polaco, referencia):
        if(referencia == (len(polaco)-1)): return polaco[referencia]
        else:
                return polacoInverso(polaco, referencia+1) + polaco[referencia]

def Inorder(f):

    if f.right == None:
        return f.label
    elif f.label == '-':
        return f.label + Inorder(f.right)
    else:
        return "(" + Inorder(f.left) + f.label + Inorder(f.right) + ")"

def QuitarDobleNegacion(f):

    if f.right == None:
        return f
    elif f.label == '-':
        if f.right.label == '-':
            return QuitarDobleNegacion(f.right.right)
        else:
            return Tree('-', None, QuitarDobleNegacion(f.right))
    else:
        return Tree(f.label, QuitarDobleNegacion(f.left), QuitarDobleNegacion(f.right))

def FormaNormal(f):

    p = f.left.label
    if f.right.label == '-':
        q = f.right.right.label
        return '(-'+p+'O-'+q+')Y('+p+'O'+q+')'
    q = f.right.left.label
    r = f.right.right.label
    if f.right.label == 'Y':
        return '('+q+'O-'+p+')Y('+r+'O-'+p+')Y(-'+q+'O-'+r+'O'+p+')'
    elif f.right.label == 'O':
        return '(-'+q+'O'+p+')Y(-'+r+'O'+p+')Y('+q+'O'+r+'O-'+p+')'
    else:
        return '('+q+'O'+p+')Y(-'+r+'O'+p+')Y(-'+q+'O'+r+'O-'+p+')'

def Tseitin(f, letrasProposicionales):

    A = Inorder(f)
    letrasProposicionalesB = ['x'+str(i) for i in range(1,700)]
    L = []
    pila = []
    i = -1
    s = A[0]
    while len(A) > 0:
        if s in letrasProposicionales and len(pila) > 0 and pila[-1] == '-':
            i += 1
            atomo = letrasProposicionalesB[i]
            pila = pila[:-1]
            pila.append(atomo)
            L.append(Tree('=', Tree(atomo, None, None), Tree('-', None, Tree(s, None, None))))
            A = A[1:]
            if len(A) > 0:
                s = A[0]
        elif s == ')':
            w = pila[-1]
            o = pila[-2]
            v = pila[-3]
            pila = pila[:len(pila)-4]
            i += 1
            atomo = letrasProposicionalesB[i]
            L.append(Tree('=',  Tree(atomo, None, None), Tree(o, Tree(v, None, None), Tree(w, None, None))))
            s = atomo
        else:
            pila.append(s)
            A = A[1:]
            if len(A) > 0:
                s = A[0]
    B = ''
    if i < 0:
        atomo = pila[-1]
    else:
        atomo = letrasProposicionalesB[i]
    for x in L:
        y = FormaNormal(x)
        B = B + 'Y' + y
    B = atomo + B
    return B

def Clausula(C):

    L = []
    s = C[0]
    literal = ''
    while len(C) > 0:
        if s == 'O' or s == '(' or s == ')':
            if len(literal)>0: L.append(literal)
            literal = ''
            C = C[1:]
        elif s == '-':
            literal = literal+s+C[1]
            C = C[2:]
        else:
            literal += s
            C = C[1:]
        if len(C) != 0:
            s = C[0]
    if len(literal) > 0: L.append(literal)
    return L

def FormaClausal(A):

    L = []
    i = 0
    while len(A) > 0:
        if i == len(A) or A[i] == 'Y':
            L.append(Clausula(A[:i]))
            A = A[i+1:]
            i = 0
        else:
            i += 1
    return L

def String2Tree(A, LetrasProposicionales):
    
    Conectivos = ['O','Y','>']
    Pila = []
    for c in A:
        if c in LetrasProposicionales:
            Pila.append(Tree(c,None,None))
        elif c=='-':
            FormulaAux = Tree(c,None,Pila[-1])
            del Pila[-1]
            Pila.append(FormulaAux)
        elif c in Conectivos:
            FormulaAux = Tree(c,Pila[-1],Pila[-2])
            del Pila[-1]
            del Pila[-1]
            Pila.append(FormulaAux)
    return Pila[-1]

for i in range(0,12):
    #A = ["(",MD1[i], ">","(", MI1[i] , "Y" , MI1[(i+4)%12] , "Y" , MI1[(i+7)%12]]
    A = MD1[i]+ ">"+'('+ MI1[i] + "Y" +'('+ MI1[(i+4)%12] + "Y" '('+ MI1[(i+7)%12]
    for j in MD1:
        if j != MD1[i]:
            #A.append("Y")
            A+= "Y("
            #A.append("-")
            A+= "-"
            #A.append(j)
            A+= j
    for i in range(0,14):
        A+=')'
    REGLA_1.append(A)

print("---------------Rule_1----------------------------")
for S in REGLA_1:
    f = ""
    for i in S:
        f+=i
    print(f)
    f=""
print("----------------------------------------------------------------")

for i in range(0,12):
    #B = [MD1[i],">", MI2[(i+5)%12], "Y", MI2[(i+9)%12], "Y", MI2[(i+12)%12]]
    B = MD1[i]+">"+'('+MI2[(i+5)%12]+"Y"+ '('+ MI2[(i+9)%12]+"Y"+'('+MI2[(i+12)%12]
    for j in MD2:
        if j != MD2[i]:
            #B.append("Y")
            B+= "Y("

            #B.append("-")
            B+= "-"
            #B.append(j)
            B+= j
    for i in range(0,14):
        B+=')'
    REGLA_2.append(B)

print("---------------Rule_2----------------------------")
for S in REGLA_2:
    f = ""
    for i in S:
        f+=i
    print(f)
    f=""
print("----------------------------------------------------------------")
polacos=[]
for i in REGLA_1:
    polacos.append(polaco(i))
for i in REGLA_2:
    polacos.append(polaco(i))
print(polacos)
polacosinv = []
for i in polacos:
    polacosinv.append(polacoInverso(i,0))
print(polacosinv)
print(len(polacosinv))
ImpRule = ""
for i in polacosinv:
    ImpRule+=i
for i in range(0,23):
    ImpRule+='Y'
print(ImpRule)


formula = String2Tree(ImpRule, LetrasProposicionalesA)
fnc = Tseitin(formula, LetrasProposicionalesA)
print(fnc)
clausulas = FormaClausal(fnc)
print(clausulas)
I = {}
print(DPLL(clausulas,I))

inv=polacoInverso(polaco("1Y(MYA)"),0)
tre=String2Tree(inv,LetrasProposicionalesA)
clau=Tseitin(tre, LetrasProposicionalesA)
fnclau=FormaClausal(clau)
I = {}
print(DPLL(fnclau,I))
