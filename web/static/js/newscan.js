function selectAll(source){
        inputs = document.getElementsByTagName('input');
        for(var i=0, n=inputs.length;i<n;i++) {
          if (inputs[i].type == "checkbox"){
            inputs[i].checked = source.checked;
          }
        }
}

function emptyCheck(){
  targetName=document.getElementById("name");
  target=document.getElementById("target");

  if (targetName.value==""){
    alert("Name field cannot be empty");
    return false;
  }
  if (target.value==""){
    alert("Target field cannot be empty");
    return false;
  }
}