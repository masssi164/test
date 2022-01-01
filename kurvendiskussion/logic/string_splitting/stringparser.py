from typing import List
import sys
class Glied():
    koeffizient =None
    exponent =None
    hasX =None

    def __init__(self,koeffizient,exponent=1,hasX=False) -> None:
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
        for i in range(0,len(spacer)):
            if len(spacer[i]) <2:
                spacer[i].append("")
        print(spacer)


def main():
    parser =makeToDic(sys.argv[1])

if __name__ == '__main__':
    main()