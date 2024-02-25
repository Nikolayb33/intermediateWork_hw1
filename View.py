from controllers.interface.iView import iView


class View(iView):
    
    
    # конструктор
    def __init__(self, controller):
        self.controller = controller
            
    # сеттер для контроллера
    def setContr(self, controller):
        self.controller = controller
    
    #  старт программы
    def start(self):
        pr_start = input("Введите команду: 'создать', 'прочитать', 'удалить', 'выход'\n")
        return pr_start
    
    # вводим имя заметки
    def name(self):
        pr_name = "Введите название заметки"
        return pr_name
    
    # вводим тело заметки
    def body(self):
        pr_body = "Введите тело заметки"
        return pr_body
    
    # вводим новое тело заметки
    def setBody(self):
        pr_set_body = "Введите новое тело заметки"
        return pr_set_body
        
    
    # о создании заметки
    def saveNote(self):
        pr_save_body = "Заметка создана"
        return pr_save_body
    
    # об удалении заметки
    def deleteNote(self):
        pr_delete_note = "Заметка удалена"
        return pr_delete_note
    
    # начало работы программы
    def viewRun(self):
        
        flag = True
        
        while flag == True:
            start = self.start()
            if start == "создать":
                print("_____________")
                print(self.name())
                name_note = self.controller.model.createNameNote()    
                print("_____________")
                print(self.body())
                body_note = self.controller.model.createBodyNote()    
                self.controller.model.createNote(name_note, body_note)
                # self.controller.model.createFileNote(name_note, body_note)
                print(self.saveNote())
                print("_____________")
                
            if start == "прочитать":
                print(self.name())
                name_note = self.controller.model.createNameNote()    
                print("_____________")
                self.controller.model.readNote(name_note)
                print("_____________")
                
            if start == "удалить":
                print(self.name())
                name_note = self.controller.model.createNameNote()
                self.controller.model.deleteNote(name_note)
                print(self.deleteNote())
                
                
            if start == "выход":
                break
        
        # self.controller.model.dictionaryNote[name] = [body, self.controller.model.date_of_note]
        # self.controller.model.createFileNote(name)
        # self.saveNote()
        
        # print(self.controller.model.dictionaryNote)
        
    
    # # main метод
    # def main(self):
    #     print("in main of view")
    #     name = self.name()
    #     body = self.body()
        
    
    