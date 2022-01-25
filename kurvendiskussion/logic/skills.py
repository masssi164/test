import concurrent.futures
from random import randint, random
import threading
from stringparser import termToFloatValues

class NullstellenThread(threading.Thread):
    def __init__(self, target,args,group=None) -> None:
        super().__init__(target=target,args=args,group=group)
        self.result =None
        self.target =target
        self.args =args

    def run(self) -> None:
        result =self.target(*self.args)
        ##print(self.result)
    
    


def abl(glieder:list) -> list:
    new_members =[]
    for glied in glieder:
        member =[]
        koeff =glied[1]*glied[0]
        expo =glied[1]-1.0
        hasX =glied[2]
        if expo ==0:
            hasX =False    
        member =[koeff,expo,hasX]
        if expo >=0:
            new_members.append(member)
    return new_members

def allAbls(glieder:list) ->list:
    returner =[]
    for_ret =glieder
    i=0
    while for_ret:
        i=i+1
        for_ret =abl(for_ret)
        returner.append(for_ret)
    return returner

def getAllNullst(glieds:list,spacer:list=[-100,150],jumper=1) ->list:
    null =False
    a =spacer[0]
    b =spacer[1]
    nullst =[]
    null =None
    #t =NullstellenThread(nullstelle,args=(spacer[0],spacer[1]))
    #t.start()
    #t.join()
    last =None    
    actual =None
    for i in range(spacer[0],spacer[1],jumper):
        last =actual
        actual =func(glieds,i)[1]
        with concurrent.futures.ThreadPoolExecutor() as executor:
            try:
                getter =executor.submit(nullstelle(i,i-jumper,glieds))
                null =getter.result()
            except Exception as e:
                e.args
                ##print(e.args)
        with concurrent.futures.ThreadPoolExecutor() as executor:
            try:
                getter =executor.submit(nullstelle(i-jumper,i,glieds))
                null =getter.result()
            except Exception as e:
                e.args
                ##print(e.args)
            
        if last ==0.0:
            null =float(i-jumper)
        if actual ==0.0:
            null =float(i)
        if isinstance(null,float):
            if null not in nullst:
                nullst.append(null)
    return [n for n in nullst]


def func(glieder:list,value):
    #print("f(",value,")")
    returner =[value,0]
    for glied in glieder:
        erg =value**glied[1]
        erg =erg*glied[0]
        #print(erg)
        returner[1] =returner[1]+erg
    returner[1] =round(returner[1],3)
    ##print(returner)
    return returner

def nullstelle(a, b,glieder=[[1,2,True],[-1,1,False]]):
    m = (a + b)/2.0
    f = [(func(glieder,n)[1]) for n in (a, b, m)]
    #print((a,b),f)
    epsilon = 0.0000000001
    if -epsilon < f[0] < epsilon:
        return a
    elif -epsilon < f[1] < epsilon:
        return b
    elif -epsilon < f[2] < epsilon:
        return m
    elif (f[0] < 0 and f[2] > 0) or (f[0] > 0 and f[2] < 0):
        return nullstelle(a, m,glieder)
    elif (f[1] < 0 and f[2] > 0) or (f[1] > 0 and f[2] < 0):
        return nullstelle(m, b,glieder)
    elif f[2] < f[1] and f[2] < f[0]:
        #minus =randint((a+b)/2,b)
        #plus =randint(a,(a+b)/2)
        return nullstelle(a+5,b-3,glieder)
    #return False

def main(term="x^3 -11x^2 +39x -45"):
    #term ="x^3 -7x^2 +7x +15"
    #term ="x^4 -5x^2 +2x -9"
    glieds =termToFloatValues(term)
    #nullstellen =getAllNullst(glieds=glieds)
    #####print("nullstellen:",nullstellen)
    return glieds 

if __name__ == '__main__':
    #main()
    term =main()
    ###print(func(term,3.0))
    ###print(getAllNullst(term))
    ###print(getAllNullst([[6.0,1.0,True],[-22.0,0.0,False]]))
    ###print(nullstelle(-15,10,[[6,1.0,True],[22.0,0.0,False]]))