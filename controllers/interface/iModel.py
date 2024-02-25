from abc import ABCMeta, abstractmethod

class iModel():
    __metaclass__ = ABCMeta
    
    # методы заметок
    
    #получени название заметки по индексу
    @abstractmethod
    def getNameOfNoteById(self, id):
        "Получить название заметки по номеру"
    
    # получение тела
    @abstractmethod
    def getBodyOfNote(self, name):
        "Получить тело заметки по имени"
        
        
    # задание тела 
    @abstractmethod
    def setBodyOfNote(self, name):
        "Поменять тело заметки по имени"
        
        
    # создание файла
    @abstractmethod 
    def createFileNote(self, name):
        "Создать файл с заметкой"
    
    