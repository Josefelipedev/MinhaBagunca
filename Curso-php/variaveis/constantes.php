<div class="titulo">Constantes</div>

<?php

define('TAXA_DE_JUROS',5.9);
echo TAXA_DE_JUROS;
//TAXA_DE_JUROS = 2.5; error

const NOVA_TAXA = 2.5;
echo '<br>' . NOVA_TAXA;

$valorVariavel = 2.8;
//const(NOVISSIMA_TAXA = $valorVariavel); NÃO CONSEGUIR REALIZAR ISSO. 
define('NOVISSIMA_TAXA' , $valorVariavel);

echo '<br>' . NOVISSIMA_TAXA;

echo '<br>' . PHP_VERSION;
echo '<br>' . __LINE__;
echo '<br>' . __FILE__;
echo '<br>' . __DIR__;