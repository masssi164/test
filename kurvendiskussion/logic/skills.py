from stringparser import termToFloatValues

def abl(glieder:list) -> list:
    new_members =[]
    pprint(glieder)
    for glied in glieder:
        member =[]
        koeff =int(glied[0])
        expo =int(glied[1])
        hasX =glied[2]
        if expo ==1:
            if hasX ==True:
                hasX =False
            else:
                expo =expo-1
        if expo >1:
            expo =expo-1

        koeff =koeff*int(glied[1])
        member =[koeff,expo,hasX]
        if member[1] >0:
            new_members.append(member)
    return new_members

def allAblsAsStr(glieder:list):
    returner:str ="\n\n<h2>0. Ableitungen</h2><br />"
    for_ret =glieder
    i=0
    while for_ret:
        i=i+1
        for_ret =abl(for_ret)
        out ="<li>"
        out =out+gliederToString(for_ret,i)
        if out[-1] !="=":
            returner =returner+out+"</li>"
    return returner





def getAllNullst(glieds:list,spacer:tuple=(-100.0,100.0)) ->list:
    null =False
    a =spacer[0]
    b =spacer[1]
    nullst =[]
    while True:
        if null ==False:
            null =nullstelle(a,b,glieds)
            ##print("ende if",type(null))
            #nullst.append(null)
        if type(0.0) ==type(null):
            ##print("anfang else")
            null =nullstelle(null+0.000001,b,glieds)
        if round(null,3) in nullst:
            break
        nullst.append(round(null,3))
        ##print(null)
    
    #print("nullstellen:",nullst)

    return [n*-1.0 for n in nullst]
    

def putValue(glieder,x):
        erg =0
        #print("glieder:",len(glieder),glieder)
        term ="f("+str(x)+") ="
        for glied in glieder:
            #print("has x:",glied)
            ko =glied[0]
            ex =glied[1]
            hasX =glied[2]
            writer =""
            if hasX ==True:
                perg =x**ex
                #print(x,"^",ex,"=",perg)
                multiplicated =ko*perg
                #print(perg,"*",ko,"=",multiplicated)
                writer =str(multiplicated)+" +"
                erg =erg+multiplicated
            else:
                #print("has no x")
                erg =erg+ko
                writer =str(ko)+" +"
                #print("no x but writer:",writer)
            term =term+writer+""
        return (erg,term[0:-2])
    
    
def division(glieder,nullstl):
    newglieds =[]
    for glied in glieder:
        newglied =[]
        hasX =glied[2]
        ko =float(glied[0]/nullstl)
        expo =glied[1]-1.0
        if hasX ==True and expo >0:
            newglied =[ko,expo,hasX]
        if hasX ==True and expo ==0:
            newglied =[ko,1,False]
        if len(newglied) >0:
            newglieds.append(newglied)
    return newglieds

def func(glieder:list,value):
    value =value*1.0
    returner =[value,0]
    for glied in glieder:
        if glied[2] ==True:
            erg =value**glied[1]
            erg =erg*glied[0]
            returner[1] =returner[1]+erg
        else:
            returner[1] =returner[1]+glied[0]
    return returner


def nullstelle(a, b,glieder=[[1,2,True],[-1,1,False]]):
    #print (a,"-",b)
    #print(glieder)
    if a ==b:
        return "im angegebenen Intervall keine Nullstellen gefunden"
    m = (a + b)/2.0
    f = [(func(glieder,n)[1]) for n in (a, b, m)]
    #print("f",f)
    epsilon = 0.0000000001
    if -epsilon < f[0] < epsilon:
        return -a
    elif -epsilon < f[1] < epsilon:
        return -b
    elif -epsilon < f[2] < epsilon:
        return -m
    elif (f[0] < 0 and f[2] > 0) or (f[0] > 0 and f[2] < 0):
        #print("was ich nicht verstehe_1")
        return nullstelle(a, m,glieder)
    elif (f[1] < 0 and f[2] > 0) or (f[1] > 0 and f[2] < 0):
        #print("was ich nicht verstehe_2")
        return nullstelle(m, b,glieder)
    elif f[0] >0 and f[1] >0 and f[2] >0:
        #print("all grater than null")
        return nullstelle(a,b-1.0,glieder)
    elif f[0] <0 and f[1] <0 and f[2] <0:
        return nullstelle(a+1.0,b,glieder)
    #print("nothing matches but why?")

def main():
    term ="x^3 -7x^2 +7x +15"
    glieds =termToFloatValues(term)
    nullstellen =getAllNullst(glieds=glieds)
    print("nullstellen:",nullstellen)
    
if __name__ == '__main__':
    main()
#f(x) =(x-1)(x+1)(x-3)
#x^2 -1
#x^3 -3x^2 -x +3
