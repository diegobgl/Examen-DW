function inicio(){
    document.getElementById("inicio").disabled = true;
}

///iniciosesion
function v_nombre(){
    var largo_rnombre = document.getElementById("nombre").value.length;
    if (largo_rnombre<3 || largo_rnombre > 15){
        document.getElementById("texto_nombre").innerHTML = "";
        document.getElementById("texto_nombre").style.color = "";
        document.getElementById("flag_nombre").value = "0";
    }else{
        document.getElementById("texto_nombre").innerHTML = "";
        document.getElementById("texto_nombre").style.color = "";
        document.getElementById("flag_nombre").value = "1";
    }
   
    var v1 = document.getElementById("flag_nombre").value;
    var v2 = document.getElementById("flag_pass").value;
    if (v1 =="1" && v2 =="1"){
        document.getElementById("inicio").disabled = false;
    }else{
        document.getElementById("inicio").disabled = true;
    }
}
function v_pass(){
    var largo_pass = document.getElementById("pass").value.length;
    if (largo_pass<6 || largo_pass > 10){
        document.getElementById("texto_pass").innerHTML = " ";
        document.getElementById("texto_pass").style.color = "";
        document.getElementById("flag_pass").value = "0";
    }else{
        document.getElementById("texto_pass").innerHTML = "";
        document.getElementById("texto_pass").style.color = "";
        document.getElementById("flag_pass").value = "1";
    }
   
    var v1 = document.getElementById("flag_nombre").value;
    var v2 = document.getElementById("flag_pass").value;
    if (v1 =="1" && v2 =="1"){
        document.getElementById("inicio").disabled = false;
    }else{
        document.getElementById("inicio").disabled = true;
    }
}
///fin iniciosesion





