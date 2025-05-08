import sys

iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable) # tem __iter__ e __next__
lista = [n for n in range(1000000)]
generator = (n for n in range(1000000)) # isso não gera uma tupla e sim um generator

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

# for n in generator:
#     print(n)

# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))