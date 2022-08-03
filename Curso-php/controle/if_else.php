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