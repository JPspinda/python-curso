# with open('aula149.txt', 'w') as arquivo:
#     ...

class MyContextManager:
    def __init__(self, caminho_arquivo, modo):
        self.caminho_arquivo = caminho_arquivo
        self.modo = modo
        self._arquivo = None
    
    def __enter__(self): # quando entra no "with" ele executa o __enter__
        print('ABRINDO ARQUIVO')
        self._arquivo = open(self.caminho_arquivo, self.modo, encoding= 'utf8')
        return self._arquivo
        
    def __exit__(self, class_exception_, exception_, traceback_): # quando sai do with ele executa o __exit__
        print('FECHANDO ARQUIVO')
        self._arquivo.close()
        
        raise class_exception_('Minha mensagem') # quando lança o raise o que está abaixo não será executado
        
        print(class_exception_)
        print(exception_)
        print(traceback_)
        
        return True # tratei a exceção

with MyContextManager('aula149.txt', 'w') as arquivo:
    arquivo.write('Linha1\n')
    arquivo.write('Linha2\n', 123)
    arquivo.write('Linha3\n')
    print('WITH', arquivo)