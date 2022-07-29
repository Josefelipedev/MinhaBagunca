<div class="titulo">Desafio String</div>

<?php
 echo str_word_count("!AbcaBcabc") . '<br>';

 echo stripos("!AbcaBcabc", 'abc') . '<br>';
 echo strpos("!AbcaBcabc", 'abc') . '<br>';
 echo strpos(strtolower("!AbcaBcabc", 'abc')) . '<br>';