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
        background.blit(self.image, (self.x, self.y)) 



class Button(PlayingField):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
        
    def draw_normal(self):   #method override(specific for button)
        self.image.blit(self.text, (self.image.get_rect().center[0] - self.text.get_width() // 2, self.image.get_rect().center[1] - self.text.get_height() // 2)) 
        background.blit(self.image, (self.x, self.y))

    
    def draw_active(self):
        self.active_button.blit(self.text, (self.image.get_rect().center[0] - self.text.get_width() // 2, self.image.get_rect().center[1] - self.text.get_height() // 2)) 
        background.blit(self.active_button, (self.x, self.y))
    

    def button_state_checker(self):
        width = self.image.get_width()
        height = self.image.get_height()
        current_pos = pygame.mouse.get_pos()
        if (self.x < current_pos[0] < self.x + width) & (self.y < current_pos[1] < self.y + height):
            #background.blit(self.active_button, (self.x, self.y))  
            self.draw_active()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    return self.callback()
        else:
            #background.blit(self.image, (self.x, self.y))
            self.draw_normal()

class RollButton(Button):
    def __init__(self, x, y, text):
        super().__init__(x, y)
        self.active_button = pygame.image.load('Images/RollButton.png').convert_alpha()
        self.image = pygame.image.load('Images/RollButton2.png').convert_alpha()
        self.text = pygame.font.Font('Fonts/IrishGrover.ttf', 25).render(str(text), 1, ('black'))
        
    
    def callback(self):
        Player.roll_cube(player1)
        
    

class MenuButton(Button):
    def __init__(self, x, y, image, active_button):
        super().__init__(x, y)
        self.active_button = pygame.image.load(str(active_button)).convert_alpha()
        self.image = pygame.image.load(str(image)).convert_alpha()
        
    def draw_normal(self):
        menu.blit(self.image, (self.x, self.y))

    def draw_active(self):
        menu.blit(self.active_button, (self.x, self.y))

class PlayButton(MenuButton):
    def __init__(self, x, y, image, active_button):
        super().__init__(x, y, image, active_button)
    
    def callback(self):                  #call enter ip adress window
        pass                   

class SettingsButton(MenuButton):
    def __init__(self, x, y):
        super().__init__(x, y)
    
    def callback():                 #call settings window
        pass




class QuitButton(MenuButton):
    def __init__(self, x, y, image, active_button):
        super().__init__(x, y, image, active_button)
        
    def callback(self):
        pygame.quit()              #call quit funcs
        exit()

class SoundButton(MenuButton):
    def __init__(self, x, y, image, active_button):    
        super().__init__(x, y, image, active_button)


    def callback(self):               #call sound switcher
        global sound_flag

        if sound_flag:
            pygame.mixer.music.pause()
            self.image = pygame.image.load('Images/soundOFF.png').convert_alpha()
            sound_flag = False
            return sound_flag

        else:
            pygame.mixer.music.unpause()
            self.image = pygame.image.load('Images/soundON.png').convert_alpha()
            sound_flag = True
            return sound_flag


class ChooseButton(Button):
    def __init__(self, x, y):
        super().__init__(x, y)
        pass




class Player(PlayingField):
    __money = 10
    bob_cards = []
    event_list = []
    image = pygame.Surface((0,0))

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
        Cube.roll(cube1)

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
window = pygame.display.set_mode((width, height))# pygame.FULLSCREEN)       #Создание окна
pygame.display.set_caption('Pirates adventures')                           #Название окна        
#pygame.display.set_icon(pygame.image.load('Images/export_png.png'))        #Установка иконки
#pygame.mouse.set_cursor                                                    #Установка курсора                                   



#Draw background & menu
background = pygame.image.load('Images/background.png').convert_alpha()    #Will changed
menu = pygame.image.load('Images/menu.png').convert_alpha()
pygame.mixer.music.load('Sounds/Background.mp3')
pygame.mixer.music.play(-1)





clock = pygame.time.Clock()


buttons = []
cells_array = []
players = []

green_cell = GreenCell(100, 100)
cells_array.append(green_cell)

player1 = Player(250, 250)
players.append(player1)
player2 = Player(300, 300)
players.append(player2)
player3 = Player(350, 350)
players.append(player3)
player4 = Player(400, 400)
players.append(player4)


menubutton = PlayButton(95, 117, 'Images/Play.png', 'Images/PlayEffect.png')
menubutton2 = QuitButton(95, 554, 'Images/Quit.png', 'Images/QuitEffect.png')
menubutton4 = SoundButton(900, 900, 'Images/soundON.png', 'Images/soundOFF.png')


cube1 = Cube(0, 0)
cube2 = Cube(100, 0)
button = RollButton(980,547,'Roll')
buttons.append(button)
buttons.append(menubutton)
buttons.append(menubutton2)
buttons.append(menubutton4)


def player_images_setter(players):
    counter = 1
    for player in players:
            player.image = Player.player_images[counter]
            player.draw()
            counter += 1

player_images_setter(players) 



#MainLoop#MainLoop#MainLoop
#MainLoop#MainLoop#MainLoop
#MainLoop#MainLoop#MainLoop

#background.blit(menu,(0,0))
#window.blit(background,(0,0))


#flags
menu_flag = True
sound_flag = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            menu_flag = not menu_flag
        
        for button in buttons:
            button.button_state_checker()
    

    for player in players:
        player.draw()
        

    for cell in cells_array:
        cell.draw()
 
    
    if menu_flag:    
        window.blit(menu,(0,0))
    else:
        window.blit(background,(0,0))
    
    pygame.display.update()
    clock.tick(FPS)
