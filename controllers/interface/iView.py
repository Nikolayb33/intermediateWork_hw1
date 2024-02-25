from abc import ABCMeta, abstractmethod

class iView():
    __metaclass__ = ABCMeta
    
    # задаем методы класса
    # задаем контроллер
    @abstractmethod
    def setContr(self, controller):
        "задает контроллер во view"
    
    # вводим имя заметки
    @abstractmethod
    def name(self):
        "для прописывания в консоли названия заметки"
    
    # вводим тело заметки
    @abstractmethod
    def body(self):
        "для прописывания в консоли тела заметки"
    
    # о создании заметки
    @abstractmethod
    def saveNote(self):
        "о создани заметки"
    
    # # начало работы программы
    # def viewRun(self):
    #     "файл запуска"
    
    # main метод
    @abstractmethod
    def main(self):
        "файл запуска"