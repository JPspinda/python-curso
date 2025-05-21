class Carro:
    def __init__(abc, nome='Sei lá'): # o método init sempre retorna None, poderia também alterar o nome do self que iria funcionar por ser o primeiro parâmetro
        abc.nome = nome
    
    def acelerar(efg):
        print(f'{efg.nome} está acelerando...')
        
fusca = Carro('Fusca')
fusca.acelerar()
Carro.acelerar(fusca)
# print(fusca.nome)
# fusca.acelerar()

celta = Carro(nome='Celta')
celta.acelerar()
Carro.acelerar(celta)
# print(celta.nome)
# celta.acelerar()