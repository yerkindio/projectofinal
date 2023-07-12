$(document).ready(function(){
    $("#formulario").submit(function(e){
        e.preventdefault(); 
        var nombre =$("#Nombre").val;
        var password =$("#password").val;

        var msjMostrar="";
        let enviar = false

        if(nombre.trim().length < 4 || nombre.trim().length > 10){
            msjMostrar +="El nombre debe tener entre 5 y 15 caracteres";
            enviar = true;
        }
        var letra = nombre.value.charAT(0);
        if(!esMayuscula(letra)){
            msjMostrar += "La primera letra debe estar en + mayúscula";
            enviar = true;
        }
        if(enviar){
            $("#warnings").html(msjMostrar);
        }
        else{
            $("#warnings").html("enviado");
        }
        });

        function esMayuscula(letra){
            if(letra == letra.toUpperCase()){
                return true;
            }
            else{
                return false;
            }
        }
        
    });