function selectAll(source){
        inputs = document.getElementsByTagName('input');
        for(var i=0, n=inputs.length;i<n;i++) {
          if (inputs[i].type == "checkbox"){
            inputs[i].checked = source.checked;
          }
        }
}

function hide(){
  //button=document.getElementById("submit-button");
  $("#newscan").replaceWith($("#scanning"));
  scan=document.getElementById("scanning");
  scan.style.display="block";
}

function nameCheck(){
  targetName=document.getElementById("name");
  if (targetName.value==""){
    return false;
  }
  else{
    return true;
  }
}

function targetCheck(){
  target=document.getElementById("target");
  if (target.value==""){
    return false;
  }
  else{
    return true;
  }
}

function send(){
  //formobj=document.getElementById("newScanForm");
  //const FD = new FormData(formobj);
  data=$("#newScanForm").serialize()
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function(){
  if( this.readyState == 4 && this.status == 200){
  document.getElementById("status").innerHTML = this.responseText;
  gif=document.getElementById("loading").src="";
  }
  };
  xhttp.open("POST","/start",true);
  //xhttp.setRequestHeader("Content-type","application/json");
  xhttp.send(data);
}

function oneForAll(e){
  if(e){
    e.preventDefault();
  }
  if (targetCheck()==false){
    alert("Target field cannot be empty");
    return
  }
  if (nameCheck()==false){
    alert("Name field cannot be empty");
    return
  }
  send();
  hide();
}


/*const myform = document.getElementById("newScanForm");
myform.onsubmit=oneForAll;
*/

/*
var req=$.post("/start",$("#newScanForm").serialize());
  req.done((function(data){
    $("#status").empty().append(data);
  }));




function signin(e){
if (e){
e.preventDefault();
}

const username = document.getElementById("user-name").value;
const userpw = document.getElementById("user-pw").value;

var xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function(){
if( this.readyState == 4 && this.status == 200){
//if (this.responseText == "1"){window.location="http://travel.ctf";} else{
document.getElementById("result").innerHTML = this.responseText;
//}
}
};
xhttp.open("POST","login.php",true);
xhttp.setRequestHeader("Content-type","application/x-www-form-urlencoded");
xhttp.send(`user-name=${username}&user-pw=${userpw}`);
}



function emptyCheck(){
  target=document.getElementById("target");
  targetName=document.getElementById("name");
  if (target.value==""){
    alert("Target field cannot be empty");
    return false;
  }
  if (targetName.value==""){
    alert("Target field cannot be empty");
    return false;
  }
}

*/

