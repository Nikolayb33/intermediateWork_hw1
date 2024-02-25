from models.domain.Model import Note
from View import View


class Controller:
    
    # конструктор
    def __init__(self):
        self.model = Note()
        self.view = View(self)
    
    def main(self):
        self.view.viewRun()
    
    
    # клиентский код
if __name__ == "__main__":
    
    
    noteContr = Controller()
    noteContr.main()

        
        
        
        
        
    