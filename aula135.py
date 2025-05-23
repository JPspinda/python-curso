class Carrinho:
    def __init__(self):
        self._produtos = []
        
    def total(self):
        return sum([p .preco for p in self._produtos])
    
    def listar_produtos(self):
        print()
        for produto in self._produtos:
            print(produto.nome, produto.preco)
        print()
        
    def inserir_produtos(self, *produtos):
        # self._produtos.extend(produtos)
        # self._produtos += produtos
        for produto in produtos:
            self._produtos.append(produto)
    
class Produtos:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        
carrinho = Carrinho()
p1, p2 = Produtos('Caneta', 1.20), Produtos('Camisetas', 20)
carrinho.inserir_produtos(p1, p2)
carrinho.listar_produtos()
print(carrinho.total())