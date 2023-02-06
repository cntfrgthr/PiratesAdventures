import pygame
from random import randint
from settings import *
from time import sleep



pygame.init()


#Classes#Classes#Classes
#Classes#Classes#Classes
#Classes#Classes#Classes

class PlayingField():
    #Font init    
    text = pygame.font.Font('Fonts/IrishGrover.ttf', 32)

    babah_cards = []
    
    def draw(self):
        window.blit(self.image, (self.x, self.y)) 



class Button(PlayingField):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
        
        
    def draw(self):   #method override(specific for button)
        self.image.blit(self.text, (self.image.get_rect().center[0] - self.text.get_width() // 2, self.image.get_rect().center[1] - self.text.get_height() // 2)) 
        window.blit(self.image, (self.x, self.y))


    def button_state_checker(self):
        width = self.image.get_width()
        height = self.image.get_height()
        current_pos = pygame.mouse.get_pos()
        if (self.x < current_pos[0] < self.x + width) & (self.y < current_pos[1] < self.y + height):
            window.blit(self.active_button, (self.x, self.y))  
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    return self.callback()
        else:
            window.blit(self.image, (self.x, self.y))
           

class RollButton(Button):
    def __init__(self, x, y, text):
        super().__init__(x, y)
        self.active_button = pygame.image.load('Images/RollButton.png').convert_alpha()
        self.image = pygame.image.load('Images/RollButton2.png').convert_alpha()
        self.text = pygame.font.Font('Fonts/IrishGrover.ttf', 25).render(str(text), 1, ('black'))
        self.draw()
    
    def callback(self):
        pass
    

class MenuButton(Button):
    def __init__(self, x, y, text):
        super().__init__(x, y)
        self.active_button = pygame.image.load('Images/PlayEffect.png').convert_alpha()
        self.image = pygame.image.load('Images/PlayButton.png').convert_alpha()
        self.text = pygame.font.Font('Fonts/IrishGrover.ttf', 60).render(str(text), 1, ('black'))
        self.draw()
    
    def callback(self):
        pass

class ChooseButton(Button):
    def __init__(self, x, y):
        super().__init__(x, y)
        pass

class SoundButton(Button):
    def __init__(self, x, y):
        super().__init__(x, y)
        pass


class Player(PlayingField):
    __money = 10
    bob_cards = []
    event_list = []
    
    player_images = {
        1:pygame.image.load('Images/GreenPlayer.png'),
        2:pygame.image.load('Images/YellowPlayer.png'),
        3:pygame.image.load('Images/BluePlayer.png'),
        4:pygame.image.load('Images/RedPlayer.png')

    }
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.draw()

    def roll_cube(self):
        pass

    def move():
        pass

    def get_money(self):
        return self.__money
    
    def set_money(self, money):
        self.__money = money




# class GreenPlayer(Player):
#     def __init__(self, x, y):
#         super().__init__(x, y)
#         self.image = pygame.image.load('Images/GreenPlayer.png').convert_alpha()
#         self.draw()

# class YellowPlayer(Player):
#     def __init__(self, x, y):
#         super().__init__(x, y)
#         self.image = pygame.image.load('Images/YellowPlayer.png').convert_alpha()
#         self.draw()

# class BluePlayer(Player):
#     def __init__(self, x, y):
#         super().__init__(x, y)
#         self.image = pygame.image.load('Images/BluePlayer.png').convert_alpha()
#         self.draw()

# class RedPlayer(Player):
#     def __init__(self, x, y):
#         super().__init__(x, y)
#         self.image = pygame.image.load('Images/RedPlayer.png').convert_alpha()
#         self.draw()





class Cube(PlayingField):
    cube_images = {
        1:pygame.image.load('Images/Cube1.png'),
        2:pygame.image.load('Images/Cube2.png'),
        3:pygame.image.load('Images/Cube3.png'),
        4:pygame.image.load('Images/Cube4.png'),
        5:pygame.image.load('Images/Cube5.png'),
        6:pygame.image.load('Images/Cube6.png')

    }
    
    def __init__(self, x, y):
        self.x = x 
        self.y = y
        

    def roll(self):
        number = randint(1,6)
        self.image = Cube.cube_images[number]
        self.draw()


class Card(PlayingField):
    pass





class Cell(PlayingField):     
    def __init__(self, x , y):
        self.x = x
        self.y = y 
        
    
    def get_pos(self, array, index):
        return (array[index].x, array[index].y)
     


class GreenCell(Cell):
    def __init__(self, x ,y):
        super().__init__(x, y)
        self.image = pygame.image.load('Images/green_cell.png').convert_alpha()
        self.draw()


class RedCell(Cell):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pygame.image.load('Images/red_cell.png').convert_alpha()
        self.draw()




#Initializing#Initializing#Initializing
#Initializing#Initializing#Initializing
#Initializing#Initializing#Initializing


#Main window init       !!!<<<---#Реализовать отображение на виртуальную поверхность, для того чтобы была возможность делать RESIZE--->>>!!!
window = pygame.display.set_mode((width, height))#, pygame.FULLSCREEN)       #Создание окна
pygame.display.set_caption('Pirates adventures')                           #Название окна        
#pygame.display.set_icon(pygame.image.load('Images/export_png.png'))        #Установка иконки
#pygame.mouse.set_cursor                                                    #Установка курсора                                   



#Draw background
background = pygame.image.load('Images/background.png')    #Will changed
window.blit(background,(0,0))




clock = pygame.time.Clock()


objects = []
cells_array = []
green_cell = GreenCell(100, 100)

cube1 = Cube(850, 490)
button = RollButton(500,500,'Textfff')




objects.append(button)


#MainLoop#MainLoop#MainLoop
#MainLoop#MainLoop#MainLoop
#MainLoop#MainLoop#MainLoop


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
        for obj in objects:
            obj.button_state_checker()
        
        
    pygame.display.update()
    clock.tick(FPS)
