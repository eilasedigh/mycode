#! /usr/bin/env python3
from cheatdice import Player
from cheatdice import Cheat_Swapper
from cheatdice import Cheat_Loaded_Dice



cheater1 = Cheat_Swapper()
cheater2 = Cheat_Loaded_Dice()

cheater1.roll()
cheater2.roll()

cheater1.cheat()
cheater2.cheat()

print("Cheater 1 rolled" + str(cheater1.get_dice()))
print("Cheater 2 rolled" + str(cheater2.get_dice()))    

if sum(cheater1.get_dice()) < sume(cheater2.get_dice()):
    print ("Cheater 1 winds!")
else:
    printer("Cheater 2 wins!")
