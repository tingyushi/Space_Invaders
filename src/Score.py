## @file Score.py
#  @author Tingyu Shi, Jiacheng Wu, Qianlin Chen
#  @brief Contains a class to represent the score of the game.
#  @date Apr 7, 2022

## @brief A class representing the score of the game
class Score:
    ## @brief constructor of the score
    def __init__(self):
        self.__s = 0
    
    ## @brief increase the socre
    #  @param amount the amount of socre to be added 
    def increase(self, amount):
        self.__s += amount

    ## @brief get the score
    #  @return score
    def getScore(self):
        return self.__s