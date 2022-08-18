<div class="titulo">Desafio Operadores Lógicos</div>


<!-- 
    Dois trabalhos -> terça e quinta!
    --Se os dois forem executados -> TV 50' e Sorvete
    -Se apenas um for executado -> TV 32' e Sorvete
    -Se nenhum for execxutado -> Fica em casa Saudável!-->

 <form action="#" method="post">
    
    <div>
        <label for="t1">Trabalho 1 (Terça-feira):</label>
        <select name="t1" id="t1">
            <option value="1">Executado</option>
            <option value="0">Não executado</option>
        </select>
    </div>
    <div>
        <label for="t1">Trabalho 2 (Quinta-feira):</label>
        <select name="t2" id="t2">
            <option value="1">Executado</option>
            <option value="0">Não executado</option>
        </select>
    </div>
    <button>Executar</button>

 </form>   

 <style>
    button,select{
        font-size:1.8rem;
    }

 </style>

 <?php

 if($_POST['t1'] == 1 && $_POST['t2'] == 1 ){
        echo "Eles vão comprar um TV 50 e sorvete";
    }elseif($_POST['t1'] == 1 || $_POST['t2'] == 1){
        echo "Eles vão comprar um TV 32' e Sorvete";
    }else{
        echo "Fica em casa Saudável!";
    }

//    $t1 = $_POST['t1'] === '1';
//    $t2 = !!$_POST['t2'];
//    $tv = '';
//    $sorvete = false;

// echo $_POST['t1'];
 //echo $_POST['t2'];