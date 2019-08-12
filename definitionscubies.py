import random

#On calcule la permutation inverse
def perminv(liste):
    n=len(liste)
    t=[[0,0] for k in range(n)]
    for k in range(n):
        t[liste[k][0]-1][0]=k+1
        t[liste[k][0]-1][1]=(3-liste[k][1])%3
    return t

#calcule B°A où B et A sont des permutations
def permprod(A,B):
    t=[[0,0] for k in range(len(A))]
    for k in range(len(A)):
        t[k][0]=B[A[k][0]-1][0]
        t[k][1]=(B[A[k][0]-1][1]+A[k][1])%3
    return t

"""     ---------
        || 9|10||
        ||12|11||
orange  ---------rouge   bleu
|| 5| 6||| 1| 2|||13|14|||17|18||     
|| 8| 7||| 4| 3|||16|15|||20|19||
        ---------
        ||21|22||jaune
        ||24|23||
        ---------"""
        
"""
UFR=[11,2,13] de référence 11
UFL=[12,1,6] de référence 12
DFL=[21,4,7] de référence 21
DFR=[22,3,16] de référence 22
UBR=[10,17,14] de référence 10
UBL=[9,18,5] de référence 9
DBL=[24,19,8] de référence 24
DBR=[23,20,15] de référence 23"""

#Représentation permutations:
"""
UFR=[1,0]
UFL=[2,0]
DFL=[3,0]
DFR=[4,0]
UBR=[5,0]
UBL=[6,0]
DBR=[7,0]
DBL=[8,0], c'est le fixe
"""
Cube2=[[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0]]
F=[[4,2],[1,1],[2,2],[3,1],[5,0],[6,0],[7,0]]
R=[[5,1],[2,0],[3,0],[1,2],[7,2],[6,0],[4,1]]
U=[[2,0],[6,0],[3,0],[4,0],[1,0],[5,0],[7,0]]
Rinv=perminv(R)
Uinv=perminv(U)
Finv=perminv(F)
F2=permprod(F,F)
R2=permprod(R,R)
U2=permprod(U,U)

#transposition de 1 et 5 : RU2RinvURU2RinvFRinvFinvR
def transposition(cubelol,liste):
    perm=["R","U2","Rinv","Uinv","R","U2","Rinv","F","Rinv","Finv","R"]
    perm1=[R,U2,Rinv,Uinv,R,U2,Rinv,F,Rinv,Finv,R]
    for i in range(len(perm)):
        cubelol=permprod(cubelol,perm1[i])
        liste.append(perm[i])
    return (cubelol,liste)


def placerEnBas(cubeMelange,solving):
    cubeCopy=cubeMelange.copy()
    if cubeCopy[2][0]==1:
        cubeCopy=permprod(cubeCopy,F2)
        solving+=["F2"]
    elif cubeCopy[2][0]==2:
        cubeCopy=permprod(cubeCopy,F)
        cubeCopy=permprod(cubeCopy,U)
        cubeCopy=permprod(cubeCopy,Finv)
        solving+=["F","U","Finv"]
    elif cubeCopy[2][0]==5:
        cubeCopy=permprod(cubeCopy,R2)
        cubeCopy=permprod(cubeCopy,F)
        solving+=["R2","F"]
    elif cubeCopy[2][0]==6: 
        cubeCopy=permprod(cubeCopy,F)
        cubeCopy=permprod(cubeCopy,Uinv)
        cubeCopy=permprod(cubeCopy,Finv)
        solving+=["F","Uinv","Finv"]
    elif cubeCopy[2][0]==4:
        cubeCopy=permprod(cubeCopy,F)
        solving+=["F"]
    elif cubeCopy[2][0]==7:
        cubeCopy=permprod(cubeCopy,R)
        cubeCopy=permprod(cubeCopy,F)
        solving+=["R","F"]
    if cubeCopy[3][0]==1: 
        cubeCopy=permprod(cubeCopy,Rinv)
        solving+=["Rinv"]
    elif cubeCopy[3][0]==2:
        cubeCopy=permprod(cubeCopy,Uinv)
        cubeCopy=permprod(cubeCopy,Rinv)
        solving+=["Uinv","Rinv"]
    elif cubeCopy[3][0]==6:
        cubeCopy=permprod(cubeCopy,U2)
        cubeCopy=permprod(cubeCopy,Rinv)
        solving+=["U2","Rinv"]
    elif cubeCopy[3][0]==5:
        cubeCopy=permprod(cubeCopy,R2)
        solving+=["R2"]
    elif cubeCopy[3][0]==7:
        cubeCopy=permprod(cubeCopy,R)
        solving+=["R"]
    if cubeCopy[6][0]==1:
        cubeCopy=permprod(cubeCopy,F)
        cubeCopy=permprod(cubeCopy,Rinv)
        cubeCopy=permprod(cubeCopy,Finv)
        solving+=["F","Rinv","Finv"]
    elif cubeCopy[6][0]==2:
        cubeCopy=permprod(cubeCopy,Rinv)
        cubeCopy=permprod(cubeCopy,U2)
        cubeCopy=permprod(cubeCopy,R)
        solving+=["Rinv","U2","R"]
    elif cubeCopy[6][0]==5:
        cubeCopy=permprod(cubeCopy,Rinv)
        cubeCopy=permprod(cubeCopy,Uinv)
        cubeCopy=permprod(cubeCopy,R)
        solving+=["Rinv","Uinv","R"]
    elif cubeCopy[6][0]==6:
        cubeCopy=permprod(cubeCopy,Rinv)
        cubeCopy=permprod(cubeCopy,U)
        cubeCopy=permprod(cubeCopy,R)
        solving+=["Rinv","U","R"]
    return (cubeCopy,solving)



