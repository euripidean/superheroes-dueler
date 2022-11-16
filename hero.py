"""
Hero class
"""

import random
from ability import Ability
from armor import Armor

class Hero:
  # We want our hero to have a default "starting_health",
  # so we can set that in the function header.
    def __init__(self, name, starting_health=100):
        '''Instance properties:
        name: String
        starting_health: Integer
        current_health: Integer
        '''
        self.abilities = list()
        self.armor = list()
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

    def fight(self, opponent):
        """Current Hero will take turns fighting the opponent hero passed in."""
        winner = random.randint(0,1)
        if winner == 1:
            print(f'{self.name} defeats {opponent.name}!')
        else:
            print(f'{opponent.name} defeats {self.name}!')

    def add_ability(self, ability):
        """Add ability to abilities list"""
        self.abilities.append(ability)

    def attack(self):
        '''Calculate the total damage from all ability attacks.
            return: total_damage:Int
        '''
        # start our total out at 0
        total_damage = 0
        # loop through all of our hero's abilities
        for ability in self.abilities:
          # add the damage of each attack to our running total
          total_damage += ability.attack()
        # return the total damage
        return total_damage

    def add_armor(self, armor):
        '''Add armor to self.armors
          Armor: Armor Object
        '''
        self.armor.append(armor)

    def defend(self):
        '''Calculate the total block amount from all armor blocks.
          return: total_block:Int
        '''
        if self.current_health > 0 and not self.armor:
            total_block = 0
            for armor in self.armor:
              total_block += armor.block()
            return total_block
        else:
          return 0

    def take_damage(self, damage):
        '''Updates self.current_health to reflect the damage minus the defense.
        '''
        # TODO: Create a method that updates self.current_health to the current
        # minus the the amount returned from calling self.defend(damage).
        defense = self.defend()
        total_damage = damage - defense
        if total_damage > 0:
          self.current_health -= total_damage

    def is_alive(self):  
        '''Return True or False depending on whether the hero is alive or not.
        '''
        if self.current_health <= 0:
            return False
        else:
            return True

    def fight(self, opponent):  
        ''' Current Hero will take turns fighting the opponent hero passed in.
        '''
        if not self.abilities and not opponent.abilities:
            print("Draw")
        else:
            while self.is_alive() and opponent.is_alive():
                opp_attack = opponent.attack()
                self.take_damage(opp_attack)
                self_attack = self.attack()
                opponent.take_damage(self_attack)
            if self.is_alive():
                print(f'{self.name} won!')
            elif opponent.is_alive():
                print(f'{opponent.name} won!')





if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.

    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)
