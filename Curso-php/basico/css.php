<div class="titulo">   Intergração CSS</div>


<h1 center dobro>
    <?php
        echo 'Olá ';
        echo '<small>';
        echo ' Mundo';
        echo '</small>';
        
        
        
        ?>
        
</h1>
<?= "<div center azul> Outra forma de me 'expressar' </div>"?>
<br>
<div><button><?= "Legal" ?></button></div>

<style>

    button{
            padding :2px 20px;
            background-color: #4286f4;
            color:#EEE;
            font-weight:bold;
            border-radius: 10px;}
    [center]{
        display: flex;
        justify-content:center;

    } 
    [azul]{
        color:#4286f4;
    }    
    [dobro]{
        font-size: 2rem;
    }
</style>
