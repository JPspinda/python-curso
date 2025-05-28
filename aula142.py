from abc import ABC, abstractmethod 

class Log(ABC):
    @abstractmethod # faz com que o Log seja uma classe abstrata sem precisar do erro
    def _log(self, msg): ...
    
    def log_error(self, msg):
        return self._log(f'Error: {msg}')
    
    def log_success(self, msg):
        return self._log(f'Sucesso: {msg}')
    
class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')   # se eu não implementar o método abstrato a classe que herda de Log também será abstrata

l = LogPrintMixin()
l.log_error('Oi')