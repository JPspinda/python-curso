class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []
        
    def inserir_endereço(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))
        
    def inserir_endereço_externo(self, endereco):
        self.enderecos.append(endereco)
        
    def listar_endereco(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)
        
class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero
        
    def __del__(self):
        print('APAGANDO,', self.rua, self.numero) # assim que acabou o código o Python deleta as classes, apaga o lixo
        
cliente_1 = Cliente('Maria')
cliente_1.inserir_endereço('Av Brasi', 30)
cliente_1.inserir_endereço('Manoel Porto', 421)
endereco_externo = Endereco('Av saudade', 981)
cliente_1.inserir_endereço_externo(endereco_externo)
cliente_1.listar_endereco()

del cliente_1 # o python acaba os endereços junto ao cliente

print('################################Aqui termina meu código')