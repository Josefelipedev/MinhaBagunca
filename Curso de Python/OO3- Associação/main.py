from classe import Escritor
from classe import Caneta
from classe import MaquinaDeEscrever



escritor = Escritor("José Felipe")
caneta = Caneta('Bic')
maquina = MaquinaDeEscrever()
# print(escritor.nome)
# print(caneta.marca)
# maquina.escrever()

escritor.ferramenta = maquina
escritor.ferramenta.escrever()

del escritor
print(caneta.marca)
maquina.escrever()