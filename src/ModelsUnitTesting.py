## @file ModelsUnitTesting.py
#  @author Tingyu Shi, Jiacheng Wu, Qianlin Chen
#  @brief Contains multiple classes to test game models.
#  @date Apr 7, 2022

'''
Some functions of models can not be testing using unit testing since they are user inputs related.
MonsterMatrix model is tested manually
Obstacle model is tested manually
'''

from pytest import *
from Ammo import *
from Heart import *
from Bomb import *
from Bullet import *
from Monster import *
from MonsterColor import *
from Score import *
from SpaceShip import *

class TestAmmo:
    def setup_method(self, method):
        self.ammo = Ammo(1, 1, 1)

    def teardown_method(self, method):
        self.ammo = None
    
    def test_getItemType(self):
        assert self.ammo.getItemType() == 3
    
    def test_update1(self):
        self.ammo.update(1)
        assert self.ammo.rect.x == 2
        assert self.ammo.rect.y == 1
    
    def test_update2(self):
        self.ammo.update(-1)
        assert self.ammo.rect.x == 0
        assert self.ammo.rect.y == 1



class TestHeart:
    def setup_method(self, method):
        self.heart = Heart(1, 1, 1)

    def teardown_method(self, method):
        self.heart = None
    
    def test_getItemType(self):
        assert self.heart.getItemType() == 2
    
    def test_update1(self):
        self.heart.update(1)
        assert self.heart.rect.x == 2
        assert self.heart.rect.y == 1
    
    def test_update2(self):
        self.heart.update(-1)
        assert self.heart.rect.x == 0
        assert self.heart.rect.y == 1


class TestBomb:
    def setup_method(self, method):
        self.bomb = Bomb(1, 1, 1)

    def teardown_method(self, method):
        self.bomb = None
    
    def test_getItemType(self):
        assert self.bomb.getItemType() == 4
    
    def test_update1(self):
        self.bomb.update(1)
        assert self.bomb.rect.x == 2
        assert self.bomb.rect.y == 1
    
    def test_update2(self):
        self.bomb.update(-1)
        assert self.bomb.rect.x == 0
        assert self.bomb.rect.y == 1


class TestBullet:
    def setup_method(self, method):
        self.bullet1 = Bullet(10, 10, (10, 20), 1, 1)
        self.bullet2 = Bullet(10, 10, (10, 20), -1, 1)
    
    def teardown_method(self, method):
        self.bullet = None
    
    def test_move1(self):
        self.bullet1.move()
        assert self.bullet1.rect.center[1] == 11
    
    def test_move1(self):
        self.bullet2.move()
        assert self.bullet2.rect.center[1] == 9


class TestMonster:
    def setup_method(self, method):
        self.monster1 = Monster(10, 10, MonsterColor.GREEN, 5)
        self.monster2 = Monster(10, 10, MonsterColor.BLUE, 5)
        self.monster3 = Monster(10, 10, MonsterColor.PINK, 5)
    
    def teardown_method(self, method):
        self.monster1 = None
        self.monster2 = None
        self.monster3 = None

    def test_reduceLife_isDead_green(self):
        self.monster1.reduceLife()
        assert self.monster1.isDead()

    def test_reduceLife_isDead_blue(self):
        self.monster2.reduceLife()
        assert not self.monster2.isDead()
        self.monster2.reduceLife()
        assert self.monster2.isDead()

    def test_reduceLife_isDead_pink(self):
        self.monster3.reduceLife()
        assert not self.monster3.isDead()
        self.monster3.reduceLife()
        assert not self.monster3.isDead()
        self.monster3.reduceLife()
        assert self.monster3.isDead()
    
    def test_getItemType(self):
        assert self.monster1.getItemType() == 1
        assert self.monster2.getItemType() == 1
        assert self.monster3.getItemType() == 1

    def test_update(self):
        self.monster1.update(1)
        assert self.monster1.rect.x == 15
        self.monster2.update(-1)
        assert self.monster2.rect.x == 5

class TestScore:
    def setup_method(self, method):
        self.score = Score()
    
    def teardown_method(self, method):
        self.score = None
    
    def test(self):
        self.score.increase(10)
        self.score.getScore() == 10

class TestSpaceShip:
    def setup_method(self, method):
        self.s = SpaceShip(10, 10, (10, 10), 10, 10)

    def teardown_method(self, method):
        self.s = None
    
    def test_reduceLife(self):
        self.s.reduceLife()
        self.s.reduceLife()
        self.s.getLife() == 3

    def test_setLife(self):
        self.s.setLife(3)
        self.s.getLife() == 3

    def test_increaseLife(self):
        self.s.setLife(3)
        self.s.increaseLife()
        self.s.getLife() == 4
        self.s.increaseLife()
        self.s.getLife() == 5
        self.s.increaseLife()
        self.s.getLife() == 5
