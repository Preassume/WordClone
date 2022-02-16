import random
import pyray as pr
from GUI.textbox import Textbox
from GUI.usedLetters import UsedLetters
from GUI.button import Button
from Dictionary.fiveLetter import fiveLetterDict

class WordGame():
    def __init__(self, **kwargs):
        self.wordlen = 5
        self.size = 60
        self.y = self.size
        self.x = self.size
        self.boxCount = 0
        self.word = random.choice(fiveLetterDict)
        
        if 'size' in kwargs:
            self.size = kwargs['size']
        
        if 'y' in kwargs:
            self.y = kwargs['y']
        
        if 'x' in kwargs:
            self.x = kwargs['x']
        
        if 'wordlen' in kwargs:
            self.wordlen = kwargs['wordlen']
        
        self.textBoxes = []
        for i in range(6):
            self.textBoxes.append(Textbox(
                size = self.size,
                x = self.x,
                y = self.y + ((self.size + 10) * i),
                length = self.wordlen
            ))
        
        self.lettersUsed = UsedLetters(
            size = int(self.size * 0.67),
            x = self.x,
            y = self.y + 6 * (self.size + 10)
        )
        
    
    def incrementCounter(self):
        self.boxCount += 1
        if self.boxCount > 6:
            self.boxCount = 6
    
    def highlightLetters(self, result):
        for r in result:
            self.lettersUsed.letters[r].setStatus(result[r])
            
    def newGame(self):
        self.boxCount = 0
        self.word = random.choice(fiveLetterDict)
        self.lettersUsed.reset()
        for i in self.textBoxes:
            i.reset()
    
    def checkKey(self):
        key = pr.get_key_pressed()
        
        if key == pr.KEY_GRAVE:
            self.newGame()
            return
        
        if self.boxCount > 5:
            return
        
        if key == pr.KEY_ENTER:
            result = self.textBoxes[self.boxCount].checkWord(self.word)
            if result:
                self.highlightLetters(result)
                self.incrementCounter()
        elif key:
            self.textBoxes[self.boxCount].enterLetter(key)
    
    def draw(self):
        for b in self.textBoxes:
            b.draw()
        self.lettersUsed.draw()
        if self.boxCount > 5:
            pr.draw_text(self.word, 0, 0, self.size, pr.WHITE)