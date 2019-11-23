import random

class Ability:
    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = max_damage

    def attack(self):
        random_value = random.randint(0, self.max_damage)
        return random_value

class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block

    def block(self):
        random_value = random.randint(0, self.max_block)
        return random_value

class Weapon(Ability):
    def attack(self):
        half_max_damage= self.max_damage // 2
        random_value = random.randint(half_max_damage, self.max_damage)
        return random_value

class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

        self.abilities = list()
        self.armors = list()

    def add_ability(self, ability):
        self.abilities.append(ability)

    def add_armor(self, armor):
        self.armors.append(armor)

    def add_weapon(self, weapon):
        self.abilities.append(weapon)

    def attack(self):

        total_damage = 0

        for ability in self.abilities:
            total_damage += ability.attack()

        return total_damage

    def defend(self):

        total_block = 0

        for armor in self.armors:
            total_block += armor.block()

        return total_block

    def take_damage(self, damage):
        defense = self.defend()
        self.current_health -= damage - defense

    def is_alive(self):
        
        if self.current_health <= 0:
            return False
        
        return True

    def fight(self, opponent):

        if self.abilities == [] and opponent.abilities == []:
            print("Draw")
        else:
            while self.is_alive() and opponent.is_alive():
                my_dmg = self.attack()
                opponent.take_damage(my_dmg)
                
                if opponent.is_alive():
                    opponent_dmg = opponent.attack()
                    self.take_damage(opponent_dmg)

                    if self.is_alive():
                        continue
                    else:
                        print(f"{opponent.name} wins!")
                else:
                    print(f"{self.name} wins!")

class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = list()

    def remove_hero(self, name):
        
        foundHero = False

        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)

                foundHero = True

        if not foundHero:
            return 0

    def view_all_heroes(self):
        
        for hero in self.heroes:
            print(hero.name)

    def add_hero(self, hero):
        self.heroes.append(hero)

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    hero = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)
    hero.add_weapon(weapon)
    print(hero.attack())