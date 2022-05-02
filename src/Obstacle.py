## @file Obstacle.py
#  @author Tingyu Shi, Jiacheng Wu, Qianlin Chen
#  @brief Contains two classes needed to create obstacles.
#  @date Apr 7, 2022

import pygame

## @brief A class representing blocks in the obstacle
class Block(pygame.sprite.Sprite):
    ## @brief Constructor of class block
    #  @param x x-coordinate of a block
    #  @param y y-coordinate of a block
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((5, 5))
        self.image.fill((247, 59, 23))
        self.rect = self.image.get_rect(topleft = (x, y))

## @brief A class to create four obstacles of the game
class Obstacles(pygame.sprite.Sprite):
    ## @brief The constructor of Obstacles of class
    def __init__(self):
        super().__init__()
        self.__blocks_group = pygame.sprite.Group()
        self.create_one_obstacle(50, 400)
        self.create_one_obstacle(250, 400)
        self.create_one_obstacle(450, 400)
        self.create_one_obstacle(650, 400)

    ## @brief A method to create one obstacle
    #  @param x_start starting x-coordinate of the obstacle
    #  @param y_start starting y_coordinate of the obstacle
    def create_one_obstacle(self, x_start, y_start):
        for row in range(10):
            for col in range(17):
                x = x_start + col * 5
                y = y_start + row * 5
                block = Block(x , y)
                self.__blocks_group.add(block)
    
    ## @brief get sprite blocks group 
    #  @return sprite blocks group 
    def getBlocksGroup(self):
        return self.__blocks_group