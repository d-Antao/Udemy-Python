#Abstract
#Herança - é um
from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log.txt'

class log:
    def _log(self,msg):
        raise NotImplementedError('Implemente o método log')

    def log_error(self,msg):
        return self._log(f'Error: {msg} ')
    
    def log_success(self,msg):
        return self._log(f'Success: {msg} ')

class LogFileMixin(log):
    def _log(self,msg):
        msg_formatada = (f'{msg} ({self.__class__.__name__})')
        print('save in log')
        with open(LOG_FILE,'a') as file:
            file.write(msg_formatada)
            file.write('\n')

class LogPrintMixin(log):
    def _log(self,msg):
        print(f'{msg} ({self.__class__.__name__})')
        
          
if __name__ == '__main__' :  
    lp =LogFileMixin()
    lp.log_error('qualquer coisa')
    lp.log_success('resoltou')
    lf =LogFileMixin()
    lf.log_error('qualquer coisa')
    lf.log_success('resoltou')
    