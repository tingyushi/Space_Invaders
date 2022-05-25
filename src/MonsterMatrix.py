## @file MonsterMatrix.py
#  @author Tingyu Shi
#  @brief Contains a class to represent a the MonsterMatrix.
#  @date Apr 7, 2022

import pygame
from Monster import *
from MonsterColor import *
from Bullet import *
from random import choice
from random import randint
from Heart import *
from Ammo import *
from Bomb import *

## @brief A class representing MonsterMatrix
class MonsterMatrix(pygame.sprite.Sprite):
    ## @brief The constructor of MonsterMatrix class
    #  @param round Indicating the round number of game
    #  @param speed moving speed of monster matrix
    #  @param screen_size_info A tuple containing the width and height of game window
    def __init__(self, round, speed, screen_size_info):
        super().__init__()
        self.__monsters_group = pygame.sprite.Group()
        self.__speed = speed
        self.__direction = 1
        self.__screen_size_info = screen_size_info
        self.__bullets_group = pygame.sprite.Group()

        if round == 1:
            self.round1()
        if round == 2:
            self.round2()
        if round == 3:
            self.round3()
        if round == 4:
            self.round4()
        if round == 5:
            self.round5()

    ## @brief round1 of the game
    def round1(self):
        itme_type = randint(2, 4)
        ran_row = randint(0, 4)
        ran_col = randint(0, 9)
        for row in range(5):
            for col in range(10):
                x = col * 50
                y = 50 + row * 30
                if row == ran_row and col == ran_col:
                    if itme_type == 2:
                        monster = Heart(x, y, self.__speed)
                    if itme_type == 3:
                        monster = Ammo(x, y, self.__speed)
                    if itme_type == 4:
                        monster = Bomb(x, y, self.__speed)
                else:    
                    monster = Monster(x, y, MonsterColor.GREEN, self.__speed)        
                self.__monsters_group.add(monster)

    ## @brief round2 of the game
    def round2(self):
        itme_type = randint(2, 4)
        ran_row = randint(0, 4)
        ran_col = randint(0, 9)
        for row in range(5):
            for col in range(10):
                x = col * 50
                y = 50 + row * 30
                if row == ran_row and col == ran_col and itme_type == 2:
                    monster = Heart(x, y, self.__speed)
                elif row == ran_row and col == ran_col and itme_type == 3:
                    monster = Ammo(x, y, self.__speed)
                elif row == ran_row and col == ran_col and itme_type == 4:
                    monster = Bomb(x, y, self.__speed)
                elif row == 0 or row == 1:
                    color = MonsterColor.BLUE
                    monster = Monster(x, y, color, self.__speed)
                else:
                    color = MonsterColor.GREEN
                    monster = Monster(x, y, color, self.__speed)
                self.__monsters_group.add(monster)

    ## @brief round3 of the game
    def round3(self):
        itme_type = randint(2, 4)
        ran_row = randint(0, 4)
        ran_col = randint(0, 9)
        for row in range(5):
            for col in range(10):
                x = col * 50
                y = 50 + row * 30
                if row == ran_row and col == ran_col:
                    if itme_type == 2:
                        monster = Heart(x, y, self.__speed)
                    if itme_type == 3:
                        monster = Ammo(x, y, self.__speed)
                    if itme_type == 4:
                        monster = Bomb(x, y, self.__speed)
                else:
                    monster = Monster(x, y, MonsterColor.BLUE, self.__speed)
                self.__monsters_group.add(monster)

    ## @brief round4 of the game
    def round4(self):
        itme_type = randint(2, 4)
        ran_row = randint(0, 4)
        ran_col = randint(0, 9)
        for row in range(5):
            for col in range(10):
                x = col * 50
                y = 50 + row * 30
                if row == ran_row and col == ran_col and itme_type == 2:
                    monster = Heart(x, y, self.__speed)
                elif row == ran_row and col == ran_col and itme_type == 3:
                    monster = Ammo(x, y, self.__speed)
                elif row == ran_row and col == ran_col and itme_type == 4:
                    monster = Bomb(x, y, self.__speed)
                elif row == 4:
                    color = MonsterColor.GREEN
                    monster = Monster(x, y, color, self.__speed)
                elif row == 3 or row == 2 or row == 1:
                    color = MonsterColor.BLUE
                    monster = Monster(x, y, color, self.__speed)
                else:
                    color = MonsterColor.PINK
                    monster = Monster(x, y, color, self.__speed)
                self.__monsters_group.add(monster)

    ## @brief round5 of the game
    def round5(self):
        itme_type = randint(2, 4)
        ran_row = randint(0, 4)
        ran_col = randint(0, 9)
        for row in range(5):
            for col in range(10):
                x = col * 50
                y = 50 + row * 30
                if row == ran_row and col == ran_col:
                    if itme_type == 2:
                        monster = Heart(x, y, self.__speed)
                    if itme_type == 3:
                        monster = Ammo(x, y, self.__speed)
                    if itme_type == 4:
                        monster = Bomb(x, y, self.__speed)
                else:
                    monster = Monster(x, y, MonsterColor.PINK, self.__speed)
                self.__monsters_group.add(monster)

    ## @brief get the sprite monsters group
    #  @return Sprite monsters group
    def getMonstersGroup(self):
        return self.__monsters_group

    ## @brief boundaryDetection for the MonsterMatrix
    #  @detail If any of the monster hits the edge of the screen, the matrix should move down
    def boundaryDetection(self):
        allMonsters = self.__monsters_group.sprites()
        for ele in allMonsters:
            if ele.rect.right >= self.__screen_size_info[0]:
                self.__direction = -1
                self.move_down()
            if ele.rect.left <= 0:
                self.__direction = 1
                self.move_down()

    ## @brief let monster matrix moves down
    def move_down(self):
        if self.__monsters_group:
            for ele in self.__monsters_group.sprites():
                ele.rect.y += 2

    ## @brief let monster matrix shoots bullets
    def shoot(self):
        temp_list = []
        if self.__monsters_group.sprites():
            for monster in self.__monsters_group.sprites():
                if monster.getItemType() == 1:
                    temp_list.append(monster)
            if (len(temp_list) != 0):
                random_monster = choice(temp_list)
                self.__bullets_group.add(Bullet(random_monster.rect.center[0], random_monster.rect.center[1], (800, 600), 4, 2))

    ## @brief get the sprite group containing all the bullets shoot from the monster matrix
    #  @return sprite group containing all the bullets shoot from the monster matrix
    def getBulletsGroup(self):
        return self.__bullets_group

    ## @brief update the position of monsters and the bullets from the monster matrix
    def update(self):
        for ele in self.__monsters_group.sprites():
            ele.update(self.__direction)
        self.boundaryDetection()
        self.__bullets_group.update()