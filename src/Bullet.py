## @file Bullet.py
#  @author Tingyu Shi
#  @brief Contains a class to represent a the Bullet.
#  @date Apr 7, 2022

import pygame

## @brief A class to represent Bullet class

class Bullet(pygame.sprite.Sprite):
    
    ## @brief Constructor for class Bullet.
    #  @details Create an instance of class Bullet, taking five
    #            arguments.
    #  @param x The x-coordinate of the bullet.
    #  @param y The y-coordinate of the bullet.
    #  @param screen_size_info A tuple to represent the screen size
    #  @param speed The moving speed of bullet. Positive to negative depending the direction of bullet.
    #  @param Moving direction of the bullet, this is used to decide which picture to use.

    def __init__ (self, x, y, screen_size_info, speed, direction):
        super().__init__()
        self.__screen_size_info = screen_size_info
        self.__speed = speed
        if direction == 1:
            self.image = pygame.image.load('Picture/bullet.png')
            self.image = pygame.transform.scale(self.image, (20, 20))
        else:
            self.image = pygame.image.load('Picture/bullet_down.png')
            self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect(center = (x, y))
    
    ## @brief Boundary Dectection of the bullet object.
    #  @details If a bullet flies out of the screen, the object should kill itself.
    def boundaryDetection(self):
        if self.rect.y <= -30 or self.rect.y >= self.__screen_size_info[1]:
            self.kill()
    
    ## @brief Move the position of the bullet object
    #  @details Let the bullet object move on the screen
    def move(self):
        self.rect.y += self.__speed
    
    ## @brief update the position of the bullet
    #  @details This method brings move and boundaryDetection together.
    def update(self):
        self.move()
        self.boundaryDetection()