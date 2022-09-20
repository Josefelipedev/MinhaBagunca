<div class="titulo">Argumentos Padrão</div>
<?php

    function saudacao($nome = 'Senhor(a)', $sobrenome ='Client'){
        return "Bem vindo , $nome $sobronem !<br>";

    }
echo  saudacao();
echo  saudacao(Null);
echo saudacao(null,null);
echo saudacao("Mestre","Supremo");

function anotarPedido($comida,$bebida = 'Agua'){
    echo "Para comer: $comida <br>";
    echo "Para beber: $bebida <br>";


}

anotarPedido('Hamburguer');
anotarPedido('Pizza','Refrigerante');