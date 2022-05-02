## @file Ammo.py
#  @author Tingyu Shi
#  @brief Contains a class to represent a the Ammo game item.
#  @date Apr 7, 2022

import pygame

## @brief A class representing Ammo game item.

class Ammo(pygame.sprite.Sprite):
    ## @brief Constructor for class Ammo.
    #  @details Create an instance of class Ammo, taking three
    #            arguments.
    #  @param x The x-coordinate of the Ammo game item.
    #  @param y The y-coordinate of the Ammo game item.
    #  @param speed The moving speed of Ammo game item.
    def __init__(self, x, y, speed):
        super().__init__()
        self.__speed = speed
        self.__itemType = 3   #In a monster matrix, each item will have an item type number, for Ammo game item, it is 3
        self.image = pygame.image.load('Picture/ammo.png')
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect(topleft = (x, y))

    ## @brief Update the position of Ammo game item.
    #  @param direction  This is the moving direction of Ammo game item. It can only be 1 or -1.
    def update(self, direction):
        self.rect.x += (direction * self.__speed)
    
    ## @brief Return the Item type of Ammo game item.
    #  @return Item Type of Ammo game item.
    def getItemType(self):
        return self.__itemType
    