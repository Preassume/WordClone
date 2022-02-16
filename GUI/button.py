import pyray as pr

class Button():
    def __init__(self, **kwargs):
        self.hovering = False
        self.rec = pr.Rectangle()
        
        if 'text' in kwargs:
            self.text = kwargs['text']
        else:
            self.text = 'button'
        
        if 'x' in kwargs:
            self.rec.x = kwargs['x']
        else:
            self.rec.x = 0
        
        if 'y' in kwargs:
            self.rec.y = kwargs['y']
        else:
            self.rec.y = 0
        
        if 'w' in kwargs:
            self.rec.width = kwargs['w']
        else:
            self.rec.width = 30
        
        if 'h' in kwargs:
            self.rec.height = kwargs['h']
        else:
            self.rec.height = 20
    
    def isHovering(self):
        if pr.check_collision_point_rec(pr.get_mouse_position(), self.rec):
            self.hovering = True
        else:
            self.hovering = False
        return self.hovering
    
    def draw(self):
        backColor = pr.Color(0, 0, 0, 255)
        textColor = pr.Color(255, 255, 255, 255)
        
        if self.hovering:
            backColor = pr.Color(255, 180, 0, 255)
            textColor = pr.Color(0, 0, 0, 255)
        
        pr.draw_rectangle_rec(self.rec, backColor)
        pr.draw_text(self.text, int(self.rec.x), int(self.rec.y), int(self.rec.height), textColor)
    
    