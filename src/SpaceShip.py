## @file SpaceShip.py
#  @author Tingyu Shi
#  @brief Contains a class to represent the Spaceship
#  @date Apr 7, 2022

import pygame
from Bullet import *
from BulletState import *

## @brief A class representing the SpaceShip.
class SpaceShip(pygame.sprite.Sprite):
    ## @brief Constructor of SpaceShip
    #  @param x x-coordinate of the spaceship
    #  @param y y-coordinate of the spaceship
    #  @param screen_size_info A tuple containgin width and height of the game window
    #  @param speed moving speeding of the spaceship
    #  @param space_ship_number The index to indicate the first spaceship or the second spaceship
    def __init__(self, x, y, screen_size_info, speed, space_ship_number):
        super().__init__()
        
        self.__screen_size_info = screen_size_info
        self.__space_ship_number = space_ship_number
        if space_ship_number == 1:
            self.image = pygame.image.load('Picture/spaceship1.png')
        else:
            self.image = pygame.image.load('Picture/spaceship2.png')
        self.rect = self.image.get_rect(midbottom = (x, y))
        self.__speed = speed
        self.__life = 5

        # bullets information
        self.__bullets_group = pygame.sprite.Group()
        self.__state = BulletState.READY
        self.__shoot_time = 0
        self.__bullet_number = 1

    ## @brief Move the spaceship according to the user input
    def move(self):
        keys = pygame.key.get_pressed()

        if self.__space_ship_number == 1:
            if keys[pygame.K_RIGHT]:
                self.rect.x += self.__speed
            if keys[pygame.K_LEFT]:
                self.rect.x -= self.__speed
        else:
            if keys[pygame.K_d]:
                self.rect.x += self.__speed
            if keys[pygame.K_a]:
                self.rect.x -= self.__speed
    
    ## @brief boundary detection of the spaceship, if a spaceship hits the edge of the screen, it can not move
    def boundaryDetection(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= self.__screen_size_info[0]:
            self.rect.right = self.__screen_size_info[0]

    ## @brief let space ship shoot the bullets
    def shoot(self):
        bullet_speed = -8  ########
        keys = pygame.key.get_pressed()
        if self.__space_ship_number == 1:
            if keys[pygame.K_SPACE] and self.__state == BulletState.READY:
                if self.__bullet_number == 1:
                    self.__bullets_group.add(Bullet(self.rect.center[0], self.rect.center[1], (800, 600), bullet_speed, 1))  
                    self.__state = BulletState.FIRE
                    self.__shoot_time = pygame.time.get_ticks()
                if self.__bullet_number == 2:
                    self.__bullets_group.add(Bullet(self.rect.center[0] - 25, self.rect.center[1], (800, 600), bullet_speed, 1))  
                    self.__bullets_group.add(Bullet(self.rect.center[0] + 25, self.rect.center[1], (800, 600), bullet_speed, 1))  
                    self.__state = BulletState.FIRE
                    self.__shoot_time = pygame.time.get_ticks()
                if self.__bullet_number == 3:
                    self.__bullets_group.add(Bullet(self.rect.center[0] - 25, self.rect.center[1], (800, 600), bullet_speed, 1))  
                    self.__bullets_group.add(Bullet(self.rect.center[0], self.rect.center[1], (800, 600), bullet_speed, 1))  
                    self.__bullets_group.add(Bullet(self.rect.center[0] + 25, self.rect.center[1], (800, 600), bullet_speed, 1))  
                    self.__state = BulletState.FIRE
                    self.__shoot_time = pygame.time.get_ticks()

        else:
            if keys[pygame.K_s] and self.__state == BulletState.READY:
                if self.__bullet_number == 1:
                    self.__bullets_group.add(Bullet(self.rect.center[0], self.rect.center[1], (800, 600), bullet_speed, 1))  
                    self.__state = BulletState.FIRE
                    self.__shoot_time = pygame.time.get_ticks()
                if self.__bullet_number == 2:
                    self.__bullets_group.add(Bullet(self.rect.center[0] - 25, self.rect.center[1], (800, 600), bullet_speed, 1))  
                    self.__bullets_group.add(Bullet(self.rect.center[0] + 25, self.rect.center[1], (800, 600), bullet_speed, 1))  
                    self.__state = BulletState.FIRE
                    self.__shoot_time = pygame.time.get_ticks()
                if self.__bullet_number == 3:
                    self.__bullets_group.add(Bullet(self.rect.center[0] - 25, self.rect.center[1], (800, 600), bullet_speed, 1))  
                    self.__bullets_group.add(Bullet(self.rect.center[0], self.rect.center[1], (800, 600), bullet_speed, 1))  
                    self.__bullets_group.add(Bullet(self.rect.center[0] + 25, self.rect.center[1], (800, 600), bullet_speed, 1))  
                    self.__state = BulletState.FIRE
                    self.__shoot_time = pygame.time.get_ticks()


    ## @brief This method is responsible for handling the gap time between two bullets
    def prepare_bullet(self):
        delay_time = 500  ##########
        if self.__state == BulletState.FIRE:
            if pygame.time.get_ticks() - self.__shoot_time >= delay_time:   ###
                self.__state = BulletState.READY

    ## @brief get spirte group of bullets from the spaceship
    #  @return spirte group of bullets from the spaceship
    def getBulletsGroup(self):
        return self.__bullets_group

    ## @brief update the status of space ship
    #  @detail Including position, move, shot and boundary detection
    def update(self):
        self.move()
        self.boundaryDetection()
        self.shoot()
        self.prepare_bullet()
        self.__bullets_group.update()

    ## @brief decrease one life for the spaceship
    def reduceLife(self):
        self.__life -= 1
    
    ## @brief increase one life for the spaceship. The maximum is 5.
    def increaseLife(self):
        self.__life += 1
        if self.__life >= 5:
            self.__life = 5

    ## @brief get the current life of the space ship
    #  @return current life of the spaceship
    def getLife(self):
        return self.__life
    
    ## @brief set the space ship life to a certain number
    def setLife(self, num):
        self.__life = num
    
    ## @brief increase the number of bullets for the space ship
    def increaseBullet(self):
        self.__bullet_number += 1
        if self.__bullet_number >= 3:
            self.__bullet_number = 3
