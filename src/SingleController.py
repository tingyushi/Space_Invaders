## @file SingleController.py
#  @author Tingyu Shi
#  @brief Contains a class to represent the controller of the single player mode.
#  @date Apr 7, 2022

import pygame
import sys
from Display import *
from SpaceShip import *
from Obstacle import *
from MonsterMatrix import *
from Score import *
import random

## @brief A class representing the single player mode controller
class SingleController:
    ## @brief Constructor of the single player mode
    #  @param window  game window object
    #  @param screen  screen object
    def __init__(self, window, screen):
        self.window = window 
        self.screen = screen 

        #space ship variables
        self.space_ship_model = SpaceShip(400, 600, (800, 600), 3, 1)
        self.space_ship_group = pygame.sprite.GroupSingle(self.space_ship_model)
        self.space_ship_display = SpaceShipDisplay(self.screen, self.space_ship_group)
        self.space_ship_bullets_display = BulletDisplay(self.screen, self.space_ship_model.getBulletsGroup())

        #obstacles variables
        self.obstacles = Obstacles()
        self.obstacles_display = ObstaclesDisplay(self.screen, self.obstacles.getBlocksGroup())

        #monster matrix
        self.monster_matrix_model = MonsterMatrix(1, 1, (800, 600))
        self.monster_matrix_display = MonsterMatrixDisplay(self.screen, self.monster_matrix_model.getMonstersGroup())
        self.monster_matrix_bullets_display = BulletDisplay(self.screen, self.monster_matrix_model.getBulletsGroup())

        #socre and life
        self.score = Score()
        self.score_display = ScoreDisplay(self.screen)
        self.life_display = LifeDisplay(self.screen)

        #win or lose
        self.win = False

    ## @brief Run the game
    #  @detail Including handling user inputs, collision detection, updating models and display models
    def run(self):
        monster_shooting = pygame.USEREVENT + 1
        pygame.time.set_timer(monster_shooting, 800)
        round_number = 2
        running = True
        clock = pygame.time.Clock()

        while running:
            #set up background
            self.window.setBackground()

            #user input handling
            for event in pygame.event.get():
                #quit game
                if event.type == pygame.QUIT:  
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                if event.type == monster_shooting:
                    self.monster_matrix_model.shoot()


            ###############################################################collision detection####################################################
            # bullets from spaceship
            if self.space_ship_model.getBulletsGroup():
                for bullet in self.space_ship_model.getBulletsGroup().sprites():
                    #with obstacle
                    if pygame.sprite.spritecollide(bullet, self.obstacles.getBlocksGroup(), True):
                        bullet.kill()
                    #with monster
                    monster_shot = pygame.sprite.spritecollide(bullet, self.monster_matrix_model.getMonstersGroup(), False)
                    for monster in monster_shot:
                        #shot a monster
                        if monster.getItemType() == 1:
                            self.score.increase(10)
                            bullet.kill()
                            monster.reduceLife()
                            if monster.isDead():
                                monster.kill()
                        #shot a heart
                        if monster.getItemType() == 2:
                            self.space_ship_model.increaseLife()
                            monster.kill()
                            bullet.kill()
                        #shot an ammo
                        if monster.getItemType() == 3:
                            self.space_ship_model.increaseBullet()
                            monster.kill()
                            bullet.kill()
                        #shot a bomb
                        if monster.getItemType() == 4:
                            monster.kill()
                            bullet.kill()
                            if (len(self.monster_matrix_model.getMonstersGroup().sprites()) <= 4):
                                for ele in self.monster_matrix_model.getMonstersGroup().sprites():
                                    ele.kill()
                            else:
                                for i in range(4):
                                    random_monster = random.choice(self.monster_matrix_model.getMonstersGroup().sprites())
                                    random_monster.kill()
            
            #bullets from monsters
            if self.monster_matrix_model.getBulletsGroup():
                for bullet in self.monster_matrix_model.getBulletsGroup():
                    #with obstacle
                    if pygame.sprite.spritecollide(bullet, self.obstacles.getBlocksGroup(), True):
                        bullet.kill()
                    if pygame.sprite.spritecollide(bullet, self.space_ship_group, False):
                        bullet.kill()
                        self.space_ship_model.reduceLife()
                        if self.space_ship_model.getLife() <= 0:
                            running = False
            
            #monster and obstacles
            if self.monster_matrix_model.getMonstersGroup():
                for monster in self.monster_matrix_model.getMonstersGroup().sprites():
                    pygame.sprite.spritecollide(monster, self.obstacles.getBlocksGroup(), True)
            
            #monster and spaceship
            if self.monster_matrix_model.getMonstersGroup():
                 for monster in self.monster_matrix_model.getMonstersGroup().sprites():
                    if pygame.sprite.spritecollide(monster, self.space_ship_group, True):
                        running = False

            ###############################################################round change##########################################################
            if (len(self.monster_matrix_model.getMonstersGroup().sprites()) == 0 and round_number == 2):
                #for bullet in self.space_ship_model.getBulletsGroup().sprites():
                    #bullet.kill()
                for bullet in self.monster_matrix_model.getBulletsGroup().sprites():
                    bullet.kill()
                self.monster_matrix_model = MonsterMatrix(2, 1, (800, 600))
                self.monster_matrix_display = MonsterMatrixDisplay(self.screen, self.monster_matrix_model.getMonstersGroup())
                self.monster_matrix_bullets_display = BulletDisplay(self.screen, self.monster_matrix_model.getBulletsGroup())
                round_number += 1
            
            if (len(self.monster_matrix_model.getMonstersGroup().sprites()) == 0 and round_number == 3):
                for bullet in self.space_ship_model.getBulletsGroup().sprites():
                    bullet.kill()
                for bullet in self.monster_matrix_model.getBulletsGroup().sprites():
                    bullet.kill()
                self.monster_matrix_model = MonsterMatrix(3, 1, (800, 600))
                self.monster_matrix_display = MonsterMatrixDisplay(self.screen, self.monster_matrix_model.getMonstersGroup())
                self.monster_matrix_bullets_display = BulletDisplay(self.screen, self.monster_matrix_model.getBulletsGroup())
                round_number += 1

            if (len(self.monster_matrix_model.getMonstersGroup().sprites()) == 0 and round_number == 4):
                for bullet in self.space_ship_model.getBulletsGroup().sprites():
                    bullet.kill()
                for bullet in self.monster_matrix_model.getBulletsGroup().sprites():
                    bullet.kill()
                self.monster_matrix_model = MonsterMatrix(4, 1, (800, 600))
                self.monster_matrix_display = MonsterMatrixDisplay(self.screen, self.monster_matrix_model.getMonstersGroup())
                self.monster_matrix_bullets_display = BulletDisplay(self.screen, self.monster_matrix_model.getBulletsGroup())
                round_number += 1
            
            if (len(self.monster_matrix_model.getMonstersGroup().sprites()) == 0 and round_number == 5):
                for bullet in self.space_ship_model.getBulletsGroup().sprites():
                    bullet.kill()
                for bullet in self.monster_matrix_model.getBulletsGroup().sprites():
                    bullet.kill()
                self.monster_matrix_model = MonsterMatrix(5, 1, (800, 600))
                self.monster_matrix_display = MonsterMatrixDisplay(self.screen, self.monster_matrix_model.getMonstersGroup())
                self.monster_matrix_bullets_display = BulletDisplay(self.screen, self.monster_matrix_model.getBulletsGroup())
                round_number += 1
            
            if (len(self.monster_matrix_model.getMonstersGroup().sprites()) == 0 and round_number == 6):
                running = False
                self.win = True

            ############################################################model update###########################################################
            self.space_ship_model.update()
            self.monster_matrix_model.update()
            
            #################################################################display############################################################
            self.space_ship_display.show()
            self.space_ship_bullets_display.show()
            self.obstacles_display.show()
            self.monster_matrix_display.show()
            self.monster_matrix_bullets_display.show()
            self.score_display.show(10, 10, self.score.getScore())
            self.life_display.show(250, 10, self.space_ship_model.getLife(), 0)
            pygame.display.flip()
            clock.tick(60)
    
    ## @brief get the score of the game
    #  @return score of the game
    def getScore(self):
        return self.score.getScore()

    ## @brief Tell if a player wins the game
    #  @return A boolean value to indicate if this game wins
    def doesWin(self):
        return self.win