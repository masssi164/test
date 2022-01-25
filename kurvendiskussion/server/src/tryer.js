function getGlobalBehavior(term) 
{
    toMinus ="\\lim_{x \\to -\\infty f(x) =";
    toPlus ="\\lim_{x \\to \\infty f(x) =";
    g =7
    if (term[0][0] >0)
    {
        g =true;
        toMinus =toMinus+"-\\infty }";

    } else {
        g =false;
        toMinus =toMinus+"\\infty }";
    }
    str_1 ="\\infty}";
    str_2 ="-\\infty}";
    evaluator =term[0][1]%2;
    console.log("evaluator",evaluator);
    if (evaluator >0 && g ==true)
    {
        toPlus =toPlus+str_1;
    } 
    if (evaluator >0 && g ==false)
    {
        toPlus =toPlus+str_2;
    }
    if (evaluator ==0 && g ==true)
    {
        toPlus =toPlus+str_2;
    }
    if (evaluator ==0 && g ==false)
    {
        toPlus =toPlus+str_1;
    }
    h1 =document.createElement("h1");
    h1.innerHTML ="Globales Verhalten";
    ul =document.createElement("ul");
    li_1 =document.createElement("li");
    li_2 =document.createElement("li");
    li_1.innerHTML =toMinus;
    li_2.innerHTML =toPlus;
    ul.appendChild(li_1);
    ul.appendChild(li_2);
    return [h1,ul];
}

function getWendepunkte(wendepunkte)
{
    h1 =document.createElement("h1");
    h1.innerHTML ="Wendepunkte";
    wp =document.createElement("ol");
    for(let i=0; i<wendepunkte.length; i++)
    {
        li =document.createElement("li");
        li.innerHTML ="("+wendepunkte[i][0].toString()+"|"+wendepunkte[i][1].toString()+")";
        if (wendepunkte[i][2] == "rl") {
                li.innerHTML =li.innerHTML+" [Rechts-Links-Wendepunkt";
        }
        if (wendepunkte[i][2] == "lr") {
            li.innerHTML =li.innerHTML+" [Links-Rechts-Wendepunkt]";
        }
    
        wp.appendChild(li);
    }
    return [h1,wp]
}

function getExtrema(extrema)
{
    h1 =document.createElement("h1");
    h1.innerHTML ="Extrema";
    extrem =document.createElement("ol");
    for(let i=0; i<extrema.length; i++)
    {
        li =document.createElement("li");
        li.innerHTML ="("+extrema[i][0].toString()+" | "+extrema[i][1].toString()+")";
        if (extrema[i][2] =="h")
        {
            li.innerHTML =li.innerHTML+" [Hochpunkt]";
        }
        if (extrema[i][2] =="t")
        {
            li.innerHTML =li.innerHTML+" [Tiefpunkt]";
        }
        
        extrem.appendChild(li);
    }
    return [h1,extrem]
}


function parseGliederToString(glieder) 
{
    console.log(glieder);
    let returnStr ="";
    for(i=0; i<glieder.length; i++) 
    {
        ko =glieder[i][0];
        ex =glieder[i][1];
        hasX =glieder[i][2];
        console.log(ko,ex,hasX);
        let forString ="";
        if(ex >0 && hasX ==true)
        {
            forString =forString+ko.toString();
        }
        if(ko >0 && hasX ==false)
        {
            forString =forString+ko.toString();
        }
        if (ko ==-1.0 && hasX ==false && i >0)
        {
            forString =forString+"-";
        }
        else if(ko ==1.0 && hasX ==false && i >0)
        {
            forString =forString+"+";
        }
        else if(ko !=-1.0 && ko !=1.0 && i>0) 
        {
            if (ko >0) {
                forString ="+"+ko.toString();    
            } else {
                forString =ko.toString();
            }
        }
        if (hasX ==true) 
        {
            forString =forString+"x";
            if(ex >1) {
                forString =forString+"^"+ex.toString();
            }
        }
        // console.log("glied:",forString);
        if (i <glieder.length-1) 
        {
            forString =forString+" ";
        }
        returnStr =returnStr+forString;
    }
    // console.log("term:", returnStr);
    return returnStr;
}


function getTerm(glieder) {
    let h1 =document.createElement("h1");
    let term ="f(x) =";
    term =term+parseGliederToString(glieder);
    h1.innerHTML =term;
    return h1;
}

function getNullst(nullstellen) 
{
    let h1 =document.createElement("h1");
    h1.innerHTML ="1. Nullstellen";
    let liste =document.createElement("ol");
    for(i=0; i<nullstellen.length; i++)
    {
        console.log("nullstelle:",nullstellen[i]);
        let eintrag =document.createElement("li");
        eintrag.innerHTML =nullstellen[i].toString();
        liste.appendChild(eintrag);
    }
    return [h1,liste];
}

function getAbleitungen(liste)
{
    let h1 =document.createElement("h1");
    h1.innerHTML ="0. Ableitungen";
    let gliederung =document.createElement("ol");

    function getApostrophies(times) {
        returner =" ";
        for(i=0; i<times+1; i++)
        {
            returner =returner+"\'";
        }
        return returner;
    }    
    liste.pop();
    console.log(parseGliederToString(liste[0]));
    for(let i=0; i<liste.length; i++) {
        console.log(liste[i].length,"länge",i,"zähler");
        let li =document.createElement("li");
        let zk= "f";
        zk =zk+getApostrophies(i)+"(x) ="+parseGliederToString(liste[i]);
        console.log(i,zk);
        li.innerHTML =zk;
        gliederung.appendChild(li);
        console.log(liste[i].length,"länge",i,"zähler");
    }
    return [h1,gliederung];
}

function appender(parent,children)
{
    for(let i=0; i<children.length; i++)
    {
        parent.appendChild(children[i]);
    }
}

window.addEventListener('DOMContentLoaded', (event) => {
    var term =document.querySelector("#term");
    var globales_verhalten =document.querySelector("#globales_verhalten");
    var wendepunkte =document.querySelector("#wendepunkte");
    var ableitungen =document.querySelector("#ableitungen");
    var extrema =document.querySelector("#extrema");
    var nullstellen =document.querySelector("#nullstellen");
    var jsonString =document.querySelector("#jsonString").value;
    var data=JSON.parse(jsonString);  
    console.log(data);
    term.appendChild(getTerm(data.term));    
    appender(nullstellen,getNullst(data.nullstellen));    
    appender(ableitungen,getAbleitungen(data.ableitungen));
    console.log(data.extrema);
    extrems =getExtrema(data.extrema);
    for(let i=0; i<extrems.length; i++)
    {
        extrema.appendChild(extrems[i])
    }
    wps =getWendepunkte(data.wendepunkte);
    for(let i=0; i<wps.length; i++)
    {
        wendepunkte.appendChild(wps[i]);
    }
    console.log(data.wendepunkte[0][2])
    g_b =getGlobalBehavior(data.term);
    for(let i =0; i<g_b.length; i++) {
        globales_verhalten.appendChild(g_b[i]);
    }
});
