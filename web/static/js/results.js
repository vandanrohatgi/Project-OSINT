function getResult(query){
    var obj2,obj,myobj,txt="";
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function(){
    if( this.readyState == 4 && this.status == 200){
    myobj=JSON.parse(this.response);
    //console.log(myobj);
    for (y in myobj){
        myobj[y]=myobj[y].replace(/\n/gi,"<br>"); 
    }
    ///myobj['Raw Data']=myobj['Raw Data'].replace(/\n/gi,"<br>");
    //console.log("New",myobj);
    //obj2=JSON.stringify(obj);
    //obj2=obj2.replaceAll(/\n/gi,"<br>");
    //obj2=obj2.replace(regex,'\<br\>');
    //console.log(obj2);
    //myobj=JSON.parse(obj2);
    txt+="<table class='table'>"
    for( x in myobj){
        txt+="<tr><td>"+x+"</td><td><pre>"+myobj[x]+"</pre></td>";
    }
    txt+="</table>";
    $('#table2').append(txt);
    $('#table2').show();
    //document.getElementById("table2").innerHTML=txt;
    }
    };
    xhttp.open("GET",query);
    //xhttp.setRequestHeader("Content-type","application/json");
    xhttp.send();
    $('#table').replaceWith($('#table2'));
}