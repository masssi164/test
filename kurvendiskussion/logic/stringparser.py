def termToFloatValues(term:str) ->list:
    glieder =term.split(" ")
    for i in range(0,len(glieder)):
        if glieder[i][0] =="x":
            glieder[i] ="1"+glieder[i]
        if "-x" ==glieder[i][0:2] or "+x" ==glieder[i][0:2]:
            #print("yes it is")
            glieder[i] =glieder[i][0]+"1"+glieder[i][1:]
    #print(glieder)
    returnGlieder =[]
    x_glieders =list(filter(lambda x: "x" in x,glieder))
    x_glieders =[n.split("^") for n in x_glieders]
    #print("xglieders",x_glieders)
    for x_glied in x_glieders:
        floatedMember =[]
        floatedMember.append(float(x_glied[0][0:-1]))
        if len(x_glied) ==2:
            floatedMember.append(float(x_glied[1]))
        else:
            floatedMember.append(1.0)
        floatedMember.append(True)
        ##print(floatedMember)
        returnGlieder.append(floatedMember)
    absGlied =list(filter(lambda x: "x" not in x,glieder))
    ##print("absglied",absGlied)
    if len(absGlied) >0:
        returnGlieder.append([float(absGlied[0]),1.0,False])

    return returnGlieder

def main():
    term ="x^3 -x^2 -21x +45"
    print(termToFloatValues(term))

if __name__ == '__main__':
    main()
    