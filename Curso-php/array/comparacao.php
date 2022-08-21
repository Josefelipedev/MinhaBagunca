<div class="titulo">Comparação Arrays</div>


<?php

$arr1 = ['nome' => 'Maria' , 'Idade'=> 20];
$arr2 = ['nome' => 'Maria' , 'Idade'=> 20];
var_dump($arr1 == $arr2);
echo '<br>';
$arr3 = ['Idade'=> 20, 'nome' => 'Maria'];
echo '<br>';
var_dump($arr1 == $arr3);
echo '<br>';
var_dump($arr1 === $arr3);
echo '<br>';
var_dump($arr1 != $arr3);
echo '<br>';
echo '<br>';

$arr4 = ['Idade'=> '20', 'nome' => 'Maria'];
var_dump($arr1 == $arr4);