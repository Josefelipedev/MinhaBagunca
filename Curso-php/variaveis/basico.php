<div class="titulo">Variáveis</div>


<?php

$numeroA = 13 ;
echo $numeroA, '<br>';
var_dump($numeroA);

echo '<br>';
$a = 3;
$b = 16;
$somaDosNumeros = $a + $b;
echo $somaDosNumeros;

echo '<br>';

echo isset($somaDosNumeros);

unset($somaDosNumeros);
echo '<br>';
echo var_dump($somaDosNumeros);

$variavel = "Agora sou um string";
echo "<br>" .$variavel;

// Nomes de variável

$var = "valida";
$var2 = "valida";
$VAR3 = "valida";
$_var_4 = "valida";
$vâr5= "valida"; // evitar
//$6var = "invalida";
//%var7%= "invalida";
//%var8%= "invalida";