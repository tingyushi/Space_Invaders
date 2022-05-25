## @file Display.py
#  @author Tingyu Shi
#  @brief Contains multiple classes to display different game elements on to the screen.
#  @date Apr 7, 2022

import pygame

## @brief A class to represent the game window
class WindowSetUp:
    ## @brief Constructor for class WindowSetUp.
    #  @details Create an instance of class WindowSetUp, taking two
    #            arguments.
    #  @param width The width of the screen.
    #  @param height The height of the screen.
    def __init__(self, width, height):
        self.__w = width
        self.__h = height
        self.__screen = pygame.display.set_mode((self.__w, self.__h))
    
    ## @brief Get the screen object
    #  @return Screen object
    def getScreen(self):
        return self.__screen

    ## @brief Set title of the game window
    def setTitle(self):
        pygame.display.set_caption("New Space Invaders")
    
    ## @brief Set icon of the game window
    def setIcon(self):
        icon = pygame.image.load('Picture/spaceship_icon.png')
        pygame.display.set_icon(icon)
    
    ## @brief Set background of the game window
    def setBackground(self):
        background = pygame.image.load("Picture/background.png")
        self.__screen.blit(background, (0, 0))


## @brief A class to display spaceship object.
class SpaceShipDisplay(pygame.sprite.Sprite):
    ## @brief Constructor for class SpaceShipDisplay.
    #  @details Create an instance of class SpaceShipDisplay, taking two
    #            arguments.
    #  @param screen The screen object to display spaceships on.
    #  @param space_ship_group  The sprite group of spaceships
    def __init__(self, screen, space_ship_group):
        self.__screen = screen
        self.__space_ship_group = space_ship_group
    
    ## @brief show spaceship groups on to the screen
    def show(self):
        self.__space_ship_group.draw(self.__screen)

## @brief A class to display bullet object.
class BulletDisplay(pygame.sprite.Sprite):
    ## @brief Constructor for class BulletDisplay.
    #  @details Create an instance of class BulletDisplay, taking two
    #            arguments.
    #  @param screen The screen object to display bullets on.
    #  @param bullets_group  The sprite group of bullets
    def __init__(self, screen, bullets_group):
        self.__screen = screen
        self.__bullets_group = bullets_group
    
    ## @brief show bullets group on to the screen.
    def show(self):
        self.__bullets_group.draw(self.__screen)


## @brief A class to display obstacle object.
class ObstaclesDisplay(pygame.sprite.Sprite):
    ## @brief Constructor for class ObstaclesDisplay.
    #  @details Create an instance of class ObstaclesDisplay, taking two
    #            arguments.
    #  @param screen The screen object to display obstacles on.
    #  @param blocks_group  The sprite group of blocks
    def __init__(self, screen, blocks_group):
        self.__screen = screen
        self.__blocks_group = blocks_group
    
    ## @brief show obstacles on to the screen
    def show(self):
        self.__blocks_group.draw(self.__screen)

## @brief A class to display MonsterMatrix
class MonsterMatrixDisplay(pygame.sprite.Sprite):
    ## @brief Constructor for class MonsterMatrixDisplay.
    #  @details Create an instance of class ObstaclesDisplay, taking two
    #            arguments.
    #  @param screen The screen object to display monster matrix on.
    #  @param blocks_group  The sprite group of monsters
    def __init__(self, screen, monsters_group):
        self.__screen = screen
        self.__monsters_group = monsters_group
    
    ## @brief show monster matrix on the screen
    def show(self):
        self.__monsters_group.draw(self.__screen)

## @brief A class to display score
class ScoreDisplay:
    ## @brief The constructor of ScoreDisplay.
    #  @param screen The screen object to display score on.
    def __init__(self, screen):
        self.__screen = screen
        self.font = pygame.font.Font("freesansbold.ttf", 32)
    
    ## @brief Show score on the screen
    #  @param x x-coordinate of score display
    #  @param y y-coordinate of score display
    #  @param score The score to be displayed on the screen.
    def show(self, x, y, score):
        score_ = self.font.render("Score: " + str(score), True, (255, 255, 255))
        self.__screen.blit(score_, (x, y))

