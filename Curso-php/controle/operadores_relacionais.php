<div class="titulo">OP. Relacionais</div>

<?php

var_dump(1 == 1);
echo "<br>";
var_dump(1 > 1);
echo "<br>";
var_dump(1 >= 1);
echo "<br>";
var_dump(1 <= 1);
echo "<br>";
var_dump(1 <> 1);
echo "<br>";
var_dump(1 != 1);

var_dump(1 == "1");
echo "<br>";
var_dump(1 === "1");//  vai olhar o tipo também 
echo "<br>";
var_dump(1 != "1");
echo "<br>";
var_dump(1 !== "1");//  vai olhar o tipo também 

echo "<p>Relacionais no IF/ELSE</p><hr>";
$idade = 75;
if($idade < 18){
    echo "Menor de idade<br>";
}else if($idade <= 65){
    echo "Adulto<br>";
}else{
    echo "Terceira Idade = $idade!<br>";
}
echo "<p>Spaceship</p><hr>";
var_dump(5 <=> 3); // vai retorna 1(se for maior ) ou 0(se for iguais) ou -1 se o numero da direita for maior 
echo "<br>";
var_dump(3 <=> 3);
echo "<br>";
var_dump(3 <=> 50);

echo "<p>Valores pode ser V ou F</p><hr>";
var_dump(!!5);
echo "<br>";
var_dump(!!0);
echo "<br>";
var_dump(!!"");




?>
<style>
    p{
        margin-bottom:0px;
    }

    hr{
        margin-top:0px
    }

</style>