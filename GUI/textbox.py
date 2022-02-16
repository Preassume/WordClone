import pyray as pr
from GUI.letterbox import Letterbox
from Dictionary.fiveLetter import fiveLetterDict

class Textbox():
    def __init__(self, **kwargs):
        self.length = 5
        self.size = 60
        self.y = self.size
        self.x = self.size
        self.letterCount = 0
        
        self.red = False
        
        if 'length' in kwargs:
            self.length = kwargs['length']
        
        if 'size' in kwargs:
            self.size = kwargs['size']
        
        if 'y' in kwargs:
            self.y = kwargs['y']
        
        if 'x' in kwargs:
            self.x = kwargs['x']
        
        self.boxes = []
        for i in range(self.length):
            self.boxes.append(Letterbox(
                size = self.size,
                x = self.x + (i * (self.size + 10)),
                y = self.y
            ))
    def decrementCounter(self):
        self.letterCount -= 1
        if self.letterCount < 0:
            self.letterCount = 0
    
    def incrementCounter(self):
        self.letterCount += 1
        if self.letterCount > self.length:
            self.letterCount = self.length
        
    def enterLetter(self, letter):
        if self.red:
            self.red = False
            for b in self.boxes:
                b.reset()
        if letter == pr.KEY_BACKSPACE:
            self.decrementCounter()
            self.boxes[self.letterCount].setLetter(letter)
        elif self.letterCount < self.length:
            if self.boxes[self.letterCount].setLetter(letter):
                self.incrementCounter()
                
    def getWord(self):
        word = ''
        for b in self.boxes:
            if b.letter == '':
                return False
            word += b.letter
        return word
    
    def checkWord(self, word):
        myWord = self.getWord()
        if not myWord in fiveLetterDict:
            for i in self.boxes:
                self.red = True
                i.notWord()
            return False
        result = {}
        for i in range(5):
            if myWord[i] == word[i]:
                self.boxes[i].letterCorrect()
            elif myWord[i] in word:
                self.boxes[i].letterClose()
            else:
                self.boxes[i].letterWrong()
            result[myWord[i]] = self.boxes[i].status
        return result
    
    def reset(self):
        self.letterCount = 0
        for i in self.boxes:
            i.clear()
    
    def draw(self):
        for b in self.boxes:
            b.draw()