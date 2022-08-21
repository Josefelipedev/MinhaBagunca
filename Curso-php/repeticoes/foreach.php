<div class="titulo">Foreach</div>

<?php 
$array =[1=>"Domingo","Segunda", "Terça", "Quarta", 
"Quinta", "Sexta", "Sábado"];

foreach($array as $valor){
    echo "$valor <br>";
}
echo "<hr>";
foreach($array as $indice => $valor){
    echo "$indice => $valor <br>";
}

$matrix = [
    ['a', 'e','i','o','u'],
    ['b','c','d']
];

foreach($matrix as $linha){
    foreach($linha as $letra){
        echo " $letra";

    }
    echo "<br>";
}

$numero = [ 1,2,3,4,5];
// & pegar o enderoço e mudar o array sem ele não mudar

foreach($numero as &$dobrar){
    $dobrar *= 2;
    echo "$dobrar <br>";
}

print_r($numero);