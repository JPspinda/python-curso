# Abstração
# Log
from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log.txt' # o python entende que é para concatenar a string

class Log:
    def _log(self, msg):
        raise NotImplementedError('Implemente o método log') 
    
    def log_error(self, msg):
        return self._log(f'Error: {msg}')
    
    def log_success(self,msg):
        return self._log(f'Sucesso: {msg}')
    
    
class LogFileMixin(Log):
    def _log(self, msg):
        msf_formatada = f'{msg} ({self.__class__.__name__})'
        print('Salvando no Log:', msg)
        with open(LOG_FILE, 'a', encoding='utf8') as arquivo:
            arquivo.write(msg)
            arquivo.write('\n')
    
class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')    
    
if __name__ == '__main__': # se o módulo for o __main__ ele irá executar
    lp = LogPrintMixin()
    lp.log_error('Qualquer coisa')
    lp.log_success('Que legal')
    lf = LogFileMixin()
    lf.log_error('Qualquer coisa')
    lf.log_success('Que legal')
    print(LOG_FILE)