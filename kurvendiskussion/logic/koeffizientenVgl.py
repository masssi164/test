import pprint
from skills import *

def gleichung(erg,schablone):
    buchstaberl =[]
    glgs =[]
    for i in erg:
        expo =i[1]
        links =list(filter(lambda x: x[2] ==expo,schablone))
        glgs.append([i[0],links])
        #p##print.p##print(glgs)
    def watchInLetters(letters,glgi):
        for letter in letters:
            i=0
            while i <len(glgi):
                if letter[1] in glgi[i]:
                    return [letter[0],letter[1],glgi[i][0],letter[2]]
                i=i+1
            ###print()
        return False
    for glg in glgs:
        if len(glg[1]) ==1:
            sol =glg[0]
            ##print("sol",sol)
            links =glg[1][0]
            ##print("links",links)
            appender =None
            er =sol/links[0]
            appender =[er,links[1],links[2]-1]
            ##print(appender)
            buchstaberl.append(appender)
        if len(glg[1]) ==2:
            ##print("glied:",glg[1])
            glied=watchInLetters(buchstaberl,glg[1])
            ###print(glied)
            if glied != False:
                otherLetter =glg[0]-glied[0]*glied[2]
                ##print("otherletter",otherLetter)
                for i in glg[1]:
                    ##print(i)
                    if glied[1] not in i:
                        value =otherLetter/i[0]
                        buchstaberl.append([value,i[1],i[2]-1])
                        ##print(buchstaberl)
    returner =[]
    buchstaberl.pop()
    #print(buchstaberl)
    for newGlied in buchstaberl:
        appender =[newGlied[0],newGlied[2]]
        if newGlied[2] >0:
            appender.append(True)
        else:
            appender.append(False)
        #print(appender)
        returner.append(appender)
    return returner




def termSchablone(highestExpo,nullst) ->list:
    highestExpo =highestExpo+1
    schablone=[]
    letters ="abcdefghijklmnopqrstuvwxyz"
    charindex =0
    while highestExpo >-1:    
        glied_1 =None
        glied_2 =None
        ko_1 =(1.0,letters[charindex])
        ko_2 =(-nullst,letters[charindex])
        ###print(ko_2)
        expo_1 =highestExpo
        expo_2 =highestExpo-1
        ###print(expo_2)
        if expo_1 >1:
            glied_1=[*ko_1,expo_1,True]
            glied_2=[*ko_2,expo_2,True]
        elif expo_1 ==1:
            glied_1=[*ko_1,expo_1,True]
            glied_2=[*ko_2,expo_2,False]
        elif expo_1 == 0:
            glied_1=[*ko_1,expo_1,False]
        highestExpo=highestExpo-1
        charindex=charindex+1
        
        for eintrag in [glied_1,glied_2]:
            schablone.append(eintrag)
    return list(filter(lambda x: x!=None,schablone))

def termVgl(original,nullst):
    nullst=round(nullst,3)
    letters="abcdefghijklmnopqrstuvwxyz"
    copy =termSchablone(original[0][1]-1,nullst)
    erg =[]
    for wertePaar in original:
        erg.append([wertePaar[0],wertePaar[1]])
    ##print("erg",erg)
    ##print("schablone",copy)
    return gleichung(erg,copy)


if __name__ == '__main__':
    term =main("x^3 -11x^2 +39x -45")
    ###print(term)
    nullst =nullstelle(-100,100,term)
    #schablone =termSchablone(term[0][1]-1,nullst)
    ###print(schablone)
    newTerm =termVgl(term,nullst)
    print(newTerm)
    nullst_1 =nullstelle(-100.0,100.0,newTerm)
    print(nullst_1)
    term_lst =termVgl(newTerm,nullst_1)
    print(nullstelle(-100.0,100.0,term_lst))
