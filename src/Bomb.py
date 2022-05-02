## @file Bomb.py
#  @author Tingyu Shi, Jiacheng Wu, Qianlin Chen
#  @brief Contains a class to represent a the Bomb game item.
#  @date Apr 7, 2022

import pygame

## @brief A class representing Bomb game item.

class Bomb(pygame.sprite.Sprite):
    ## @brief Constructor for class Bomb.
    #  @details Create an instance of class Bomb, taking three
    #            arguments.
    #  @param x The x-coordinate of the Bomb game item.
    #  @param y The y-coordinate of the Bomb game item.
    #  @param speed The moving speed of Bomb game item.
    def __init__(self, x, y, speed):
        super().__init__()
        self.__speed = speed
        self.__itemType = 4
        self.image = pygame.image.load('Picture/Bomb.png')
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect(topleft = (x, y))

    ## @brief Update the position of Bomb game item.
    #  @param direction  This is the moving direction of Bomb game item. It can only be 1 or -1.
    def update(self, direction):
        self.rect.x += (direction * self.__speed)
    
    ## @brief Return the Item type of Bomb game item.
    #  @return Item Type of Bomb game item.
    def getItemType(self):
        return self.__itemType
    