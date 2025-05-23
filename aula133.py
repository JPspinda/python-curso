"""
public, private, protected

    (sem underline) = public
        Pode ser usado em qualquer lugar do código
        
    (com 1 underline) = protecte
        não deve ser usado fora da classe ou das suas subclasses
        
    (com 2 underline) = private
        só deve ser usado na classe em que foi declarada
"""

from functools import partial

class Foo:
    def __init__(self):
        self.public = 'Isso é publico' # posso usar em qualquer lugar do código
        self._protected = 'Isso é protegido' # posso usar apenas na classe e nas subclasses
        self.__exemplo = 'Isso é privado' # posso usar apena na classe criada
        
    def metodo_publico(self):
        self._metodo_protected()
        print(self._protected)
        return 'Método Público'
    
    def _metodo_protected(self):
        return 'Método Protegido'
    
    def __metodo_private(self):
        return 'Privado'
    
f = Foo()
print(f.public)
print(f._protected)
print(f._metodo_protected())
# print(f.__metodo_private()) # isso não dá certo
print(f._Foo__metodo_private())
# print(f.public)
# print(f.metodo_publico())