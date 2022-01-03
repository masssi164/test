from typing import List, SupportsAbs
import sys
class Glied():
    koeffizient =None
    exponent =None
    hasX =None

    def __init__(self,koeffizient=1,exponent=1,hasX=False) -> None:
        self.koeffizient =koeffizient
        self.exponent =exponent
        self.hasX =hasX
        print(self.koeffizient,self.exponent,self.hasX)


def makeToDic(term:str):
    print("makeToDic")
    returner =[]
    # splitting for spaces 
    spacer =term.split(" ")
    # drop first member to get just the right site of the term
    fx =spacer.pop(0)
    print("right site of the term:",spacer)
    # removing =
    spacer[0] =spacer[0][1:]
    for i in range(0,len(spacer)):
        spacer[i] =spacer[i].split("^")    
        laenge=len(spacer[i])
        for j in range(0,laenge):
            spacer[i][j] =spacer[i][j].split("x")
        # alle teilabschnitte gleichlang machen [[len(3)]]
        print(spacer)
        for i in range(0,len(spacer)):
            print("spacer laengean stelle ",i,"=",len(spacer[i]))
            if len(spacer[i]) <2:
                spacer[i].append([""])
                print("appended",spacer[i])
            print(spacer)
        def returnGlied(elem) -> Glied:
            exponent =elem[1][0]
            koeffizient =elem[0][0]
            hasX =False
            expomin =1
            koeffmin =1
            if len(koeffizient) >=1:
                if koeffizient[0] == "-":
                    koeffmin =-1
                if koeffizient[0] =="-" or koeffizient[0] =="+":
                    koeffizient =koeffizient[1:]
            if len(exponent) >=1:
                if exponent[0] =="-":
                    expomin =-1
                if exponent[0] =="-" or exponent[0] =="+":
                    exponent =exponent[1:]    
            if len(elem[0]) >1:
                hasX =True
            if exponent =="":
                exponent =1
            if koeffizient =="":
                koeffizient =1
            return Glied(int(koeffizient)*koeffmin,int(exponent)*expomin,hasX)

                                            
        print("länge spacer:",len(spacer))
        print(len(returner),"returner länge")        
        i=len(returner)
        while i>0:
            returner.pop()
            i=len(returner)
        for i in range(0,len(spacer)):
            print(spacer[i])
            gl =returnGlied(spacer[i])
            returner.append(gl)
    return returner
    

def main(mstring):
    gliedListe =makeToDic(mstring)
    print("gliedliste in main:","länge:",len(gliedListe),gliedListe)
    return gliedListe

if __name__ == '__main__':
    main()