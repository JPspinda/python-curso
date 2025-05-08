def generator(n=0, maximum=10): #toda a function generator usa yield
    while True:
        yield n
        n += 1
        
        if n > maximum:
            return
        
        

gen = generator(maximum=40)
for n in gen:
    print(n)


# print(next(gen)) #enquanto eu chamar o next() ele vai retornar tudo até o próximo yield
# print(next(gen))
# print(next(gen))