## @file Monster.py
#  @author Tingyu Shi, Jiacheng Wu, Qianlin Chen
#  @brief Contains a class to represent a the Monster.
#  @date Apr 7, 2022

import pygame
from MonsterColor import *

## @brief A class representing monster
class Monster(pygame.sprite.Sprite):
    ## @brief The constructor of Monster class
    #  @param x x-coordinate of monster
    #  @param y y-coordinate of monster
    #  @param color monster color
    #  @param moving speed of monster
    def __init__(self, x, y, color, speed):
        super().__init__()
        if (color == MonsterColor.GREEN):
            filepath = 'Picture/green_monster.png'
            self.__life = 1
        if (color == MonsterColor.BLUE):
            filepath = 'Picture/blue_monster.png'
            self.__life = 2
        if (color == MonsterColor.PINK):
            filepath = 'Picture/pink_monster.png'
            self.__life = 3

        self.__speed = speed
        self.__itemType = 1
        self.image = pygame.image.load(filepath)
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect(topleft = (x, y))

    ## @brief reduce one life of the monsters
    def reduceLife(self):
        self.__life -= 1
    
    ## @brief tell if a monster has died
    #  @return boolean True--> monster died    False-->monster sill alive
    def isDead(self):
        return self.__life == 0

    ## @brief update the position of monster
    #  @param direction indicating the moving direction of monster. This variable can only be 0 or 1
    def update(self, direction):
        self.rect.x += (direction * self.__speed)
    
    ## @brief get the item type of monster
    #  @return item type of monster object
    def getItemType(self):
        return self.__itemType
    
        