## @brief A class to display life.
class LifeDisplay:
    ## @brief The constructor of LifeDisplay.
    #  @param screen The screen object to display life on.
    def __init__(self, screen):
        self.__screen = screen
        self.font = pygame.font.Font("freesansbold.ttf", 32)

    ## @brief show life on the screen
    #  @param x x-coordinate of life display
    #  @param y y-coordinate of life display
    #  @param life number of lives to be displayed on the screen
    #  @param index  0 means single mode
    #                1 means s1 in double mode
    #                2 means s2 in double mode
    def show(self, x, y, life, index):
        if index == 0:
            life_ = self.font.render("Life: " + str(life), True, (255, 255, 255))
        if index == 1:
            life_ = self.font.render("Life1: " + str(life), True, (255, 255, 255))
        if index == 2:
            life_ = self.font.render("Life2: " + str(life), True, (255, 255, 255))
        self.__screen.blit(life_, (x, y))

## @brief display welcoming message at the beginning of the game
class WelcomeMessageDisplay:
    def __init__(self, screen):
        font1 = pygame.font.Font("freesansbold.ttf", 40)
        font2 = pygame.font.Font("freesansbold.ttf", 32)
        msg = font1.render("Welcome to New Space Invaders!!", True, (255, 128, 0))
        ins = font2.render("Press ENTER to continue", True, (255, 128, 0))
        screen.blit(msg, (70, 200))
        screen.blit(ins, (200, 400))

## @brief display game mode selection message on the screen
class ModeSelectionDisplay:
     def __init__(self, screen):
        font1 = pygame.font.Font("freesansbold.ttf", 40)
        font2 = pygame.font.Font("freesansbold.ttf", 40)
        single = font1.render("Press S for Single Player Mode", True, (255, 128, 0))
        double = font2.render("Press D for Double Player Mode", True, (255, 128, 0))
        screen.blit(single, (70, 200))
        screen.blit(double, (70, 400))

## @brief display game instruction on the screen
class GameInstruction:
    def __init__(self, screen, mode):
        if mode == 's':
            font1 = pygame.font.Font("freesansbold.ttf", 40)
            font2 = pygame.font.Font("freesansbold.ttf", 20)
            font3 = pygame.font.Font("freesansbold.ttf", 18)

            s1_image = pygame.image.load('Picture/spaceship1.png')
            g_image = pygame.image.load('Picture/green_monster.png')
            b_image = pygame.image.load('Picture/blue_monster.png')
            p_image = pygame.image.load('Picture/pink_monster.png')
            g_image = pygame.transform.scale(g_image, (40, 40))
            b_image = pygame.transform.scale(b_image, (40, 40))
            p_image = pygame.transform.scale(p_image, (40, 40))

            msg1 = font1.render("Instruction", True, (255, 128, 0))
            msg2 = font2.render("Press left arrow to move left", True, (225, 128, 0))
            msg3 = font2.render("Press right arrow to move right", True, (225, 128, 0))
            msg4 = font2.render("Press space to shoot bullets", True, (225, 128, 0))
            msg5 = font2.render("10 Points", True, (225, 128, 0))
            msg6 = font2.render("20 Points", True, (225, 128, 0))
            msg7 = font2.render("30 Points", True, (225, 128, 0))
            msg8 = font2.render("Die after being shot once", True, (225, 128, 0))
            msg9 = font2.render("Die after being shot twice", True, (225, 128, 0))
            msg10 = font3.render("Die after being shot three times", True, (225, 128, 0))
            msg11 = font1.render("Press Enter to check Game Items", True, (255, 128, 0))

            screen.blit(msg1, (280, 20))
            screen.blit(msg2, (100, 230))
            screen.blit(msg3, (100, 280))
            screen.blit(msg4, (100, 330))
            screen.blit(msg5, (500, 200))
            screen.blit(msg6, (500, 300))
            screen.blit(msg7, (500, 400))
            screen.blit(msg8, (500, 230))
            screen.blit(msg9, (500, 330))
            screen.blit(msg10, (500, 430))
            screen.blit(msg11, (80, 550))

            screen.blit(s1_image, (20, 250))
            screen.blit(g_image, (450, 200))
            screen.blit(b_image, (450, 300))
            screen.blit(p_image, (450, 400))
        else:
            font1 = pygame.font.Font("freesansbold.ttf", 40)
            font2 = pygame.font.Font("freesansbold.ttf", 20)
            font3 = pygame.font.Font("freesansbold.ttf", 18)

            s1_image = pygame.image.load('Picture/spaceship1.png')
            s2_image = pygame.image.load('Picture/spaceship2.png')
            g_image = pygame.image.load('Picture/green_monster.png')
            b_image = pygame.image.load('Picture/blue_monster.png')
            p_image = pygame.image.load('Picture/pink_monster.png')
            g_image = pygame.transform.scale(g_image, (40, 40))
            b_image = pygame.transform.scale(b_image, (40, 40))
            p_image = pygame.transform.scale(p_image, (40, 40))

            msg1 = font1.render("Instruction", True, (255, 128, 0))
            msg2 = font2.render("Press left arrow to move left", True, (225, 128, 0))
            msg3 = font2.render("Press right arrow to move right", True, (225, 128, 0))
            msg4 = font2.render("Press space to shoot bullets", True, (225, 128, 0))
            msg5 = font2.render("10 Points", True, (225, 128, 0))
            msg6 = font2.render("20 Points", True, (225, 128, 0))
            msg7 = font2.render("30 Points", True, (225, 128, 0))
            msg8 = font2.render("Die after being shot once", True, (225, 128, 0))
            msg9 = font2.render("Die after being shot twice", True, (225, 128, 0))
            msg10 = font3.render("Die after being shot three times", True, (225, 128, 0))
            msg11 = font2.render("Press A to move left", True, (225, 128, 0))
            msg12 = font2.render("Press D to move right", True, (225, 128, 0))
            msg13 = font2.render("Press S to shoot bullets", True, (225, 128, 0))
            msg14 = font1.render("Press Enter to check Game Items", True, (255, 128, 0))

            screen.blit(msg1, (280, 20))
            screen.blit(msg2, (100, 180))
            screen.blit(msg3, (100, 230))
            screen.blit(msg4, (100, 280))
            screen.blit(msg5, (500, 200))
            screen.blit(msg6, (500, 300))
            screen.blit(msg7, (500, 400))
            screen.blit(msg8, (500, 230))
            screen.blit(msg9, (500, 330))
            screen.blit(msg10, (500, 430))
            screen.blit(msg11, (100, 380))
            screen.blit(msg12, (100, 430))
            screen.blit(msg13, (100, 480))
            screen.blit(msg14, (80, 550))

            screen.blit(s1_image, (20, 200))
            screen.blit(s2_image, (20, 400))
            screen.blit(g_image, (450, 200))
            screen.blit(b_image, (450, 300))
            screen.blit(p_image, (450, 400))


