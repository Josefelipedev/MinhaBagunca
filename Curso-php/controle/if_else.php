<<<<<<< HEAD
<div class="titulo">If Else</div>

<?php
echo "Linha 1";
echo "Linha 2";

if(false)//false só valido apenas para primeira linha sem {}
    echo "Serei impresso?";
    echo "<br>Serei impresso novamente?";

if(true){//; colocando ele desligar o bloco de codigo
    echo "Serei impresso?";
    echo "<br>Serei impresso novamente?";

}
=======
<div class="titulo">If e Else</div>

<?php
if(true){  //colocar ; terminar e não executa o bloco
    echo "Serei impresso?<br>";
    echo "Serei impresso novamente?";
}// "" string vazia vai ser false e string" " com espaço ou algum coisa vai ser true
   

if(true){
    echo "Verdadeiro<br> - Parte A ";
    echo "Verdadeiro<br> - Parte B ";
}else{
    echo "Falso<br> - Parta A";
    echo "Falso<br> - Parta B";
}
if(false){
    echo "Passo A <br>";
}else if(true){
    echo "Passo B<br>";
}else{
    echo "Ultimo Passo<br>";
}



echo "Fim<br>";
>>>>>>> 26a05fb064468e903486d6fa54e76a233c68dab3
