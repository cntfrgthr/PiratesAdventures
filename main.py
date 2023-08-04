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

    def print_text(self, x, y, input, surface, size, color=('black')):
        self.text = pygame.font.Font('Fonts/IrishGrover.ttf', size)
        surface.blit(self.text.render(str(input), 1, color), (x, y))

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
            self.draw_active()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    return self.callback()
        else:
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
        global press_sound
        press_sound = pygame.mixer.Sound('Sounds/MenuButtonClick.mp3')

    def draw_normal(self):
        menu.blit(self.image, (self.x, self.y))

    def draw_active(self):
        menu.blit(self.active_button, (self.x, self.y))
    


class PlayButton(MenuButton):
    def __init__(self, x, y, image, active_button):
        super().__init__(x, y, image, active_button)
    

    def callback(self):                  #call enter ip adress window
        global enter_ip_flag, settings_window_flag
        if sound_flag:
            press_sound.play()
        if not enter_ip_flag:  
            settings_window_flag = False
            enter_ip = pygame.image.load('Images/EnterIP.png').convert_alpha()
            menu.blit(enter_ip, (menu.get_rect().center[0] - enter_ip.get_width() // 2, menu.get_rect().center[1] - enter_ip.get_height()))
            enter_ip_flag = True         
            return enter_ip_flag
        else:
            settings_window_flag = False
            enter_ip = pygame.image.load('Images/menu.png').convert_alpha()
            menu.blit(enter_ip, (menu.get_rect().center[0] - enter_ip.get_width() // 2, menu.get_rect().center[1] - enter_ip.get_height() // 2))
            enter_ip_flag = False
            return enter_ip_flag
    
    def return_ip_addr(self):
        global enter_ip_flag, input_text
        
        if enter_ip_flag:                                                                                                             
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        enter_ip_flag = False                                     #Try to connect after Enter pressing in {try:   except:}
                        return input_text
                    elif event.key == pygame.K_BACKSPACE:
                        input_text = input_text[:-1]
                        menu.blit(enter_ip, (menu.get_rect().centerx - enter_ip.get_width() // 2, menu.get_rect().centery - enter_ip.get_height()))
                    else:
                        if len(input_text) <= 14:
                            input_text += event.unicode

                self.print_text(795, 295, input_text, menu, 50)         







class SettingsButton(MenuButton):
    def __init__(self, x, y, image, active_button):
        super().__init__(x, y, image, active_button)

    def callback(self):                 #call settings window
        global settings_window_flag, enter_ip_flag, menu
        if sound_flag:
            press_sound.play()
        if not settings_window_flag:  
            enter_ip_flag = False
            settings_window = pygame.image.load('Images/SettingsMenu.png').convert_alpha()
            menu.blit(settings_window, (menu.get_rect().center[0] - settings_window.get_width() // 2, menu.get_rect().center[1] - settings_window.get_height()))
            settings_window_flag = True
            return settings_window_flag
        else:
            enter_ip_flag = False
            settings_window = pygame.image.load('Images/menu.png').convert_alpha()
            menu.blit(settings_window, (menu.get_rect().center[0] - settings_window.get_width() // 2, menu.get_rect().center[1] - settings_window.get_height() // 2))
            settings_window_flag = False
            return settings_window_flag

    #global buttons, fullscreen_toggle, fps60, fps144, fps240, volume_minus, volume_plus, save_button
class FullscreenToggle(MenuButton):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load('Images/FullscreenOFF.png')
        self.active_button = pygame.image.load('Images/FullscreenOFF.png')
        
    def callback(self):
        global fullscreen_flag, window

        if not fullscreen_flag:
            self.image = pygame.image.load('Images/FullscreenON.png')
            self.active_button = pygame.image.load('Images/FullscreenON.png')
            window = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
            fullscreen_flag = True
            return fullscreen_flag
        else:
            self.image = pygame.image.load('Images/FullscreenOFF.png')
            self.active_button = pygame.image.load('Images/FullscreenOFF.png')
            window = pygame.display.set_mode((width, height))
            fullscreen_flag = False
            return fullscreen_flag

class FPS60(MenuButton):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load('Images/60fps.png')
        self.active_button = pygame.image.load('Images/60fps.png')
        

    def callback(self):
        global FPS
        FPS = 60
        menu.blit(fps_fone, (995, 312))
        self.print_text(1005, 310, FPS, menu, 28)

class FPS144(MenuButton):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load('Images/144fps.png')
        self.active_button = pygame.image.load('Images/144fps.png')
       
    def callback(self):
        global FPS
        FPS = 144
        menu.blit(fps_fone, (995, 312))
        self.print_text(1002, 310, FPS, menu, 28)

class FPS240(MenuButton):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load('Images/240fps.png')
        self.active_button = pygame.image.load('Images/240fps.png')
       
    def callback(self):
        global FPS
        FPS = 240
        menu.blit(fps_fone, (995, 312))
        self.print_text(999, 310, FPS, menu, 28)

class VolumePlus(MenuButton):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load('Images/VolumePlus.png')
        self.active_button = pygame.image.load('Images/VolumePlusEffect.png')

    def callback(self):
        global sound_volume

        if sound_volume < 1:
            sound_volume = float('%.1f' % (sound_volume + 0.1))
            pygame.mixer.music.set_volume(sound_volume)
            press_sound.set_volume(sound_volume)                                      #Sound volumes
            menu.blit(fps_fone, (997, 387))
            self.print_text(998, 392, f'{sound_volume * 100}%', menu, 18)

class VolumeMinus(MenuButton):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load('Images/VolumeMinus.png')
        self.active_button = pygame.image.load('Images/VolumeMinusEffect.png')

    def callback(self):
        global sound_volume

        if sound_volume > 0:
            sound_volume = float('%.1f' % (sound_volume - 0.1))
            pygame.mixer.music.set_volume(sound_volume)                              #Sound volumes
            press_sound.set_volume(sound_volume)
            menu.blit(fps_fone, (997, 387))
            self.print_text(998, 392, f'{sound_volume * 100}%', menu, 18)


class SaveButton(MenuButton):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load('Images/SaveButton.png')
        self.active_button = pygame.image.load('Images/SaveButtonEffect.png')

    def callback(self):
        global fullscreen_flag, FPS, sound_volume, settings_window, settings_window_flag                     
        file = open('settings.py', 'w')
        file.write(f'width = 1920\nheight = 1080\nFPS = {FPS}\nsound_volume = {sound_volume}\nfullscreen_flag = {fullscreen_flag}')
        file.close()
        settings_window_flag = False
        settings_window = pygame.image.load('Images/menu.png').convert_alpha()
        menu.blit(settings_window, (menu.get_rect().center[0] - settings_window.get_width() // 2, menu.get_rect().center[1] - settings_window.get_height() // 2))
        return settings_window_flag

class QuitButton(MenuButton):
    def __init__(self, x, y, image, active_button):
        super().__init__(x, y, image, active_button)
        
    def callback(self):
        if sound_flag:
            press_sound.play()
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
if not fullscreen_flag:
    window = pygame.display.set_mode((width, height))                       #Создание окна
else:
    window = pygame.display.set_mode((width, height), pygame.FULLSCREEN) 

pygame.display.set_caption('Pirates adventures')                            #Название окна        
#pygame.display.set_icon(pygame.image.load('Images/export_png.png'))        #Установка иконки
#pygame.mouse.set_cursor                                                    #Установка курсора                                   



#Draw background & menu
background = pygame.image.load('Images/background.png').convert_alpha()    #Will changed
menu = pygame.image.load('Images/menu.png').convert_alpha()
pygame.mixer.music.load('Sounds/Background.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(sound_volume)




#IP address enter window init
enter_ip = pygame.image.load('Images/EnterIP.png').convert_alpha()
#Settings window init
settings_window = pygame.image.load('Images/SettingsMenu.png').convert_alpha()
fullscreen_toggle = FullscreenToggle(900,245)
fps60 = FPS60(774, 304)
fps144 = FPS144(842, 304)
fps240 = FPS240(913, 304)
fps_fone = pygame.image.load('Images/FpsFone.png').convert_alpha()
volume_plus = VolumePlus(844, 381)
volume_minus = VolumeMinus(915, 381)
save_button = SaveButton(915, 465)



clock = pygame.time.Clock()

settings_buttons = []
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


PlayButton1 = PlayButton(95, 65, 'Images/Play.png', 'Images/PlayEffect.png')
SettingsButton1 = SettingsButton(95, 331, 'Images/Settings.png', 'Images/SettingsEffect.png')
menubutton2 = QuitButton(95, 597, 'Images/Quit.png', 'Images/QuitEffect.png')
menubutton4 = SoundButton(1740, 890, 'Images/soundON.png', 'Images/soundOFF.png')



cube1 = Cube(0, 0)
cube2 = Cube(100, 0)
button = RollButton(980,547,'Roll')
buttons.append(button)
buttons.append(PlayButton1)
buttons.append(menubutton2)
buttons.append(menubutton4)
buttons.append(SettingsButton1)
settings_buttons.append(fullscreen_toggle)
settings_buttons.append(fps60)
settings_buttons.append(fps144)
settings_buttons.append(fps240)
settings_buttons.append(volume_plus)
settings_buttons.append(volume_minus)
settings_buttons.append(save_button)


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


#flags and globals
menu_flag = True
if sound_volume == 0.0:
    sound_flag = False
else:
    sound_flag = True
enter_ip_flag = False
settings_window_flag = False
input_text = ''

while True:
    for event in pygame.event.get():                                         #For any control events
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:    #Esc menu switcher
            menu_flag = not menu_flag
        
        for button in buttons:                                               #Button state checker
            button.button_state_checker()                                    
    
        PlayButton1.return_ip_addr()                                          #Обязательно обрабатывать через try: except:, при возникновении ошибки в except выводить текст
        
        if settings_window_flag:
            for button in settings_buttons:                                   #"неправильный ip адрес, попробуйте снова" и занулять input_text = ''
                button.button_state_checker()
                
                                                                             #For everything else
    for player in players:                                                   #Update for players
        player.draw()
        

    for cell in cells_array:                                                 #Update for cells
        cell.draw()
    
   
    if menu_flag:     
        window.blit(menu,(0,0))
    else:
        window.blit(background,(0,0))
            
    
    pygame.display.update()
    clock.tick(FPS)
