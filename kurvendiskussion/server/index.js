var express =require("express");
const { path } = require("express/lib/application");
const { json } = require("express/lib/response");
const { stdout } = require("process");
var app =express();
app.set('view engine', 'pug');
app.set('views');
app.use(express.json());
app.use(express.static("src"));
app.use(express.urlencoded({ extended: true }));

// functions

app.get("/",function(req,res)
{
    res.render("first_view");
});
app.post("/",function(req,res)
{
    console.log(req.body);
    const child_process =require("child_process");
    term =req.body["Term"];
    start =req.body["Start"];
    end =req.body["End"];
    jumper =req.body["Deepness"];
    console.log("term",term);
    var out ="";
    child_process.exec('starter.bat \"'+term+"\" "+start+" "+end+" "+jumper, function(err, stdout, stderr) {
        console.log(stdout,err,stderr);
        let jsonString =stdout.replace(/True/g,"true");
        jsonString =jsonString.replace(/False/g,"false");
        jsonString =jsonString.replace(/'/g,"\"");
        JSONObject =JSON.parse(jsonString);
        res.render("kd",{title:term,jsonStr:jsonString});
        // console.log(JSONObject);
        // console.log("Term:",JSONObject.ableitungen);
        // res.send(JSONObject.term);
    });
    
    // res.send(out);
    
});
app.listen(3000);
