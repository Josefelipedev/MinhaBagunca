<div class="titulo">Operações </div>

<?php

$dados1 = [
    "nome" => "Jose",
    "idade" => 28
];

$dados2 = [
  "naturalidade" => "Fortaleza"

];
// sem tem dados  do mesmo valor pegar o que está primeiro na soma 
$dadosCompletos = $dados1 + $dados2;

print_r($dadosCompletos);
echo "<br>" . is_array($dadosCompletos);// 1 true 0 false
echo "<br>" . count($dadosCompletos);// contar
echo '<br>';

$indice = array_rand($dadosCompletos);
echo "$indice = $dadosCompletos[$indice]";
echo '<br>';
echo "{$dadosCompletos['idade']}";
echo '<br>';
echo "${dadosCompletos['idade']}";

unset($dadosCompletos["nome"]);
echo '<br>';
print_r($dadosCompletos);
echo '<br>';
unset($dadosCompletos);
var_dump($dadosCompletos);

$impares = [1,3,5,7,9];
$pares = [0,2,4,6,8];

$decimais = $pares + $impares;
echo '<br>';
print_r($decimais);

$decimais = array_merge($pares, $impares);
echo '<br>';
print_r($decimais);
echo '<br>';
sort($decimais);
print_r($decimais);