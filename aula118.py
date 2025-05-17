def adiciona_clientes(nome, lista=None): # se o valor padrão for mutável, [], {}, set(), tem que criar com None
    if lista is None:
        lista = []
    lista.append(nome)
    return lista

lista1 = []
cliente1 = adiciona_clientes('Luiz', lista1)
adiciona_clientes('Joana', cliente1)
adiciona_clientes('Fernando', cliente1)
cliente1.append('João')

cliente2 = adiciona_clientes('Helena')
adiciona_clientes('Maria', cliente2)

print(cliente1)
print(cliente2)
