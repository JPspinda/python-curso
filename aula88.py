lista = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2), 
    {0, 1}, {'nome': 'João'}
]

for item in lista:
    if isinstance(item, set): #com o isinstance() o computador sabe qual tipo a variável é
        print('SET')
        item.add(5)
        print(item)
        
    if isinstance(item, str):
        print('STR')
        print(item.islower(), item.upper(), isinstance(item, set))
        
    if isinstance(item, (int, float)):
        print('NUM')
        print(item, item * 2)
        