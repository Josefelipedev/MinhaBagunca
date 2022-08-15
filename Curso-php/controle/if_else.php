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

if(true)
    echo "Verdadeiro<br>";

else
    echo "Falso<br>";

echo "Fim<br>";


if(false){
    echo "Passo A<br>";

}else if(true){
echo "Passo B<br>";
}
else if(true){
    echo "Passo c<br>";
}else{
    echo "Ultimo Passo<br>";
}
echo "Fim<br>";