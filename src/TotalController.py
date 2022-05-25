## @file TotalController.py
#  @author Tingyu Shi
#  @brief Contains a class to represent the controller of the overall game.
#  @date Apr 7, 2022
import pygame
import sys
from SingleController import *
from DoubleController import *
from Display import *

## @brief A class representing the controller of the overall game
class TotalController:
    ## @brief Constructor of the TotalController
    def __init__(self):
        self.window = WindowSetUp(800, 600)
        self.screen = self.window.getScreen()
        self.running = True

    ## @brief Run the total controller
    #  @detail Including welcoming message, game mode selection
    #          game instruction, game items introduction and choosing which controller to use 
    #          based on the user input.
    def run(self):
        self.window.setIcon()
        self.window.setTitle()
        #welcoming message
        while self.running:
            self.window.setBackground()
            WelcomeMessageDisplay(self.screen)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.running = False
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
        
        self.running = True

        #game mode selection
        while self.running:
            self.window.setBackground()
            ModeSelectionDisplay(self.screen)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        mode = 's'
                        self.running = False
                    if event.key == pygame.K_d:
                        mode = 'd'
                        self.running = False
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
        
        self.running = True

        #game instruction
        while self.running:
            self.window.setBackground()
            GameInstruction(self.screen, mode)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.running = False
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
        
        self.running = True

        #game item introduction
        while self.running:
            self.window.setBackground()
            GameItemIntroductionDisplay(self.screen)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.running = False
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
        
        self.running = True
        
        if mode == 's':
            game = SingleController(self.window, self.screen)
            game.run()
        else:
            game = DoubleController(self.window, self.screen)
            game.run()      
        
        score = game.getScore()
        
        if game.doesWin():
            while self.running:
                self.window.setBackground()
                WinDisplay(self.screen, score)
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            self.running = False
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                pygame.display.update()
        else:
            while self.running:
                self.window.setBackground()
                LoseDisplay(self.screen, score)
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            self.running = False
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                pygame.display.update()