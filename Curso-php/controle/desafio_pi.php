<div class="titulo">Desafio do PI</div>

<?php
echo pi();
$pi = 3.14;


if($pi <=> pi()){
    echo "<br>Iguais";
}else{
    echo"<br>Diferentes!";
}
$piErrado = 2.8;


//Resposta do professor
echo '<br>' . ($pi - pi());
echo '<br>' . ($pi - $piErrado);

if($pi - pi() <= 0.01){
    echo "<br> Praticamento iguais!";
}else{
    echo "<br> Praticamento iguais!";
}