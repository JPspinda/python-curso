class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor
        
    @property # faz um método se comportar como atributo, não preciso chamar o mátod com parênteses '()'
    def cor(self):
        print('PROPERTY')
        return self.cor_tinta
    
    @property
    def cor_tampa(self):
        return 123456

caneta = Caneta('Azul')        
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor_tampa)