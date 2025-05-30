class A:
    def __new__(cls, x):
        instancia = super().__new__(cls)
        return instancia
    
    def __init__(self, x):
        self.x = x
        print('Sou o init')
        
    def __repr__(self):
        return 'A()'
    
a = A(123)
# a = object.__new__(A)
# a.__init__()
print(a.x)