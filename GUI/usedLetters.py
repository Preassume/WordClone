import pyray as pr
from GUI.letterbox import Letterbox

offset = {
    'Q': 0,
    'W': 0,
    'E': 0,
    'R': 0,
    'T': 0,
    'Y': 0,
    'U': 0,
    'I': 0,
    'O': 0,
    'P': 0,
    'A': 1,
    'S': 1,
    'D': 1,
    'F': 1,
    'G': 1,
    'H': 1,
    'J': 1,
    'K': 1,
    'L': 1,
    'Z': 2,
    'X': 2,
    'C': 2,
    'V': 2,
    'B': 2,
    'N': 2,
    'M': 2,
}

class UsedLetters():
    def __init__(self, **kwargs):
        self.x = 60
        self.y = 600
        self.size = 40
        
        if 'x' in kwargs:
            self.x = kwargs['x']
            
        if 'y' in kwargs:
            self.y = kwargs['y']
            
        if 'size' in kwargs:
            self.size = kwargs['size']
        
        self.letters = {}
        
        i = 0
        for Letter in offset:
            #xVal = i
            xVal = i
            if xVal >= 19:
                xVal -= 19
            elif xVal >= 10:
                xVal -= 10
            
            self.letters[Letter] = Letterbox(
                size = self.size,
                x = self.x + (int(self.size / 2) * offset[Letter] + (xVal * (self.size + 10))),
                y = self.y + offset[Letter] * (self.size + 10),
                letter = Letter
            )
            i += 1
            
            
    def reset(self):
        for i in self.letters:
            self.letters[i].reset()
            
    def draw(self):
        for l in self.letters:
            self.letters[l].draw()