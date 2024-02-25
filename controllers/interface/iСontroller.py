from abc import ABCMeta, abstractmethod

class iСontroller():
    __metaclass__ = ABCMeta
    
    # метод контроллера
    @abstractmethod
    def main(self):
        "файл запуска" 
    