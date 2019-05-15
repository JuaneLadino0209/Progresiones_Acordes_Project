form = "UY(U=WYS)Y(W=P>S)Y(S=-T)Y(T=q>p)"
newForm = ""
subform = "";
p = ""
q = ""
flag = True
for i in form:
    if i != '(' and flag == True:
        newForm+= i
    elif i == '(':
        flag = False
    elif i != ')' and i != '=':
        q += i
    elif i == ")":
        p = q[0]
        q = q[1:]
        if q[0] == '-':
            subform += "(-"+p+"O"+q+")Y("+p+"O"+q[1]+")"
        elif q[1] == 'Y':
            r = q[2]
            q = q[0]
            subform += "("+q+"O-"+p+")Y("+r+"O-"+p+")Y(-"+q+"O-"+r+"O"+p+")"
        elif q[1] == 'O':
            r = q[2]
            q = q[0]
            subform += "(-"+q+"O"+p+")Y(-"+r+"O"+p+")Y("+q+"O"+r+"O-"+p+")"
        elif q[1] == '>':
            r = q[2]
            q = q[0]
            subform += "("+q+"O"+p+")Y(-"+r+"O"+p+")Y(-"+q+"O"+r+"O-"+p+")"
        newForm += subform
        p = ""
        q = ""
        subform = ""
        flag = True


print(newForm)
#print(p)
#print(q)