## @brief display game items introduction on the screen
class GameItemIntroductionDisplay:
    def __init__(self, screen):
        font1 = pygame.font.Font("freesansbold.ttf", 40)
        font2 = pygame.font.Font("freesansbold.ttf", 20)

        msg1 = font1.render("Game Items Introduction", True, (255, 128, 0))
        msg2 = font2.render("Increase one life to the spaceship(5 maximum)", True, (225, 128, 0))
        msg3 = font2.render("Kill four random monsters", True, (225, 128, 0))
        msg4 = font2.render("Increase one bullet for the spaceship(3 maximum)", True, (225, 128, 0))
        msg5 = font1.render("Press Enter to Start Game!", True, (255, 128, 0))
        
        heart_img = pygame.image.load('Picture/heart.png')
        heart_img = pygame.transform.scale(heart_img, (70, 70))
        bomb_img = pygame.image.load('Picture/bomb.png')
        bomb_img = pygame.transform.scale(bomb_img, (70, 70))
        ammo_img = pygame.image.load('Picture/ammo.png')
        ammo_img = pygame.transform.scale(ammo_img, (70, 70))

        screen.blit(msg1, (160, 20))
        screen.blit(msg2, (250, 150))
        screen.blit(msg3, (250, 300))
        screen.blit(msg4, (250, 450))
        screen.blit(msg5, (150, 550))

        screen.blit(heart_img, (160, 130))
        screen.blit(bomb_img, (160, 280))
        screen.blit(ammo_img, (160, 430))

## @brief display message when a player loses a game
class LoseDisplay:
    def __init__(self, screen, score):
        font1 = pygame.font.Font("freesansbold.ttf", 40)
        msg1 = font1.render("You Lose!", True, (255, 128, 0))
        msg2 = font1.render("Press ENTER to Exit", True, (255, 128, 0))
        msg3 = font1.render("Score: " + str(score), True, (255, 128, 0))

        screen.blit(msg1, (300, 200))
        screen.blit(msg2, (200, 400))
        screen.blit(msg3, (300, 300))

## @brief display message when a player wins a game
class WinDisplay:
    def __init__(self, screen, score):
        font1 = pygame.font.Font("freesansbold.ttf", 40)
        msg1 = font1.render("You Win!", True, (255, 128, 0))
        msg2 = font1.render("Press ENTER to Exit", True, (255, 128, 0))
        msg3 = font1.render("Score: " + str(score), True, (255, 128, 0))

        screen.blit(msg1, (300, 200))
        screen.blit(msg2, (200, 400))
        screen.blit(msg3, (300, 300))