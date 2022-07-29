<div class="titulo">Tipos String</div>

<?php
echo 'Eu sou um string';
echo '<br>';
var_dump("Eu também");
echo '<br>';

// concatenção

echo "Nós também" . 'somos';
echo '<br>', "També aceito", "Virgulas";
echo '<br>';
echo "'Teste'" . '" Teste "' . "\"Teste\"";

print("<br>Também existe o função print");
print"<br>Também existe o função print";


//Algumas funções 

echo '<br>' . strtoupper('Maximizado');
echo '<br>' . strtolower('Minimizado');
echo '<br>' . ucfirst('Só a primeira letra');
echo '<br>' . ucwords('todas as palavras');
echo '<br>' . strlen('Quantas letras?');
echo '<br>' . mb_strlen('Quantas é letras?', "utf-8");
echo '<br>' . substr('Só uma parte mesmo', 7 , 6);
echo '<br>' . str_replace('isso', 'aquilo', 'troca isso isso');

