


import random
import sys

sys.path.append('..')
import package_KingOfGlory.global_var as GLV

from package_KingOfGlory.class_eq_move import EQMove
from package_KingOfGlory.class_eq_mana import EQMana
from package_KingOfGlory.class_eq_defense import EQDefense
from package_KingOfGlory.class_eq_attack import EQAttack
from package_KingOfGlory.class_hero import Hero
from package_KingOfGlory.class_soldier import Soldier


for i in range (1,10):
    h=Hero()
    eq =EQAttack()
    s=Soldier(h,eq)
    s.show_me()
    print(i)
