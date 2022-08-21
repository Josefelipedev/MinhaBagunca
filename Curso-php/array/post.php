<div class="titulo">$_POST</div>


<form action="#" method="post">
    <input type="text" name="nome" id="">
    <br>
    <input type="text" name="sobrenome" id="">
    <select name="estado" id="">
        <option value="AC">Acre</option>
        <option value="BA">Bahia</option>

    </select>

    <button>Enviar</button>
</form>

<style>
     form > *{
        margin : 5px;
        font-size: 1.8rem;
     }   
</style>
<?php
print_r($_GET);
echo '<br>';
print_r($_POST);
echo '<br>';
echo "<br>" . count($_POST);


