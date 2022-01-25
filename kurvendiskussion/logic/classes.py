import sys
from skills import *
from koeffizientenVgl import termVgl

def alleNullstellen(term,start=-100.0,end=100.0,deepness=3):
    null =False
    newTerm =None
    nullStellen=[]
    null =nullstelle(start,end,term)
    newTerm =termVgl(term,null)
    nullStellen.append(null)    
    while null !=None:
        try:
            null =nullstelle(start,end,newTerm)
            newTerm =termVgl(newTerm,null)
            nullStellen.append(null)
            #print(nullStellen)
        except Exception as e:
            #print(e.args)
            break
    return nullStellen

class Struct():
    function:list
    nullstellen:list
    abls:list
    extrema:list
    wendepunkte:list

    def __init__(self,function:list,start:int,end:int,deepness:int) -> None:
        self.start =start
        self.end =end
        self.deepness =deepness
        self.function =function
        self.nullstellen =alleNullstellen(self.function,start,end,deepness)
        ##print("nullstellen:",self.nullstellen)
        self.abls =allAbls(function)
        self.calculateExtrema()
        self.calculateWendepunkt()

    
    def calculateWendepunkt(self):
        if len(self.abls) >=2:
            ###print("lang genug")
            abl2 =self.abls[1]
            stellen =alleNullstellen(abl2,self.start,self.end,self.deepness)
        ys =[]
        for stelle in stellen:
            ys.append(func(self.function,stelle)[1])
        ###print("ys",ys)
        self.wendepunkte =[]
        for i in range(0,len(stellen)):
            point =[stellen[i],ys[i]]
            if len(self.abls) >=3:
                highorlow =0
                xes =[n[2] for n in self.abls[2]]

                ###print("xes")
                if True in xes:
                    highorlow =func(self.abls[2],stellen[i])[1]
                else:
                    kos =[n[0] for n in self.abls[2]]
                    for ko in kos:
                        highorlow =highorlow+ko
                if highorlow >0:
                    point.append("rl")
                if highorlow <0:
                    point.append("lr")
                if highorlow ==0:
                    point.append(0)
                self.wendepunkte.append(point)



    def calculateExtrema(self):
        abl1 =self.abls[0]
        stellen =alleNullstellen(abl1,self.start,self.end,self.deepness)
        ys =[]
        for stelle in stellen:
            ys.append(func(self.function,stelle)[1])
        ###print("ys",ys)
        self.extrema =[]
        for i in range(0,len(stellen)):
            point =[stellen[i],ys[i]]
            highorlow =func(self.abls[1],stellen[i])[1]
            if highorlow >0:
                point.append("t")
            if highorlow <0:
                point.append("h")
            if highorlow ==0:
                point.append("s")
            self.extrema.append(point)


if __name__ == '__main__':
    term =sys.argv[1].split("=")[1]
    jumper =int(sys.argv[4])
    start =int(sys.argv[2])
    end =int(sys.argv[3])
    struct =Struct(main(term=term),start,end,jumper)
    print("{\"term\":")
    print(struct.function)
    print(",\"nullstellen\":")
    print(struct.nullstellen)
    print(",\"ableitungen\":")
    print(struct.abls)
    print(",\"extrema\":")    
    print(struct.extrema)
    print(",\"wendepunkte\":")
    print(struct.wendepunkte)
    print("}")
    ###print("new")