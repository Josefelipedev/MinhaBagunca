<div class="titulo">Constantes</div>

<?php

const FRUTAS = ['laranja', 'abacaxi'];
//FRUTAS[0] = 'banana'; não e possível
echo FRUTAS[0];

const CARROS = ["fiat"=> "UNO", "Fort" => 'Fiesta'];

define('CIDADES', Array('Bele Horizonte','Recife'));
//CIDADES[] = 'Rio de janeiro';
echo '<br>'. CIDADES[1];
