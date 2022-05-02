## @file Heart.py
#  @author Tingyu Shi
#  @brief Contains a class to represent a the Heart game item.
#  @date Apr 7, 2022

import pygame

## @brief A class representing Heart game item.

class Heart(pygame.sprite.Sprite):

    ## @brief Constructor for class Heart.
    #  @details Create an instance of class Heart, taking three
    #            arguments.
    #  @param x The x-coordinate of the Heart game item.
    #  @param y The y-coordinate of the Heart game item.
    #  @param speed The moving speed of Heart game item.
    def __init__(self, x, y, speed):
        super().__init__()
        self.__speed = speed
        self.__itemType = 2 #In a monster matrix, each game item has an item number. For heart, it is 2.
        self.image = pygame.image.load('Picture/heart.png')
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect(topleft = (x, y))

    ## @brief Update the position of Heart game item.
    #  @param direction  This is the moving direction of Heart game item. It can only be 1 or -1.
    def update(self, direction):
        self.rect.x += (direction * self.__speed)
    
    ## @brief Return the Item type of Heart game item.
    #  @return Item Type of Heart game item.
    def getItemType(self):
        return self.__itemType
    