import pyray as pr
from GUI.button import Button
from GUI.letterbox import Letterbox
from GUI.textbox import Textbox
from Dictionary.fiveLetter import fiveLetterDict
from game import WordGame

myBut = Button(text = b'b boi', x=100, y=300, w=300, h=80)
#myBox = Letterbox()
#myBox.setLetter('d')

myTx = Textbox(x=120)
myTx2 = Textbox(x=120, y=130, length=7)

myGame = WordGame()

pr.init_window(800, 700, "words bruh")
pr.set_target_fps(60)

def checkIsWord(word):
    if word in fiveLetterDict:
        return True
    return False

while not pr.window_should_close():
    pr.begin_drawing()
    pr.clear_background(pr.BLACK)
    
    #letter = pr.get_key_pressed()
    #if letter == pr.KEY_ENTER:
    #    word = myTx.getWord()
    #    myTx.checkWord("JEANS")
        #print(word)
        #print(checkIsWord(word))
    #elif letter:
    #    myTx.enterLetter(letter)
    
    #if myBut.isHovering():
    #    myBox.letterCorrect()
    #else:
    #    myBox.letterClose()
    
    #myBox.draw()
    #myBut.draw()
    #myTx.draw()
    #myTx2.draw()
    
    myGame.checkKey()
    
    myGame.draw()
    
    pr.end_drawing()
pr.close_window()
