# class MinhaString(str): # a classe MinhaString herda a classe str do próprio Python
#     def upper(self):
#         print('CHAMOU UPPER')
#         retorno = super().upper()
#         print('DEPOIS DO UPPER')
#         return retorno
    
# string = MinhaString('Luiz')

# print(string.upper())

class A:
    atributo_a = 'valor a'
    
    def __init__(self, atributo):
        self.atributo = atributo
    
    def metodo(self):
        print('A')

class B(A):
    atributo_b = 'valor b'
    
    def __init__(self, atributo, outra_coisa):
        super().__init__(atributo)
        self.outra_coisa = outra_coisa
    
    def metodo(self):
        print('B')
        
class C(B):
    atributo_c = 'valor c'
    
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        print('EI, burlei o sistema')
    
    def metodo(self):
        # super(B, self).metodo() # estou chamando o método de B
        # super(C, self).metodo() # super().metodo()
        A.metodo(self)
        print('C')
      
# print(C.mro()) # um método de classe que retorna a ordem de herança e quais classes estão na classe herdeira
# print(B.mro())
# print(A.mro())
c = C('atributo', 'Qualquer')  
print(c.atributo)
print(c.outra_coisa)
c.metodo()
# print(C.atributo_a)
# print(C.atributo_b)
# print(C.atributo_c)
# c.metodo()