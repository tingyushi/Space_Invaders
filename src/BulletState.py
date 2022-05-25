## @file BulletState.py
#  @author Tingyu Shi
#  @brief Contains a Enum class to represent two states of the bullet.
#  @date Apr 7, 2022

from enum import Enum

## @brief A enum class to represent two states of bullets(fire and ready to fire)

class BulletState(Enum):
    READY = 1
    FIRE = 2

