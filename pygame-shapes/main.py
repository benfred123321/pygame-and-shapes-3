import pygame

pygame.init()

#creating screen
screen= pygame.display.set_mode((800,800))

#adding title to this game window
pygame.display.set_caption("pygame and shapes")

#adding backround coulor to your screen
screen.fill("sky blue")

pygame.display.update()
circle_color=(125,65,152)
class Circle():
    def __init__(self,color,pos,radius,width):
        self.radius=radius
        self.color=color
        self.pos=pos
        self.width=width
        self.surface=screen
    def draw(self):
        self.draw_circle = pygame.draw.circle(self.surface,self.color,self.pos,self.radius,self.width)
    def grow_circle(self,radius):
        self.radius+= radius
        # += is to increase the value of the left valable with the amount of the right valable 
        self.draw_circle = pygame.draw.circle(self.surface,self.color,self.pos,self.radius,self.width)

circle = Circle(circle_color,(400,400),20,5)
while True:
    
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            screen.fill("white")
            circle.draw()
            pygame.display.update()
        elif event.type == pygame.MOUSEBUTTONUP:
            screen.fill("white")
            circle.grow_circle(20)
            pygame.display.update()

    