def orientationEnBas(cube,solving):
    orientations=[cube[k][1] for k in range(len(cube))]
    if cube[2][1]==2:
        perm=["Finv","U","F2","Uinv","F2","Uinv","Finv","U","F","U","Finv","Uinv","F2","Uinv","F2","U"]
        perm1=[Finv,U,F2,Uinv,F2,Uinv,Finv,U,F,U,Finv,Uinv,F2,Uinv,F2,U]
        for i in range(len(perm)):
            cube=permprod(cube,perm1[i])
            solving.append(perm[i])
    elif cube[2][1]==1:
        perm=["F","U","F2","Uinv","F2","Uinv","Finv","U","F","U","Finv","Uinv","F2","Uinv","F2","U","F2"]
        perm1=[F,U,F2,Uinv,F2,Uinv,Finv,U,F,U,Finv,Uinv,F2,Uinv,F2,U,F2]
        for i in range(len(perm)):
            cube=permprod(cube,perm1[i])
            solving.append(perm[i])
    if cube[3][1]==1:
        perm=["R","U","R2","Uinv","R2","Uinv","Rinv","U","R","U","Rinv","Uinv","R2","Uinv","R2","U","R2"]
        perm1=[R,U,R2,Uinv,R2,Uinv,Rinv,U,R,U,Rinv,Uinv,R2,Uinv,R2,U,R2]
        for i in range(len(perm)):
            cube=permprod(cube,perm1[i])
            solving.append(perm[i])
    elif cube[3][1]==2:
        perm=["Rinv","U","R2","Uinv","R2","Uinv","Rinv","U","R","U","Rinv","Uinv","R2","Uinv","R2","U"]
        perm1=[Rinv,U,R2,Uinv,R2,Uinv,Rinv,U,R,U,Rinv,Uinv,R2,Uinv,R2,U]
        for i in range(len(perm)):
            cube=permprod(cube,perm1[i])
            solving.append(perm[i])
    if cube[6][1]==2:
        perm=["U","R2","Uinv","R2","Uinv","Rinv","U","R","U","Rinv","Uinv","R2","Uinv","R2","U","Rinv"]
        perm1=[U,R2,Uinv,R2,Uinv,Rinv,U,R,U,Rinv,Uinv,R2,Uinv,R2,U,Rinv]
        for i in range(len(perm)):
            cube=permprod(cube,perm1[i])
            solving.append(perm[i])
    elif cube[6][1]==1:
        perm=["R2","U","R2","Uinv","R2","Uinv","Rinv","U","R","U","Rinv","Uinv","R2","Uinv","R2","U","R"]
        perm1=[R2,U,R2,Uinv,R2,Uinv,Rinv,U,R,U,Rinv,Uinv,R2,Uinv,R2,U,R]
        for i in range(len(perm)):
            cube=permprod(cube,perm1[i])
            solving.append(perm[i])
    return (cube,solving)



