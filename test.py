from settings import *
import pygame
import time


pygame.init()



window = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
clock = pygame.time.Clock()

text = pygame.font.Font('Fonts/IrishGrover.ttf',68)
background = pygame.image.load('Images/background.png')

window.blit(background,(0,0))

menu_buttons = text.render('Play', 1 , (0,0,0), (95,125,125))
window.blit(menu_buttons,(100,250))
pygame.display.update()

surf = pygame.Surface((50,50))
surf.fill((255,0,0))


window.blit(surf,(100,500))





   


class Button():
    def button_click_check(self, button_coords):
       press = pygame.mouse.get_pressed(num_buttons=3)
       if press[0] == 1:
           self.button_coords = button_coords
           self.coords = pygame.mouse.get_pos()
           if (self.button_coords[0] < self.coords[0] <= (self.button_coords[0] + self.button_coords[2])) & (self.button_coords[1] < self.coords[1] <= (self.button_coords[1] + self.button_coords[3])):
               
               pygame.draw.rect(window, (255,0,0), self.button_coords) 
               pygame.display.update()
               time.sleep(0.2)
               press = False
                
    
    def is_cursor_on_button(coords):
        if event.type == pygame.MOUSEMOTION:
                coords = pygame.mouse.get_pos()
                if (coords[0] < coords[0] <= (coords[0] + coords[2])) & (coords[1] < coords[1] <= (coords[1] + coords[3])):
                    pygame.draw.rect(window, (255,0,0), coords)
                else:
                    pygame.draw.rect(window, (0,0,255), coords)
    
    def get_coords(self):
        return (self.x, self.y, self.W, self.H)    
        #Interface.is_cursor_on_button(self.coords)

    def update(self):
        self.button_click_check(self.get_coords())

    def draw(self):
        pygame.draw.rect(window, (0,0,255), self.get_coords()) 

    def __init__(self, x, y, W, H):
        objects.append(self)

        self.x = x
        self.y = y 
        self.W = W
        self.H = H 
        
        

        objects[max(0,len(objects) - 1)].draw()

    
    
objects = []

Button1 = Button(100,100,50,50)
Button2 = Button(200,200,50,50)
Button3 = Button(300,300,50,50)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    for object in objects:
        object.update()    
    
    #display.fill('black')    
    
   
    #for object in objects:
     #   object.draw()
            
        
    pygame.display.update()    
    clock.tick(60)
    

