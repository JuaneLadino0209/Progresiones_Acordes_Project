MD1 = ['A','A#','B','C','C#','D','D#','E','F','F#','G','G#'] # Mano Derecha
MD2 = ['A!','A#!','B!','C!','C#!','D!','D#!','E!','F!','F#!','G!','G#!']
MI1 = ['A1','A1#','B1','C1','C1#','D1','D1#','E1','F1','F1#','G1','G1#'] # Mano Izquierda
MI2 = ['A2','A2#','B2','C2','C2#','D2','D2#','E2','F2','F2#','G2','G2#'] # Mano Izquierda2
LetrasProposicionalesA = ['A','A#','B','C','C#','D','D#','E','F','F#','G','G#','A!','A#!','B!','C!','C#!','D!','D#!','E!','F!','F#!','G!','G#!','A1','A1#','B1','C1','C1#','D1','D1#','E1','F1','F1#','G1','G1#','A2','A2#','B2','C2','C2#','D2','D2#','E2','F2','F2#','G2','G2#']

REGLA_1 = []
REGLA_2 = []
FINAL_RULE = []

for i in range(0,12):
    A = ["(",MD1[i], ">","(", MI1[i] , "Y" , MI1[(i+4)%12] , "Y" , MI1[(i+7)%12]]
    #A = "(" + MD1[i]+ ">"+"(" + MI1[i] + "Y" + MI1[(i+4)%12] + "Y" + MI1[(i+7)%12]
    for j in MD1:
        if j != MD1[i]:
            A.append("Y")
            #A+= "Y"
            A.append("-")
            #A+= "-"
            A.append(j)
            #A+= j
    A.append(")")
    A.append(")")
    cont = 0
    for i in range(4,len(A)+6):
        if A[i] == "Y":
            if A[i+1] == "-":
                A.insert(i+3,")")
                cont += 1
            else:
                A.insert(i+2,")")
                cont += 1
    for i in range(1,cont+1):
        A.insert(4,"(")

            #A.insert(4,"(")
    REGLA_1.append(A)


# for i in range(0,12):
#     #B = [MD1[i],">", MI2[(i+5)%12], "Y", MI2[(i+9)%12], "Y", MI2[(i+12)%12]]
#     B = ["(",MD1[i],">","(", MI2[(i+5)%12], "Y", MI2[(i+9)%12], "Y", MI2[(i+12)%12]]
#     for j in MD2:
#         if j != MD2[i]:
#             B.append("Y")
#             #B+= "Y"
#             B.append("-")
#             #B+= "-"
#             B.append(j)
#             #B+= j
#     B.append(")")
#     B.append(")")
#     REGLA_2.append(B)


for S in REGLA_1:
    f = "";
    for i in S:
        f+=i
    print(f)
    f = ""
    # print(S)
    # print(len(S))
    # print("\n")
# for S in REGLA_2:
#     # f = "";
#     # for i in S:
#     #     f+=i
#     # print(f)
#     # f = ""
#     print(S)
#     print(len(S))
#     print("\n")