def OLL(cube,solving):
    liste=[cube[0][1],cube[1][1],cube[4][1],cube[5][1]]
    s=0
    for k in range(len(liste)):
        if liste[k]==0:
            s+=1
    if s==1:
        listebis=[]
        for k in [1,2,5,6]:
            for j in range(len(cube)):
                if cube[j][0]==k:
                    listebis.append(j)
        while cube[listebis[0]][1]!=0:
            listebis=[]
            for k in [1,2,5,6]:
                for j in range(len(cube)):
                    if cube[j][0]==k:
                        listebis.append(j)
            cube=permprod(cube,U)
            solving+=["U"]
        perm=["R","U","Rinv","U","R","U2","Rinv"]
        perm1=[R,U,Rinv,U,R,U2,Rinv]
        for i in range(len(perm)):
            cube=permprod(cube,perm1[i])
            solving.append(perm[i])
    elif s==0:
        listebis=[]
        for k in [1,2,5,6]:
            for j in range(len(cube)):
                if cube[j][0]==k:
                    listebis.append(j)
        while cube[listebis[0]][1]!=2 or cube[listebis[1]][1]!=1:
            cube=permprod(cube,U)
            solving+=["U"]
            listebis=[]
            for k in [1,2,5,6]:
                for j in range(len(cube)):
                    if cube[j][0]==k:
                        listebis.append(j)
        if cube[listebis[2]][1]==1:
            perm=["R2","U2","Rinv","U2","R2"]
            perm1=[R2,U2,Rinv,U2,R2]
            for i in range(len(perm)):
                cube=permprod(cube,perm1[i])
                solving.append(perm[i])
        else:
            perm=["U","F","R","U","Rinv","Uinv","R","U","Rinv","Uinv","Finv"]
            perm1=[U,F,R,U,Rinv,Uinv,R,U,Rinv,Uinv,Finv]
            for i in range(len(perm)):
                cube=permprod(cube,perm1[i])
                solving.append(perm[i])
    elif s==2:
        listebis=[]
        for k in [1,2,5,6]:
            for j in range(len(cube)):
                if cube[j][0]==k:
                    listebis.append(j)
        if (cube[listebis[0]][1]==cube[listebis[3]][1] and cube[listebis[0]][1]==0) or (cube[listebis[1]][1]==cube[listebis[2]][1] and cube[listebis[1]][1]==0):
            while cube[listebis[1]][1]!=1:
                cube=permprod(cube,U)
                solving+=["U"]
                listebis=[]
                for k in [1,2,5,6]:
                    for j in range(len(cube)):
                        if cube[j][0]==k:
                            listebis.append(j)
                
            perm=["Rinv","F","R","U","F","Uinv","Finv"]
            perm1=[Rinv,F,R,U,F,Uinv,Finv]
            for i in range(len(perm)):
                cube=permprod(cube,perm1[i])
                solving.append(perm[i])
        else:
            while cube[listebis[0]][1]!=cube[listebis[2]][1]:
                cube=permprod(cube,U)
                solving+=["U"]
                listebis=[]
                for k in [1,2,5,6]:
                    for j in range(len(cube)):
                        if cube[j][0]==k:
                            listebis.append(j)
            if cube[listebis[3]][1]==1:
                perm=["F","R","Finv","Uinv","Rinv","Uinv","R"]
                perm1=[F,R,Finv,Uinv,Rinv,Uinv,R]
                for i in range(len(perm)):
                    cube=permprod(cube,perm1[i])
                    solving.append(perm[i])
            else:
                perm=["F","R","U","Rinv","Uinv","Finv"]
                perm1=[F,R,U,Rinv,Uinv,Finv]
                for i in range(len(perm)):
                    cube=permprod(cube,perm1[i])
                    solving.append(perm[i])
    elif s==3:
        return "ERROR Orientation: 'Non-official move was made. Please twist a corner then retry'"
    return (cube,solving)


