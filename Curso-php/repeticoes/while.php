<div class="titulo">While</div>

<?php
const VALOR_LIMITE = 5;
$contador = 10; 

do{
    echo "Whilie $contador <br>";
    $contador++;
}while($contador < VALOR_LIMITE);


while($contador < VALOR_LIMITE){
    echo "Whilie $contador <br>";
    $contador++;
    
}

while(true){
    echo "while(true $contador<br>";
    $contador++;
    if($contador >= VALOR_LIMITE)break;
}