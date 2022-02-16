import pyray as pr

class Letterbox():
    def __init__(self, **kwargs):
        self.backColor = pr.Color(0, 0, 0, 255)
        self.foreColor = pr.Color(255, 255, 255, 255)
        self.size = 60
        self.x = 60
        self.y = 60
        self.letter = ''
        self.status = 'clear'
        
        if 'size' in kwargs:
            self.size = kwargs['size']
        
        if 'x' in kwargs:
            self.x = kwargs['x']
        
        if 'y' in kwargs:
            self.y = kwargs['y']
        
        if 'letter' in kwargs:
            self.letter = kwargs['letter']
    
    def setLetter(self, letter):
        if letter == pr.KEY_BACKSPACE:
            self.letter = ''
            return True
        elif letter >= 65 and letter <= 90:
            self.letter = chr(letter)
            return True
        return False
    
    def letterClose(self):
        self.backColor = pr.Color(200, 150, 20, 255)
        self.foreColor = pr.Color(255, 255, 20, 255)
        self.status = 'close'
        
    def letterCorrect(self):
        self.backColor = pr.Color(20, 150, 20, 255)
        self.foreColor = pr.Color(20, 255, 20, 255)
        self.status = 'correct'
    
    def letterWrong(self):
        self.backColor = pr.Color(50, 50, 50, 255)
        self.foreColor = pr.Color(150, 150, 150, 255)
        self.status = 'wrong'
        
    def notWord(self):
        self.backColor = pr.Color(100, 20, 20, 255)
        self.foreColor = pr.Color(255, 70, 70, 255)
        self.status = 'notWord'
    
    def reset(self):
        self.backColor = pr.Color(0, 0, 0, 255)
        self.foreColor = pr.Color(255, 255, 255, 255)
        self.status = 'reset'
        
    def clear(self):
        self.reset()
        self.letter = ''
    
    def setStatus(self, status):
        if status == 'close':
            self.letterClose()
        elif status == 'correct':
            self.letterCorrect()
        elif status == 'wrong':
            self.letterWrong()
        else:
            self.reset()
    
    def draw(self):
        #pr.draw_rectangle_rec(self.rec, self.backColor)
        #pr.draw_rectangle_lines_ex(self.rec, 6, self.foreColor)
        pr.draw_rectangle(self.x, self.y, self.size, self.size, self.backColor)
        pr.draw_rectangle_lines_ex(pr.Rectangle(self.x, self.y, self.size, self.size), int(self.size/10), self.foreColor)
        
        textX = int(self.x + self.size / 3.5)
        textY = int(self.y + self.size / 5)
        textSize = int(self.size / 1.5)
        pr.draw_text(self.letter, textX, textY, textSize, self.foreColor)
        
        