def PLL(cube,solving):
    while cube[0][0]!=1:
        cube=permprod(cube,U)
        solving+=["U"]
    if cube[1][0]==6:
        cube=permprod(cube,U2)
        solving+=["U2"]
        (cube,solving)=transposition(cube,solving)
        cube=permprod(cube,U2)
        solving+=["U2"]
    elif cube[1][0]==5:
        perm=["Rinv","U","Rinv","F2","R","Finv","U","Rinv","F2","R","Finv","R","Uinv"]
        perm1=[Rinv,U,Rinv,F2,R,Finv,U,Rinv,F2,R,Finv,R,Uinv]
        for i in range(len(perm)):
            cube=permprod(cube,perm1[i])
            solving.append(perm[i])
    if cube[5][0]==5:
        cube=permprod(cube,U)
        solving+=["U"]
        (cube,solving)=transposition(cube,solving)
        cube=permprod(cube,Uinv)
        solving+=["Uinv"]
    return (cube,solving)


def reduction(listeperm):
    i=0
    n=len(listeperm)
    liste2=[]
    liste=[]
    for k in range(len(listeperm)):
        if listeperm[k]=="R":
            liste.append([0,1])
        elif listeperm[k]=="Rinv":
            liste.append([0,3])
        elif listeperm[k]=="R2":
            liste.append([0,2])
        elif listeperm[k]=="F":
            liste.append([1,1])
        elif listeperm[k]=="Finv":
            liste.append([1,3])
        elif listeperm[k]=="F2":
            liste.append([1,2])
        elif listeperm[k]=="U":
            liste.append([2,1])
        elif listeperm[k]=="Uinv":
            liste.append([2,3])
        elif listeperm[k]=="U2":
            liste.append([2,2])
    i=0
    while i<len(liste)-1:
        k=i
        s=0
        w=liste[i][0]
        while k<len(liste) and liste[k][0]==w:
            k+=1
        for j in range(i,k):
            s+=liste[j][1]
        s%=4
        if s!=0:           
            liste.insert(k,[w,s])
        del liste[i:k]
        if k!=i+1 and i>0:
            i-=1
        else:
            i+=1
    for k in range(len(liste)):
        if liste[k]==[0,1]:
            liste2.append("R")
        elif liste[k]==[0,3]:
            liste2.append("Rinv")
        elif liste[k]==[0,2]:
            liste2.append("R2")
        elif liste[k]==[1,1]:
            liste2.append("F")
        elif liste[k]==[1,3]:
            liste2.append("Finv")
        elif liste[k]==[1,2]:
            liste2.append("F2")
        elif liste[k]==[2,1]:
            liste2.append("U")
        elif liste[k]==[2,3]:
            liste2.append("Uinv")
        elif liste[k]==[2,2]:
            liste2.append("U2")        
    return liste2




def resolution(cube):
    solution=[]
    (cube,solution)=placerEnBas(cube,solution)
    (cube,solution)=orientationEnBas(cube,solution)
    (cube,solution)=OLL(cube,solution)
    (cube,solution)=PLL(cube,solution)
    solution=reduction(solution)
    return solution


def Scramble(cube):
    t=[]
    for k in range(25):
        i=random.randint(0,8)
        if i==0:
            cube=permprod(cube,F)
            t.append('F')
        elif i==1:
            cube=permprod(cube,R)
            t.append('R')
        elif i==2:
            cube=permprod(cube,U)
            t.append('U')
        elif i==3:
            cube=permprod(cube,F2)
            t.append('F2')
        elif i==4:
            cube=permprod(cube,R2)
            t.append('R2')
        elif i==5:
            cube=permprod(cube,U2)
            t.append('U2')
        elif i==6:
            cube=permprod(cube,Finv)
            t.append('Finv')
        elif i==7:
            cube=permprod(cube,Rinv)
            t.append('Rinv')
        elif i==8:
            cube=permprod(cube,Uinv)
            t.append('Uinv')
    return (cube,t)

def comptage(n):
    liste=[]
    m=0
    for k in range(n):
        cube=Cube2.copy()
        (cube,t)=Scramble(cube)
        w=len(resolution(cube))
        liste.append(w)
        m+=(w/n)
    return m
print(comptage(100000))
