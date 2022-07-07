carrinho = []

carrinho.append(('Produto 1',30))
carrinho.append(('Produto 2',50))
carrinho.append(('Produto 3',20))
somar = []
somar = [ (x[1]) for x in carrinho ] #posso colocar float int e  posso usar o sum nesse linha sum(codigo)
print(sum(somar))