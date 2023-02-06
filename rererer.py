import pygame

player_images = ['pl1', 'pl2', 'pl3', 'pl4']

def turn():
    player_images.append(player_images.pop(0))



turn()
turn()
turn()

print(player_images)