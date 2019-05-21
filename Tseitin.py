from random import choice

class Tree(object):
    def __init__(self, r, iz, der):
        self.left = iz
        self.right = der
        self.label = r

def Inorder(f):
    # Imprime una formula como cadena dada una formula como arbol
    # Input: tree, que es una formula de logica proposicional
    # Output: string de la formula

    if f.right == None:
        return f.label
    elif f.label == '-':
        return f.label + Inorder(f.right)
    else:
        return "(" + Inorder(f.left) + f.label + Inorder(f.right) + ")"

def QuitarDobleNegacion(f):
    # Elimina las dobles negaciones en una formula como arbol
    # Input: tree, que es una formula de logica proposicional
    # Output: tree sin dobles negaciones
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
    # Devuelve las equivalencias en forma normal conjuntiva de las expresiones en las transformaciones de Tseitin
    # Input: tree, que es una formula de logica proposicional
    # Output: Forma normal conjuntiva como cadena de caracteres
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
    # Halla la forma normal conjuntiva de una formula usando la transformacion de Tseitin
    # Input: tree f, lista de strings letrasProposicionales
    # Output: Forma normal conjuntiva como cadena de caracteres
    # f = QuitarDobleNegacion(f)
    # A = Inorder(f)
    letrasProposicionalesB = ['x'+str(i) for i in range(1,101)]
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
            #L.append(Tree('=', Tree(atomo, None, None), Tree('-', None, Tree(s, None, None))))

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
            L.append(atomo)
            L.append('=')
            L.append(v)
            L.append()
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
    # Transforma una clausula en forma de string a una lista de literales
    # Input: String C
    # Output: Clausula como lista de caracteres
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
    # Obtiene la forma clausal de una formula en FNC
    # Input: A, que es una formula de logica proposicional en FNC en forma de cadena de caracteres
    # Output: lista de clausulas
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

#################### Prueba del programa ########################
formula = Tree('-', None, Tree('Y', Tree('p', None, None), Tree('q', None, None)))
fnc = Tseitin(formula, ['p','q'])
print(fnc)
clausulas = FormaClausal(fnc)
print(clausulas)
