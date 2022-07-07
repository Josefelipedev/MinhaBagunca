from contapoupanca import ContaPoupanca
from contacorrente import  ContaCorrente

cp = ContaPoupanca(111,222,00)
cp.despositar(10)


print('#######################')
cc = ContaCorrente(agencia=155,conta= 4444 , saldo= 0 , limite=500)
cc.despositar(100)
cc.sacar(250)
cc.sacar(500)
cc.despositar(1000)

