<div class="titulo">Array</div>


<?php

$lista = array(1,2,3.5,"Texto");

echo $lista . '<br>';
var_dump($lista) . '<br>';
echo '<br>';
print_r($lista);
echo '<br>';
echo '<br>'. $lista[0];
echo '<br>'. $lista[1];
echo '<br>'. $lista[2];
echo '<br>' .$lista[3];
echo '<br>';

$texto = 'Esse é um texto de teste';
echo  '<br>'. $texto[0];
echo  '<br>'. $texto[2];
echo  '<br>'. $texto[11]; //cuidado pode dar problemas
echo  '<br>'. mb_substr($texto, 10, 1); // melhor
