import datetime
import os



class Note():
    
    # конструктор
    def __init__(self):

        self.id = 0

        self.dictionaryNote = dict()
        
    
    #создание имени заметки
    def createNameNote(self):
        return input()
        
    #создание тела
    def createBodyNote(self):
        return input()
    
    # пишет путь файла 
    def printNamePathFile(self):
        return self.path_file
    
     

    
    # посмотреть тело заметки
    def readBodyNote(self, key_name):
        with open(f'{key_name}.csv', 'r') as f:
            for line in f:
                print(line.split("\n")[0])
        
        

        
    # создает файл с заметкой
    def createFileNote(self, key_name, id, date_of_note, body_note):
        with open(f'{key_name}.csv', 'w+') as f:
            f.write(id + "\n")
            f.write(date_of_note + "\n")
            f.write(body_note + "\n")
    

    
    
    
    # 3 основных метода
    # ______________________
    # создание заметки
    def createNote(self, name_note, body_note):
        self.id += 1 #присваиваем новое ид
        self.date_now = datetime.datetime.now() # фиксируем дату создания
        self.date_of_note = datetime.date.strftime(self.date_now, '%Y-%m-%d %H:%M:%S') # подгоняем дату под шаблон, который нужен
        self.createFileNote(name_note, str(self.id), self.date_of_note, body_note) # создаем заметку
        
        
    # чтение заметки
    def readNote(self, name_note):
        self.readBodyNote(name_note)
    

    # удаление заметки
    def deleteNote(self, name_note):
        path_file = os.getcwd()
        os.remove(path_file + f"/{name_note}.csv")
    # ____________________________
    
       

        
        